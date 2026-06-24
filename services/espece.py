from flask import jsonify

import models.espece as especeModel

def createEspece(name) :
    name = name.strip()

    # On vérifie que c'est correctement formater

    if(not name) :
        response = {
            "message" : "Il manque le nom",
            "code" : 422
        }
        return response
    
    if(len(name) > 50) :
        response = {
            "message" : "Le nom est trop grand",
            "code" : 403
        }
        return response
    
    # On créé l'espèce
    especeModel.create(name)

    # On renvoie une réponse
    response = {
        "message" : "L'espèce a été correctement ajouté",
        "code" : 200
    }

    return response

def getAllEspece() :

    # On récupère une espèce
    response = especeModel.getAllEspece()

    # On renvoie les informations de l'espèce
    return response

def getEspeceById(idEspece) :
    # On vérifie que c'est correctement formater
    if(not idEspece) :
        response = {
            "message" : "Il manque l'identifiant de l'espèce",
            "code" : 422
        }
        return response

    # On récupère une note
    response = especeModel.getEspeceById(idEspece)

    # On renvoie les informations de l'activité
    return response

def updateEspece(idEspece, name) :
    # On vérifie que c'est bien formaté
    name = name.strip()

    if(not idEspece) :
        response = {
            "message" : "Il manque l'identifiant",
            "code" : 422
        }
        return response

    if(not name) :
        response = {
            "message" : "Il manque le nom",
            "code" : 422
        }
        return response

    if(len(name) > 50) :
        response = {
            "message" : "L'identifiant est trop grand",
            "code" : 403
        }
        return response

    # On vérifie si l'espèce existe
    checkEspece = especeModel.getEspeceById(idEspece)

    if(checkEspece["code"] == 404) :
        # L'espèce n'existe pas
        response = {
            "message" : "L'espèce n'existe pas",
            "code" : 422
        }
        return response

    # On modifie l'espèce
    especeModel.update(idEspece, name)
    response = {
            "message" : "L'espèce a été correctement modifié",
            "code" : 200
        }

    # On renvoie une réponse
    return response

def deleteEspece(idEspece) :
    # On vérifie qu'on a bien un identifiant
    if(not idEspece) :
        response = {
            "message" : "Il manque l'identifiant",
            "code" : 422
        }
        return response

    # On vérifie que l'espèce existe
    check = especeModel.getEspeceById(idEspece)

    if(check["code"] == 404) :
        response = {
            "message" : "L'espèce n'existe pas",
            "code" : 404
        }

    else :
        # On supprime une espèce
        response = especeModel.delete(idEspece)

    # On renvoie une réponse
    return response
