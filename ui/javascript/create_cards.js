const LOGO_DIRECTORY = "../assets/app_icons/";
const CARD_DATA = [
    {
        title: "VS Code",
        image: LOGO_DIRECTORY + "vs_code_logo.png"
    },
    {
        title: "Auto-Py-To-Exe",
        image: LOGO_DIRECTORY + "python_logo.png"
    }

];

const container = document.getElementById("app-grid");

function renderCards(dataArray){
    container.innerHTML = "";
    dataArray.forEach(item => {
        const cardElement = document.createElement("div");
        cardElement.classList.add("card");

        cardElement.innerHTML = `
            <img src="${item.image}" alt="${item.title}" class="app-card">
            <div class="card-body">
                <h3 class="card-title">${item.title}</h3>
            </div>`;

        container.appendChild(cardElement);

    });
}
renderCards(CARD_DATA)