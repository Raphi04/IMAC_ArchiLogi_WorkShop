idName = localStorage.getItem("idName");
pwd = localStorage.getItem("pwd");

const inputDate = document.getElementById("date");
const activiteContainer = document.getElementById("notreSelection_filtre");

const now = new Date();
const currentDate = now.getFullYear() + "-0" + (now.getMonth() + 1) + "-" + now.getDate();

const urlParams = new URLSearchParams(window.location.search);
var idActivite = urlParams.get("idActivite");

const animalContainer = document.getElementById("notreSelection_card-container");

const message = document.getElementById("message");

var allAnimalsSelected = [];

async function getAllActivities() {
  try {
    const response = await fetch(back + "activite", {
      method: "GET",
    });

    if (!response.ok) {
      throw new Error(`Ça marche pas ! ${response.status}`);
    }

    data = await response.json();

    if (data["code"] == 200) {
      for (let i = 0; i < data["activites"].length; i++) {
        if (!idActivite) {
          if (i == 0) {
            idActivite = data["activites"][i]["idActivite"];
            activiteContainer.innerHTML += `
              <button id="activite${data["activites"][i]["idActivite"]}" class="selected" onClick="changeActivity(${data["activites"][i]["idActivite"]})">${data["activites"][i]["name"]}</button>
            `;
          } else {
            activiteContainer.innerHTML += `
              <button id="activite${data["activites"][i]["idActivite"]}" onClick="changeActivity(${data["activites"][i]["idActivite"]})">${data["activites"][i]["name"]}</button>
            `;
          }
        } else {
          if (data["activites"][i]["idActivite"] == idActivite) {
            activiteContainer.innerHTML += `
              <button id="activite${data["activites"][i]["idActivite"]}" class="selected" onClick="changeActivity(${data["activites"][i]["idActivite"]})">${data["activites"][i]["name"]}</button>
            `;
          } else {
            activiteContainer.innerHTML += `
              <button id="activite${data["activites"][i]["idActivite"]}" onClick="changeActivity(${data["activites"][i]["idActivite"]})">${data["activites"][i]["name"]}</button>
            `;
          }
        }
      }
    }
  } catch (error) {
    console.log(error);
  }
}

async function getAnimals(idActivite, date) {
  allAnimalsSelected = [];
  message.innerHTML = "";
  window.history.pushState(
    {},
    "",
    window.location.origin + window.location.pathname + "?idActivite=" + idActivite,
  );
  animalContainer.innerHTML = "";

  document.getElementsByClassName("selected")[0].classList.remove("selected");
  document.getElementById("activite" + idActivite).classList.add("selected");
  try {
    const response = await fetch(back + "activite/animal/" + idActivite, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        date: date,
      }),
    });

    if (!response.ok) {
      throw new Error(`Ça marche pas ! ${response.status}`);
    }

    data = await response.json();

    if (data["code"] == 200 && data["fiches_animal"].length > 0) {
      data["fiches_animal"].forEach((fiche_animal) => {
        animalContainer.innerHTML += `
          <div class="animalCard">
            <!-- Première partie de la carte -->
            <div>
                <img src="${fiche_animal["animal"]["imageUrl"]}" alt="">
                <div class="animalDescription-container">
                    <div class="animalCard_nameAndrating">
                        <h3 class="animalCard_name">${fiche_animal["animal"]["name"]}</h3>
                        <div class="animalCard_rating">
                            <p>${fiche_animal["moyenne-note"] ? fiche_animal["moyenne-note"] : "Non noté"}</p>
                            <img src="../ressource/icons/stars.svg" alt="">
                        </div>
                    </div>
                    <p class="animalCard_categorie">${fiche_animal["espece"]["name"]}</p>
                    <p>${fiche_animal["animal"]["description"]}</p>
                    <input id="selection${fiche_animal["animal"]["idAnimal"]}" onclick="isSelected(${fiche_animal["animal"]["idAnimal"]})" class="submitCommentaire  ${allAnimalsSelected.includes(fiche_animal["animal"]["idAnimal"]) ? "selectionner" : ""}" type="button" value="Sélectionner">
                </div>
            </div>
            <!-- Deuxieme partie de la carte -->
            <div class="animalCardCommentaire-container">
                <!-- Commentaires -->
                <div>
                  ${
                    fiche_animal["commentaires"]
                      ? fiche_animal["commentaires"]
                          .map((commentaire) => {
                            return `
                        <div class="commentaire">
                          <p class="username">@${commentaire["utilisateur"]["idName"]}</p>
                          <p class="message">${commentaire["commentaire"]["commentaire"]}</p>
                        </div>
                      `;
                          })
                          .join("")
                      : ""
                  }
                </div>
            </div>
        </div>`;
      });
    } else {
      animalContainer.innerHTML = `<div id="noAnimal">Il n'y a pas d'animaux disponibles</div>`;
    }
  } catch (error) {
    console.log(error);
  }
}

async function onLoad() {
  code = await checkIfConnected(idName, pwd);

  if (code == 200) {
    document.getElementsByTagName("body")[0].classList.remove("disappear");
  }

  await getAllActivities();

  await getAnimals(idActivite, currentDate);
}

function changeActivity(idActivite) {
  getAnimals(idActivite, inputDate.value);
}

function changeDate() {
  getAnimals(idActivite, inputDate.value);
}

onLoad();

inputDate.value = currentDate;

function remove(arr, item) {
  for (var i = arr.length; i--; ) {
    if (arr[i] === item) {
      arr.splice(i, 1);
    }
  }
}

function isSelected(animalNumber) {
  console.log(animalNumber);
  selected = document.getElementById("selection" + animalNumber);
  if (selected.classList.contains("selectionner")) {
    selected.classList.remove("selectionner");
    selected.value = "Selectionner";
    remove(allAnimalsSelected, animalNumber);
  } else {
    selected.classList.add("selectionner");
    selected.value = "Selectionné";

    if (!allAnimalsSelected.includes(animalNumber)) {
      allAnimalsSelected.push(animalNumber);
    }
  }
  console.log(allAnimalsSelected);
}

form = document.getElementById("reservationForm");

form.addEventListener("submit", async function (event) {
  event.preventDefault();

  allAnimalsSelected.forEach((idAnimal) => {
    createParticipation(idAnimal);
  });
});

async function createParticipation(idAnimal) {
  try {
    const response = await fetch(back + "participe", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        idName: localStorage.getItem("idName"),
        idAnimal: idAnimal,
        idActivite: idActivite,
        date: inputDate.value,
      }),
    });

    console.log(inputDate.value);

    if (!response.ok) {
      throw new Error(`Ça marche pas ! ${response.status}`);
    }

    data = await response.json();

    message.innerHTML = "";
    message.classList.remove("sucess");
    message.classList.remove("error");

    if (data["code"] == 200) {
      getAnimals(idActivite, inputDate.value);
      message.classList.add("success");
      message.innerHTML = data["message"];
    } else {
      message.classList.add("error");
      message.innerHTML = data["message"];
    }
  } catch (error) {
    console.log(error);
  }
}
