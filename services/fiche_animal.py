from flask import jsonify

import models.fiche_animal as fiche_animalModel
import models.utilisateur as utilisateurModel
import models.espece as especeModel
import models.commentaire as commentaireModel
import models.note as noteModel

def createFiche_animal(name, description, idName, idEspece, imageUrl) :
    # On vérifie que c'est correctement formater
    name = name.strip()

    if(not name) :
        response = {
            "message" : "Il manque le nom de l'animal",
            "code" : 422
        }
        return response

    if(not description) :
        response = {
            "message" : "Il manque la description de l'animal",
            "code" : 422
        }
        return response

    if(not idName) :
        response = {
            "message" : "Il manque l'identifiant utilisateur",
            "code" : 422
        }
        return response

    if(not idEspece) :
        response = {
            "message" : "Il manque l'identifiant de l'espèce",
            "code" : 422
        }
        return response

    if(not imageUrl) :
        response = {
            "message" : "Il manque l'url de l'image",
            "code" : 422
        }
        return response

    if(len(name) > 20) :
        response = {
            "message" : "Le nom de l'animal est trop grand",
            "code" : 403
        }
        return response

    if(len(description) > 200) :
        response = {
            "message" : "La description de l'animal est trop grande",
            "code" : 403
        }
        return response

    # On vérifie que l'idName existe
    checkUser = utilisateurModel.getUtilisateurById(idName)

    if(checkUser["code"] == 404) :
        # L'utilisateur n'existe pas
        response = {
            "message" : "L'utilisateur n'existe pas",
            "code" : 422
        }
        return response

    # On vérifie que l'idEspece existe
    checkEspece = especeModel.getEspeceById(idEspece)

    if(checkEspece["code"] == 404) :
        # L'espece n'existe pas
        response = {
            "message" : "L'espèce n'existe pas",
            "code" : 422
        }
        return response

    # On créé la fiche animal
    fiche_animalModel.create(name, description, idName, idEspece, imageUrl)
    
    # On renvoie une réponse
    response = {
        "message" : "La fiche animal a été correctement ajouté",
        "code" : 200
    }
    
    return response

def getFiche_animalAll() :
    # On récupère la fiche animal
    response = fiche_animalModel.getAll()

    for fiche_animal in response["fiches_animal"] :
        # On récupère les commentaires de l'animal
        idAnimal = fiche_animal["animal"]["idAnimal"]
        getComms = commentaireModel.getByAnimal(idAnimal)
        fiche_animal["commentaires"] = getComms["commentaires"]

        # On récupère la note moyenne
        idAnimal = fiche_animal["animal"]["idAnimal"]
        getAVGNote = noteModel.getAvgNoteAnimal(idAnimal)
        if(getAVGNote["code"] == 200) :
            fiche_animal["moyenne-note"] = getAVGNote["note"]["moyenne-note"]

    # On renvoie les informations de la fiche animal
    return response

def getFiche_animalById(idAnimal) :
    # On vérifie qu'on a bien un identifiant
    if(not idAnimal) :
        response = {
            "message" : "Il manque l'identifiant",
            "code" : 422
        }
        return response

    # On récupère la fiche animal
    response = fiche_animalModel.getById(idAnimal)

    # On renvoie les informations de la fiche animal
    return response

def getFiche_animalByEspece(idEspece) :
    # On vérifie qu'on a bien un identifiant
    if(not idEspece) :
        response = {
            "message" : "Il manque l'identifiant",
            "code" : 422
        }
        return response
        
    # On vérifie que l'idEspece existe
    checkEspece = especeModel.getEspeceById(idEspece)

    if(checkEspece["code"] == 404) :
        # L'espece n'existe pas
        response = {
            "message" : "L'espèce n'existe pas",
            "code" : 422
        }
        return response

    # On récupère la fiche animal
    response = fiche_animalModel.getByEspece(idEspece)

    # On renvoie les informations de la fiche animal
    return response

def updateFiche_animal(idAnimal, name, description, idName, idEspece, imageUrl) :
    # On vérifie que c'est bien formaté
    name = name.strip()
    idName = idName.strip()

    if(not idAnimal) :
        response = {
            "message" : "Il manque l'identifiant de l'animal",
            "code" : 422
        }
        return response

    if(not name) :
        response = {
            "message" : "Il manque le nom de l'animal",
            "code" : 422
        }
        return response

    if(not description) :
        response = {
            "message" : "Il manque la description de l'animal",
            "code" : 422
        }
        return response

    if(not idName) :
        response = {
            "message" : "Il manque l'identifiant de l'utilisateur",
            "code" : 422
        }
        return response

    if(not idEspece) :
        response = {
            "message" : "Il manque l'identifiant de l'espèce",
            "code" : 422
        }
        return response
    
    if(not imageUrl) :
        response = {
            "message" : "Il manque l'url de l'image",
            "code" : 422
        }
        return response

    if(len(name) > 20) :
        response = {
            "message" : "Le nom est trop grand",
            "code" : 403
        }
        return response

    if(len(description) > 200) :
        response = {
            "message" : "La description de l'animal est trop grande",
            "code" : 403
        }
        return response

    # On vérifie que l'idAnimal existe
    checkAnimal = fiche_animalModel.getById(idAnimal)

    if(checkAnimal["code"] == 404) :
        # L'utilisateur n'existe pas
        response = {
            "message" : "L'animal n'existe pas",
            "code" : 404
        }
        return response

    # On vérifie que l'idName existe
    checkUser = utilisateurModel.getUtilisateurById(idName)

    if(checkUser["code"] == 404) :
        # L'utilisateur n'existe pas
        response = {
            "message" : "L'utilisateur n'existe pas",
            "code" : 404
        }
        return response

    # On vérifie que l'idEspece existe
    checkEspece = especeModel.getEspeceById(idEspece)

    if(checkEspece["code"] == 404) :
        # L'espece n'existe pas
        response = {
            "message" : "L'espèce n'existe pas",
            "code" : 404
        }
        return response

    # On modifie la fiche animal
    fiche_animalModel.update(idAnimal, name, description, idName, idEspece, imageUrl)
    response = {
        "message" : "Fiche animal correctement modifié",
        "code" : 200
    }

    # On renvoie une réponse
    return response

def deleteFiche_animal(idAnimal) :
    # On vérifie qu'on a bien un identifiant
    if(not idAnimal) :
        response = {
            "message" : "Il manque l'identifiant de l'animal",
            "code" : 422
        }
        return response

    # On vérifie que la fiche de l'animal existe
    check = fiche_animalModel.getById(idAnimal)

    if(check["code"] == 404) :
        response = {
            "message" : "La fiche animal n'existe pas",
            "code" : 404
        }

    else :
        # On supprime un utilisateur
        response = fiche_animalModel.delete(idAnimal)

    # On renvoie une réponse
    return response
