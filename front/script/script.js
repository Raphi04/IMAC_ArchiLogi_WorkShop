function menuOn1(){
    menuOpen=document.getElementById("menu")
    menuOff=document.getElementById("menuNotDisplay")
    main1=document.getElementById("accueil-main")
    footer1=document.getElementById("footer-main")

    menuOpen.style.display="flex"
    menuOff.style.display="none"
    main1.style.display="none"
    footer1.style.display="none"

}

function menuOff1(){
    menuOpen=document.getElementById("menu")
    menuOff=document.getElementById("menuNotDisplay")
    main1=document.getElementById("accueil-main")
    footer1=document.getElementById("footer-main")
    menuOpen.style.display="none"
    menuOff.style.display="flex"
    main1.style.display="flex"
    main1.style.flexDirection="column"
    footer1.style.display="flex"
}

isSelectedOrNot=0

function isSelected(animalNumber){
    selected=document.getElementById("selection"+animalNumber)
    if(isSelectedOrNot%2==0){
        selected.value="Sélectionner"
        selected.style.backgroundColor="#FFFFFF"
        selected.style.borderColor="#000000"
        selected.style.color="#000000"
        isSelectedOrNot++
    }else if(isSelectedOrNot%2==1){
        selected.value="Sélectionné"
        selected.style.backgroundColor="#2D7819"
        selected.style.borderColor="#2D7819"
        selected.style.color="#FFFFFF"
        isSelectedOrNot++
    }
}

