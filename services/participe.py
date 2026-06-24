from flask import jsonify

from datetime import datetime

import models.utilisateur as utilisateurModel
import models.fiche_animal as fiche_animalModel
import models.activite as activiteModel
import models.participe as participeModel

def createParticipe(idName, idAnimal, idActivite, date) :
    if(not idName) :
        response = {
            "message" : "Il manque l'identifiant utilisateur",
            "code" : 422
        }
        return response

    if(not idAnimal) :
        response = {
            "message" : "Il manque l'identifiant de la fiche animal",
            "code" : 422
        }
        return response

    if(not idActivite) :
        response = {
            "message" : "Il manque l'identifiant de l'activite",
            "code" : 422
        }
        return response

    if(not date) :
        response = {
            "message" : "Il manque la date",
            "code" : 422
        }
        return response

    enteredDate = datetime.strptime(date, "%Y-%m-%d")
    dateNow = datetime.now().strftime("%Y-%m-%d")

    if(enteredDate < datetime.strptime(dateNow, "%Y-%m-%d")) :
        response = {
            "message" : "Veuillez selectionner une date supérieur ou égale à celle actuelle",
            "code" : 403
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

    # On vérifie que l'idAnimal existe
    checkAnimal = fiche_animalModel.getById(idAnimal)

    if(checkAnimal["code"] == 404) :
        # La fiche animal n'existe pas
        response = {
            "message" : "La fiche animal n'existe pas",
            "code" : 404
        }
        return response

    # On vérifie que l'idActivite existe
    checkActivite = activiteModel.getActiviteById(idActivite)

    if(checkActivite["code"] == 404) :
        # L'activité n'existe pas
        response = {
            "message" : "L'activité n'existe pas",
            "code" : 404
        }
        return response

    # On vérifie que l'animal à le droit de participer
    idEspece = fiche_animalModel.getById(idAnimal)["fiche_animal"]["espece"]["idEspece"]

    especesParticipante = activiteModel.getEspecesByActiviteId(idActivite)["especes"]

    for especeParticipante in especesParticipante :
        if(idEspece == especeParticipante["idEspece"]):
            # On créé la fiche animal
            participeModel.create(idName, idAnimal, idActivite, date)
            
            # On renvoie une réponse
            response = {
                "message" : "La participation a été correctement ajouté",
                "code" : 200
            }
            
            return response
    
    # L'animal ne peut pas participer
    response = {
        "message" : "L'animal ne peut pas participer",
        "code" : 200
    }
    
    return response



def getParticipe(idParticipe) :
    # On vérifie qu'on a bien un identifiant
    if(not idParticipe) :
        response = {
            "message" : "Il manque l'identifiant",
            "code" : 422
        }
        return response

    # On récupère la fiche animal
    response = participeModel.get(idParticipe)

    # On renvoie les informations de la fiche animal
    return response

def updateParticipe(idParticipe, idName, idAnimal, idActivite, date) :

    if(not idParticipe) :
        response = {
            "message" : "Il manque l'identifiant de participation",
            "code" : 422
        }
        return response

    if(not idName) :
        response = {
            "message" : "Il manque l'identifiant d'utilisateur",
            "code" : 422
        }
        return response

    if(not idAnimal) :
        response = {
            "message" : "Il manque l'identifiant de l'animal",
            "code" : 422
        }
        return response

    if(not idActivite) :
        response = {
            "message" : "Il manque l'identifiant de l'activité",
            "code" : 422
        }
        return response

    if(not date) :
        response = {
            "message" : "Il manque la date",
            "code" : 422
        }
        return response

    # On vérifie que l'idParticipe existe
    checkParticipe = participeModel.get(idParticipe)

    if(checkParticipe["code"] == 404) :
        # La participation n'existe pas
        response = {
            "message" : "La participation n'existe pas",
            "code" : 422
        }
        return response

    # On vérifie que l'idName existe
    checkName = utilisateurModel.getUtilisateurById(idName)

    if(checkName["code"] == 404) :
        # L'utilisateur n'existe pas
        response = {
            "message" : "L'utilisateur n'existe pas",
            "code" : 422
        }
        return response

    # On vérifie que l'idAnimal existe
    checkAnimal = fiche_animalModel.getById(idAnimal)

    if(checkAnimal["code"] == 404) :
        # La fiche de l'animal n'existe pas
        response = {
            "message" : "L'animal n'existe pas",
            "code" : 422
        }
        return response

    # On vérifie que l'idActivite existe
    checkActivite = activiteModel.getActiviteById(idActivite)

    if(checkActivite["code"] == 404) :
        # L'activité n'existe pas
        response = {
            "message" : "L'activité n'existe pas",
            "code" : 422
        }
        return response

    enteredDate = datetime.strptime(date, "%Y-%m-%d")
    dateNow = datetime.now().strftime("%Y-%m-%d")

    if(enteredDate < datetime.strptime(dateNow, "%Y-%m-%d")) :
        response = {
            "message" : "Veuillez selectionner une date supérieur ou égale à celle actuelle",
            "code" : 403
        }
        return response

    print(date)

    # On modifie la participation
    participeModel.update(idParticipe, idName, idAnimal, idActivite, date)
    response = {
        "message" : "Participation correctement modifié",
        "code" : 200
    }

    # On renvoie une réponse
    return response

def deleteParticipe(idParticipe) :
    # On vérifie qu'on a bien un identifiant
    if(not idParticipe) :
        response = {
            "message" : "Il manque l'identifiant",
            "code" : 422
        }
        return response

    # On vérifie que la participation existe
    check = participeModel.get(idParticipe)

    if(check["code"] == 404) :
        response = {
            "message" : "La participation n'existe pas",
            "code" : 404
        }

    else :
        # On supprime la participation
        response = participeModel.delete(idParticipe)

    # On renvoie une réponse
    return response
