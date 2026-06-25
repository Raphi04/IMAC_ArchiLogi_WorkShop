function menuOn1() {
  menuOpen = document.getElementById("menu");
  menuOff = document.getElementById("menuNotDisplay");
  main1 = document.getElementById("accueil-main");
  footer1 = document.getElementById("footer-main");

  menuOpen.style.display = "flex";
  menuOff.style.display = "none";
  main1.style.display = "none";
  footer1.style.display = "none";
}

function menuOff1() {
  menuOpen = document.getElementById("menu");
  menuOff = document.getElementById("menuNotDisplay");
  main1 = document.getElementById("accueil-main");
  footer1 = document.getElementById("footer-main");
  menuOpen.style.display = "none";
  menuOff.style.display = "flex";
  main1.style.display = "flex";
  main1.style.flexDirection = "column";
  footer1.style.display = "flex";
}
