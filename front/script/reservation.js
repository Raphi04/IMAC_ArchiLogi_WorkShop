idName = localStorage.getItem("idName");
pwd = localStorage.getItem("pwd");

const inputDate = document.getElementById("date");
const activiteContainer = document.getElementById("notreSelection_filtre");

const now = new Date();
const currentDate = now.getFullYear() + "-0" + now.getMonth() + "-" + now.getDate();

const urlParams = new URLSearchParams(window.location.search);
var idActivite = urlParams.get("idActivite");

const animalContainer = document.getElementById("notreSelection_card-container");

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
            <button id="activite${data["activites"][i]["idActivite"]}" class="selected">${data["activites"][i]["name"]}</button>
            `;
          } else {
            activiteContainer.innerHTML += `
            <button id="activite${data["activites"][i]["idActivite"]}">${data["activites"][i]["name"]}</button>
            `;
          }
        } else {
          if (data["activites"][i]["idActivite"] == idActivite) {
            activiteContainer.innerHTML += `
              <button id="activite${data["activites"][i]["idActivite"]}" class="selected">${data["activites"][i]["name"]}</button>
            `;
          } else {
            activiteContainer.innerHTML += `
              <button id="activite${data["activites"][i]["idActivite"]}">${data["activites"][i]["name"]}</button>
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

    if (data["code"] == 200) {
      data["fiches_animal"].forEach((fiche_animal) => {
        animalContainer.innerHTML += `
          <div class="animalCard mammifere">
            <!-- Première partie de la carte -->
            <div>
                <img src="${fiche_animal["animal"]["imageUrl"]}" alt="">
                <div class="animalDescription-container">
                    <div class="animalCard_nameAndrating">
                        <h3 class="animalCard_name">${fiche_animal["animal"]["name"]}</h3>
                        <div class="animalCard_rating">
                            <p>${fiche_animal["moyenne-note"]}</p>
                            <img src="../ressource/icons/stars.svg" alt="">
                        </div>
                    </div>
                    <p class="animalCard_categorie">${fiche_animal["espece"]["name"]}</p>
                    <p>${fiche_animal["animal"]["description"]}</p>
                    <input id="selection1" onclick="isSelected(1)" class="submitCommentaire" type="button" value="Sélectionner">
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

onLoad();

inputDate.value = currentDate;

isSelectedOrNot = 0;

function isSelected(animalNumber) {
  selected = document.getElementById("selection" + animalNumber);
  if (isSelectedOrNot % 2 == 0) {
    selected.value = "Sélectionner";
    selected.style.backgroundColor = "#FFFFFF";
    selected.style.borderColor = "#000000";
    selected.style.color = "#000000";
    isSelectedOrNot++;
  } else if (isSelectedOrNot % 2 == 1) {
    selected.value = "Sélectionné";
    selected.style.backgroundColor = "#2D7819";
    selected.style.borderColor = "#2D7819";
    selected.style.color = "#FFFFFF";
    isSelectedOrNot++;
  }
}
