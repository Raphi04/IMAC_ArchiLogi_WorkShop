from flask import jsonify

import models.activite as activiteModel
import models.fiche_animal as fiche_animalModel
import services.fiche_animal as fiche_animalService

def createActivite(name) :
    name = name.strip()

    # On vérifie que c'est correctement formater

    if(not name) :
        response = {
            "message" : "Il manque le nom",
            "code" : 422
        }
        return response
    
    if(len(name) > 20) :
        response = {
            "message" : "Le nom est trop grand",
            "code" : 403
        }
        return response
    
    # On créé l'activité
    activiteModel.create(name)

    # On renvoie une réponse
    response = {
        "message" : "L'activité a été correctement ajouté",
        "code" : 200
    }

    return response

def getAllActivite() :
    # On récupère les activités
    response = activiteModel.getAllActivite()

    # On renvoie les informations des activités
    return response

def activiteGetEspece(idActivite) :
    # On vérifie qu'on a bien une activité
    if(not idActivite) :
        response = {
            "message" : "Il manque l'activité",
            "code" : 422
        }
        return response

    # On regarde si l'activité existe
    checkActivite = activiteModel.getActiviteById(idActivite)

    if(checkActivite["code"] == 404) :
        # L'activité n'existe pas
        response = {
            "message" : "L'activité n'existe pas",
            "code" : 422
        }
        return response

    # On récupère les activités
    response = activiteModel.getEspecesByActiviteId(idActivite)

    # On renvoie les informations des activités
    return response

def activiteGetAnimals(date, idActivite) :
    # On vérifie qu'on a bien une activité
    if(not date) :
        response = {
            "message" : "Il manque la date",
            "code" : 422
        }
        return response

    # On vérifie qu'on a bien une activité
    if(not idActivite) :
        response = {
            "message" : "Il manque l'activité",
            "code" : 422
        }
        return response

    # On regarde si l'activité existe
    checkActivite = activiteModel.getActiviteById(idActivite)

    if(checkActivite["code"] == 404) :
        # L'activité n'existe pas
        response = {
            "message" : "L'activité n'existe pas",
            "code" : 422
        }
        return response

    response = {
        "fiches_animal" : [],
        "code" : 200
    }

    # On récupère les idEspeces
    checkIdEspeces = activiteModel.getEspecesByActiviteId(idActivite)

    if(checkIdEspeces["code"] == 200) :
        for idEspece in checkIdEspeces["especes"] :
            animalsList = fiche_animalModel.getByEspece(idEspece["idEspece"])

            if(animalsList["code"] == 200) :
                for animal in animalsList["fiches_animal"] :
                    checkAvailability = fiche_animalService.checkAvailability(animal["animal"]["idAnimal"], date)

                    if(checkAvailability["code"] == 200) :
                        response["fiches_animal"].append(animal)
    else :
        response = {
            "message" : "Aucune espèce n'est lié à cette activité",
            "code" : 404
        }

    # On renvoie les informations des activités
    return response

def getActiviteById(idActivite) :
    # On vérifie qu'on a bien une activité
    if(not idActivite) :
        response = {
            "message" : "Il manque l'activité",
            "code" : 422
        }
        return response

    # On récupère une activité
    response = activiteModel.getActiviteById(idActivite)

    # On renvoie les informations de l'activité
    return response

def updateActivite(idActivite, name) :
    # On vérifie que c'est bien formaté
    name = name.strip()

    if(not idActivite) :
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

    if(len(name) > 20) :
        response = {
            "message" : "L'identifiant est trop grand",
            "code" : 403
        }
        return response
    

    # On regarde si l'activité existe
    checkActivite = activiteModel.getActiviteById(idActivite)

    if(checkActivite["code"] == 404) :
        # L'activité n'existe pas
        response = {
            "message" : "L'espèce n'existe pas",
            "code" : 422
        }
        return response

    # On modifie l'activité
    activiteModel.update(idActivite, name)
    response = {
            "message" : "L'activité a été correctement modifié",
            "code" : 200
        }

    # On renvoie une réponse
    return response

def deleteActivite(idActivite) :
    # On vérifie qu'on a bien un identifiant
    if(not idActivite) :
        response = {
            "message" : "Il manque l'identifiant",
            "code" : 422
        }
        return response

    # On vérifie que l'activité existe
    check = activiteModel.getActiviteById(idActivite)

    if(check["code"] == 404) :
        response = {
            "message" : "L'activité n'existe pas",
            "code" : 404
        }

    else :
        # On supprime une activité
        response = activiteModel.delete(idActivite)

    # On renvoie une réponse
    return response
