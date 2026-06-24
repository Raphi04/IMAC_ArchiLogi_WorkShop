from flask import jsonify

import models.inclue as inclueModel
import models.espece as especeModel
import models.activite as activiteModel

def createInclue(idEspece, idActivite) :

    # On vérifie que c'est correctement formater

    if(not idEspece) :
        response = {
            "message" : "Il manque l'identifiant de l'espèce",
            "code" : 422
        }
        return response
    
    if(not idActivite) :
        response = {
            "message" : "Il manque l'identifiant de l'activité",
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
    
    # On vérifie que l'idActivite existe
    checkActivite = activiteModel.getActiviteById(idActivite)

    if(checkActivite["code"] == 404) :
        # L'activite n'existe pas
        response = {
            "message" : "L'activité n'existe pas",
            "code" : 422
        }
        return response

    # On créé l'inclusion
    inclueModel.create(idEspece,idActivite)

    # On renvoie une réponse
    response = {
        "message" : "L'inclusion a été correctement ajouté",
        "code" : 200
    }

    return response

def getInclue(idInclue) :
    # On vérifie qu'on a bien une activité
    if(not idInclue) :
        response = {
            "message" : "Identifiant non reconnu",
            "code" : 422
        }
        return response

    # On récupère une activité
    response = inclueModel.get(idInclue)

    # On renvoie les informations de l'activité
    return response

def updateInclue(idInclue,idEspece,idActivite) :
    # On vérifie que c'est bien formaté

    if(not idInclue) :
        response = {
            "message" : "Il manque l'identifiant d'inclusion",
            "code" : 422
        }
        return response
    
    if(not idEspece) :
        response = {
            "message" : "Il manque l'identifiant de l'espèce",
            "code" : 422
        }
        return response
    
    if(not idActivite) :
        response = {
            "message" : "Il manque l'identifiant de l'activité",
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
    # On vérifie que l'idActivite existe
    checkActivite = activiteModel.get(idActivite)

    if(checkActivite["code"] == 404) :
        # L'activite n'existe pas
        response = {
            "message" : "L'activité n'existe pas",
            "code" : 422
        }
        return response

    # On modifie l'inclusion
    inclueModel.update(idInclue,idEspece,idActivite)
    response = {
            "message" : "L'inclusion a été correctement modifié",
            "code" : 200
        }

    # On renvoie une réponse
    return response

def deleteInclue(idInclue) :
    # On vérifie qu'on a bien un identifiant
    if(not idInclue) :
        response = {
            "message" : "Il manque l'identifiant",
            "code" : 422
        }
        return response

    # On vérifie que l'inclusion existe
    check = inclueModel.get(idInclue)

    if(check["code"] == 404) :
        response = {
            "message" : "L'inclusion n'existe pas",
            "code" : 404
        }

    else :
        # On supprime une inclusion
        response = inclueModel.delete(idInclue)

    # On renvoie une réponse
    return response
