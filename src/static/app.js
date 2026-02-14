function TotalSize(files_f){
    let total = 0;

    for (const f of files_f){
        total += f.size;
    }

    return total;
}

function formatSize(bytes){
    const units = ["B","KB","MB","GB","TB"];
    let i = 0;

    while (bytes >= 1024 && i < units.length - 1){
        bytes /= 1024;
        i++;
    }

    return bytes.toFixed(1) + " " + units[i];
}

async function loadmovies() {
    const status = document.getElementById("status");
    const container = document.getElementById("movies");
    const query = document.getElementById("search").value.toLowerCase();
    const indicator = document.getElementById("occupied");

    status.innerText = "Loading....";
    status.innerHTML = "";

    try{
        const res = await fetch("/list");
        const data = await res.json();

        const filtered = data.files.filter(f => f.name.toLowerCase().includes(query));

        status.innerText = `Found ${filtered.length} file(s).`;

        container.innerHTML = "";
        const total_size = formatSize(TotalSize(filtered));

        indicator.innerText = `Total Size: ${total_size}`;


        for (const file of filtered){
            const div = document.createElement("div");
            div.className = "movie";

            const name = document.createElement("div");
            name.className = "name";
            name.innerText = file.name + " (" + formatSize(file.size) + ")";

            const actions = document.createElement("div");
            actions.className = "actions";

            const plyButton = document.createElement("button");
            plyButton.className = "secondary";
            plyButton.innerText = "Play";
            plyButton.onclick = () => {
                window.open(`/play/${encodeURIComponent(file.name)}`, "_blank");
            };

            const cpyButton = document.createElement("button");
            cpyButton.className = "secondary";
            cpyButton.innerText = "Copy Link";
            cpyButton.onclick = async () => {
                const url = `${location.origin}/play/${encodeURIComponent(file.name)}`;
                
                try{
                    await navigator.clipboard.writeText(url);
                    alert("Copied: " + url);
                }
                catch (err) {
                    const temp = document.createElement("input");
                    temp.value = url;
                    document.body.appendChild(temp);
                    temp.select();
                    document.execCommand("copy");
                    document.body.removeChild(temp);

                    alert("Copied (fallback): " + url);
                }
            };

            actions.appendChild(plyButton);
            actions.appendChild(cpyButton);

            div.appendChild(name);
            div.appendChild(actions);

            container.appendChild(div);
        }
    }
    catch(e){
        status.innerText = "Failed to Load Movies";
    }
}

document.getElementById("refreshBtn").addEventListener("click", loadmovies);
document.getElementById("search").addEventListener("input", loadmovies);

document.getElementById("uploadForm").addEventListener("submit", async (e) => {
    e.preventDefault();

    const fileInput = document.getElementById("fileInput");
    const uploadStatus = document.getElementById("uploadStatus");

    if(!fileInput.files.length){
        uploadStatus.innerText = "Choose a file first";
        return;
    }

    const formData = new FormData();
    formData.append("file", fileInput.files[0]);

    uploadStatus.innerText = "Uploading....";

    const res = await fetch("/upload", {
        method: "POST",
        body: formData
    });

    if (res.ok){
        const data = await res.json();
        uploadStatus.innerText = "Uploaded: " + data.file;
        fileInput.value = "";
        loadmovies();
    }
    else {
        uploadStatus.innerText = "Upload failed.";
    }
});

loadmovies();