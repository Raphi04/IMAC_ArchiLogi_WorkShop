idName = localStorage.getItem("idName");
pwd = localStorage.getItem("pwd");

async function onLoad() {
  code = await checkIfConnected(idName, pwd);

  if (code == 200) {
    document.getElementsByTagName("body")[0].classList.remove("disappear");
  }
}

onLoad();
