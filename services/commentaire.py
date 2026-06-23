from flask import jsonify

import models.commentaire as commentaireModel
import models.fiche_animal as fiche_animalModel
import models.utilisateur as utilisateurModel

def createCommentaire(idName, idAnimal, commentaire) :
    # On vérifie que c'est correctement formater
    commentaire = commentaire.strip()

    if(not commentaire) :
        response = {
            "message" : "Il manque le commentaire",
            "code" : 422
        }
        return response

    if(not idName) :
        response = {
            "message" : "Il manque l'identifiant utilisateur",
            "code" : 422
        }
        return response

    if(not idAnimal) :
        response = {
            "message" : "Il manque l'identifiant de l'animal",
            "code" : 422
        }
        return response

    if(len(commentaire) > 200) :
        response = {
            "message" : "Le commentaire est trop grand",
            "code" : 403
        }
        return response

    # On vérifie que l'idName existe
    checkUser = utilisateurModel.get(idName)

    if(checkUser["code"] == 404) :
        # L'utilisateur n'existe pas
        response = {
            "message" : "L'utilisateur n'existe pas",
            "code" : 422
        }
        return response

    # On vérifie que l'idAnimal existe
    checkFiche_animal = fiche_animalModel.get(idAnimal)

    if(checkFiche_animal["code"] == 404) :
        # La fiche animal n'existe pas
        response = {
            "message" : "La fiche n'existe pas",
            "code" : 422
        }
        return response

    # On créé le commentaire
    commentaireModel.create(idName, idAnimal, commentaire)
    
    # On renvoie une réponse
    response = {
        "message" : "Le commentaire a été correctement ajouté",
        "code" : 200
    }
    
    return response

def getCommentaire(idName, idAnimal) :
    # On vérifie qu'on a bien un identifiant d'utilisateur
    if(not idName) :
        response = {
            "message" : "Il manque l'identifiant de l'utilisateur",
            "code" : 422
        }
        return response

    # On vérifie qu'on a bien un identifiant de fiche animal
    if(not idAnimal) :
        response = {
            "message" : "Il manque l'identifiant de la fiche animal",
            "code" : 422
        }
        return response

    # On récupère la fiche animal
    response = commentaireModel.get(idName, idAnimal)

    # On renvoie les informations de la fiche animal
    return response

def updateCommentaire(idName, idAnimal, commentaire) :
    # On vérifie que c'est bien formaté
    commentaire = commentaire.strip()

    if(not idName) :
        response = {
            "message" : "Il manque l'identifiant de l'utilisateur",
            "code" : 422
        }
        return response

    if(not idAnimal) :
        response = {
            "message" : "Il manque l'identifiant de la fiche de l'animal",
            "code" : 422
        }
        return response

    if(not commentaire) :
        response = {
            "message" : "Il manque le commentaire",
            "code" : 422
        }
        return response
    
    if(len(commentaire) > 200) :
        response = {
            "message" : "Le commentaire est trop grand",
            "code" : 403
        }
        return response

    # On vérifie que l'idName existe
    checkUser = utilisateurModel.get(idName)

    if(checkUser["code"] == 404) :
        # L'utilisateur n'existe pas
        response = {
            "message" : "L'utilisateur n'existe pas",
            "code" : 422
        }
        return response

    # On vérifie que l'idAnimal existe
    checkFiche_animal = fiche_animalModel.get(idAnimal)

    if(checkFiche_animal["code"] == 404) :
        # La fiche animal n'existe pas
        response = {
            "message" : "La fiche animal n'existe pas",
            "code" : 422
        }
        return response

    # On modifie le commentaire
    commentaireModel.update(idName, idAnimal, commentaire)
    response = {
        "message" : "Commentaire correctement modifié",
        "code" : 200
    }

    # On renvoie une réponse
    return response

def deleteCommentaire(idName, idAnimal) :
    # On vérifie qu'on a bien un identifiant de l'utilisateur
    if(not idName) :
        response = {
            "message" : "Il manque l'identifiant de l'utilisateur",
            "code" : 422
        }
        return response

    # On vérifie qu'on a bien un identifiant de la fiche de l'animal
    if(not idAnimal) :
        response = {
            "message" : "Il manque l'identifiant de l'animal",
            "code" : 422
        }
        return response

    # On vérifie que le commentaire existe
    check = commentaireModel.get(idName, idAnimal)

    if(check["code"] == 404) :
        response = {
            "message" : "Le commentaire n'existe pas",
            "code" : 404
        }

    else :
        # On supprime le commentaire
        response = commentaireModel.delete(idName, idAnimal)

    # On renvoie une réponse
    return response
