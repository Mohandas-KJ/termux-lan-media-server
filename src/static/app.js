async function loadmovies() {
    const status = document.getElementById("status");
    const container = document.getElementsById("movies");
    const query = document.getElementsById("search").value.toLowerCase();

    status.innerText = "Loading....";
    status.innerHTML = "";
}