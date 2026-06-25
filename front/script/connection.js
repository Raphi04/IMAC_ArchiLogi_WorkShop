form = document.getElementById("connexionForm");
idName = document.getElementById("idName");
pwd = document.getElementById("pwd");

errorMessage = document.getElementById("errorMessage");

form.addEventListener("submit", async function (event) {
  event.preventDefault();
  response = await userConnect(idName.value, pwd.value);
  errorMessage.innerHTML = response || "";
});
