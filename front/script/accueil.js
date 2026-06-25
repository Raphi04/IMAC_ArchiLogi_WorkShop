idName = localStorage.getItem("idName");
pwd = localStorage.getItem("pwd");

animalContainer = document.getElementById("notreSelection_card-container");

async function getAnimals() {
  try {
    const response = await fetch(back + "fiche_animal", {
      method: "GET",
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
                            <p>${fiche_animal["moyenne-note"] ? fiche_animal["moyenne-note"] : "Non noté"}</p>
                            <img src="./ressource/icons/stars.svg" alt="">
                        </div>
                    </div>
                    <p class="animalCard_categorie">${fiche_animal["espece"]["name"]}</p>
                    <p>${fiche_animal["animal"]["description"]}</p>
                </div>
            </div>
            <!-- Deuxieme partie de la carte -->
            <div class="animalCardCommentaire-container">
                <!-- Commentaires -->
                  <div class="commentairesContainer${fiche_animal["animal"]["idAnimal"]}">
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
                <form class="commentSender">
                    <input class="commentaire1 commentaire${fiche_animal["animal"]["idAnimal"]}" type="text" placeholder="Écrire un commentaire..." name="comment">
                    <input type="hidden" value="${fiche_animal["animal"]["idAnimal"]}" name="idAnimal">
                    <input class="submitCommentaire" type="submit" value="Envoyer">
                    <p class="errorMessage"></p>
                </form>
            </div>
          </div>
        `;
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

  /* Get animals */
  await getAnimals();

  allForms = document.querySelectorAll(".commentSender");

  allForms.forEach((form) => {
    form.addEventListener("submit", async function (e) {
      e.preventDefault();
      const formData = new FormData(this);

      try {
        const response = await fetch(back + "commentaire", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            idName: localStorage.getItem("idName"),
            idAnimal: formData.get("idAnimal"),
            commentaire: formData.get("comment"),
          }),
        });

        if (!response.ok) {
          throw new Error(`Ça marche pas ! ${response.status}`);
        }

        data = await response.json();

        if (data["code"] == 200) {
          document.querySelector(".commentaire" + formData.get("idAnimal")).value = "";

          const commentContainer = document.querySelector(
            ".commentairesContainer" + formData.get("idAnimal"),
          );

          commentContainer.innerHTML += `
            <div class="commentaire">
              <p class="username">@${localStorage.getItem("idName")}</p>
              <p class="message">${formData.get("comment")}</p>
            </div>
          `;

          commentContainer.scrollTo(0, commentContainer.scrollHeight);
        } else {
          this.children[3].innerHTML = data["message"];
        }
      } catch (error) {
        console.log(error);
      }
    });
  });
}

onLoad();
