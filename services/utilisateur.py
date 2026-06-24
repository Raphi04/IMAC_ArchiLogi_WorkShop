from flask import jsonify

import models.utilisateur as utilisateurModel

def createUtilisateur(idName, username, pwd) :
    # On vérifie que c'est correctement formater
    idName = idName.strip()
    username = username.strip()
    pwd = pwd.strip()

    if(not idName) :
        response = {
            "message" : "Il manque l'identifiant",
            "code" : 422
        }
        return response

    if(not username) :
        response = {
            "message" : "Il manque le nom",
            "code" : 422
        }
        return response

    if(not pwd) :
        response = {
            "message" : "Il manque le mot de passe",
            "code" : 422
        }
        return response

    if(len(idName) > 20) :
        response = {
            "message" : "L'identifiant est trop grand",
            "code" : 403
        }
        return response
    
    if(len(username) > 20) :
        response = {
            "message" : "Le nom est trop grand",
            "code" : 403
        }
        return response

    if(len(pwd) > 50) :
        response = {
            "message" : "Le mot de passe est trop grand",
            "code" : 403
        }
        return response

    # On créé l'utilisateur

    utilisateurModel.create(idName, username, pwd)
    
    # On renvoie une réponse
    response = {
        "message" : "Utilisateur correctement ajouté",
        "code" : 200
    }
    
    return response

def getAllUtilisateur() :

    # On récupère tous les utilisateurs
    response = utilisateurModel.getAllUtilisateur()

    # On renvoie les informations de l'utilisateur
    return response

def getUtilisateurById(idName) :
    # On vérifie que c'est correctement formater
    if(not idName) :
        response = {
            "message" : "Il manque l'identifiant de l'utilisateur",
            "code" : 422
        }
        return response

    # On récupère une note
    response = utilisateurModel.getUtilisateurById(idName)

    # On renvoie les informations de l'activité
    return response


def updateUtilisateur(previousIdName, newidName, username, pwd) :
    # On vérifie que c'est bien formaté
    newidName = newidName.strip()
    username = username.strip()
    pwd = pwd.strip()

    if(not newidName) :
        response = {
            "message" : "Il manque l'identifiant",
            "code" : 422
        }
        return response

    if(not username) :
        response = {
            "message" : "Il manque le nom",
            "code" : 422
        }
        return response

    if(not pwd) :
        response = {
            "message" : "Il manque le mot de passe",
            "code" : 422
        }
        return response

    if(len(newidName) > 20) :
        response = {
            "message" : "L'identifiant est trop grand",
            "code" : 403
        }
        return response
    
    if(len(username) > 20) :
        response = {
            "message" : "Le nom est trop grand",
            "code" : 403
        }
        return response

    if(len(pwd) > 50) :
        response = {
            "message" : "Le mot de passe est trop grand",
            "code" : 403
        }
        return response

    # On vérifie que l'idName n'est pas déjà pris
    if(previousIdName != newidName) :
        check = utilisateurModel.getUtilisateurById(newidName)

        if(check["code"] == 404) :

            # On modifie l'utilisateur
            utilisateurModel.update(previousIdName, newidName, username, pwd)
            response = {
                "message" : "Utilisateur correctement modifié",
                "code" : 200
            }

        else :
            response = {
                "message" : "Identifiant déjà utilisé",
                "code" : 403
            }

    else : 
        # On modifie l'utilisateur
        utilisateurModel.update(previousIdName, newidName, username, pwd)
        response = {
            "message" : "Utilisateur correctement modifié",
            "code" : 200
        }

    # On renvoie une réponse
    return response

def deleteUtilisateur(idName) :
    # On vérifie qu'on a bien un identifiant
    if(not idName) :
        response = {
            "message" : "Il manque l'identifiant",
            "code" : 422
        }
        return response

    # On vérifie que l'utilisateur existe
    check = utilisateurModel.getUtilisateurById(idName)

    if(check["code"] == 404) :
        response = {
            "message" : "Utilisateur n'existe pas",
            "code" : 404
        }

    else :
        # On supprime un utilisateur
        response = utilisateurModel.delete(idName)

    # On renvoie une réponse
    return response

def connectUtilisateur(idName, pwd) :
    # On vérifie qu'on a bien un identifiant
    if(not idName) :
        response = {
            "message" : "Il manque l'identifiant",
            "code" : 422
        }
        return response

    # On vérifie qu'on a bien un mot de passe
    if(not pwd) :
        response = {
            "message" : "Il manque le mot de passe",
            "code" : 422
        }
        return response

    # On teste si l'identifiant existe
    checkName = utilisateurModel.get(idName)

    if(checkName["code"] == 404) :
        # L'utilisateur n'existe pas
        response = {
            "message" : "L'utilisateur n'existe pas",
            "code" : 404
        }
        return response

    # On teste le mot de passe
    response = utilisateurModel.connectUtilisateur(idName, pwd)

    return response
