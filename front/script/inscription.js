form = document.getElementById("inscriptionForm");
idName = document.getElementById("idName");
username = document.getElementById("username");
pwd = document.getElementById("pwd");

errorMessage = document.getElementById("errorMessage");

form.addEventListener("submit", async function (event) {
  event.preventDefault();
  response = await userRegister(idName.value, username.value, pwd.value);
  errorMessage.innerHTML = response || "";
});
