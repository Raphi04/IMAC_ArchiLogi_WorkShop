async function userConnect(idName, pwd) {
  try {
    const response = await fetch(back + "utilisateur/connect", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        idName: idName,
        pwd: pwd,
      }),
    });

    if (!response.ok) {
      throw new Error(`Ça marche pas ! ${response.status}`);
    }

    data = await response.json();

    if (data["code"] == 200) {
      localStorage.setItem("idName", idName);
      localStorage.setItem("pwd", pwd);

      window.location.replace(front + "index.html");
    } else {
      return data["message"];
    }
  } catch (error) {
    console.log(error);
  }
}

async function userRegister(idName, username, pwd) {
  try {
    const response = await fetch(back + "utilisateur", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        idName: idName,
        username: username,
        pwd: pwd,
      }),
    });

    if (!response.ok) {
      throw new Error(`Ça marche pas ! ${response.status}`);
    }

    data = await response.json();

    if (data["code"] == 200) {
      localStorage.setItem("idName", idName);
      localStorage.setItem("pwd", pwd);

      window.location.replace(front + "index.html");
    } else {
      return data["message"];
    }
  } catch (error) {
    console.log(error);
  }
}

async function checkIfConnected(idName, pwd) {
  try {
    const response = await fetch(back + "utilisateur/connect", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        idName: idName,
        pwd: pwd,
      }),
    });

    if (!response.ok) {
      throw new Error(`Ça marche pas ! ${response.status}`);
    }

    data = await response.json();

    if (data["code"] != 200) {
      window.location.replace(front + "page/connexion.html");
    } else {
      return 200;
    }
  } catch (error) {
    console.log(error);
  }
}

function userDisconnect() {
  localStorage.removeItem("idName");
  localStorage.removeItem("pwd");
  window.location.replace(front + "page/connexion.html");
}
