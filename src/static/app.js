async function loadmovies() {
    const status = document.getElementById("status");
    const container = document.getElementsById("movies");
    const query = document.getElementsById("search").value.toLowerCase();

    status.innerText = "Loading....";
    status.innerHTML = "";

    try{
        const res = await fetch("/list");
        const data = await res.json();

        const filtered = data.files.filter(f => f.toLowerCase().includes(query));

        status.innerText = `Found ${filtered.length} file(s).`;

        for (const file of filtered){
            const div = document.createElement("div");
            div.className = "movie";

            const name = document.createElement("div");
            name.className = "name";
            name.innerText = file;

            const actions = document.createElement("div");
            actions.className = "actions";

        }
    }
    catch(e){

    }
}