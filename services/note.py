from flask import jsonify

import models.note as noteModel
import models.utilisateur as utilisateurModel
import models.fiche_animal as fiche_animalModel

def createNote(idName, idAnimal,note) :

    # On vérifie que c'est correctement formater
    if(not idName) :
        response = {
            "message" : "Il manque l'identifiant de l'utilisateur",
            "code" : 422
        }
        return response
    
    if(not idAnimal) :
        response = {
            "message" : "Il manque l'identifiant de l'animal",
            "code" : 422
        }
        return response
    
    if(not note) :
        response = {
            "message" : "Il manque la note",
            "code" : 422
        }
        return response
    
    if(note > 5 or note < 1):
        response = {
            "message" : "Note en dehors du scope",
            "code" : 403
        }
        return response

    # On vérifie que l'idName existe
    checkName = utilisateurModel.getUtilisateurById(idName)

    if(checkName["code"] == 404) :
        # L'utilisateur n'existe pas
        response = {
            "message" : "L'espèce n'existe pas",
            "code" : 404
        }
        return response
    
    # On vérifie que l'idAnimal existe
    checkAnimal = fiche_animalModel.getById(idAnimal)

    if(checkAnimal["code"] == 404) :
        # L'utilisateur n'existe pas
        response = {
            "message" : "L'espèce n'existe pas",
            "code" : 404
        }
        return response
    
    # On vérifie que la note n'est pas en doublon
    checkNote = noteModel.getNoteByName(idName, idAnimal)

    if(checkNote["code"] == 200) :
        # La note existe déjà
        response = {
            "message" : "La note existe déjà",
            "code" : 403
        }
        return response
    
    # On créé la note
    noteModel.create(idName, idAnimal,note)

    # On renvoie une réponse
    response = {
        "message" : "La note a été correctement ajouté",
        "code" : 200
    }

    return response

def getNoteAll() :
    # On récupère une note
    response = noteModel.getAll()

    # On renvoie les informations des notes
    return response

def getNoteById(idNote) :
    # On vérifie que c'est correctement formater
    if(not idNote) :
        response = {
            "message" : "Il manque l'identifiant de l'utilisateur",
            "code" : 422
        }
        return response

    # On récupère une note
    response = noteModel.getNoteById(idNote)

    # On renvoie les informations de l'activité
    return response

def getNoteUtilisateurById(idName):
     # On récupère une note
    response = noteModel.getAllFromUtilisateur(idName)

    # On renvoie les informations de l'activité
    return response

def getAvgNoteAnimal(idAnimal):
    # On vérifie que c'est correctement formater
    if(not idAnimal) :
        response = {
            "message" : "Il manque l'identifiant de l'animal",
            "code" : 422
        }
        return response

    # On récupère une note
    response = noteModel.getAvgNoteAnimal(idAnimal)

    # On renvoie les informations de l'activité
    return response

def updateNote(idNote, idName, idAnimal,note) :
    # On vérifie que c'est bien formaté

    if(not idNote) :
        response = {
            "message" : "Il manque l'identifiant de la note",
            "code" : 422
        }
        return response
        # On vérifie que c'est correctement formater
    if(not idName) :
        response = {
            "message" : "Il manque l'identifiant de l'utilisateur",
            "code" : 422
        }
        return response
    
    if(not idAnimal) :
        response = {
            "message" : "Il manque l'identifiant de l'animal",
            "code" : 422
        }
        return response
    
    if(not note) :
        response = {
            "message" : "Il manque la note",
            "code" : 422
        }
        return response
    
    if(note > 5 or note < 1):
        response = {
            "message" : "Note en dehors du scope",
            "code" : 403
        }
        return response
    
    # On vérifie que l'idName existe
    checkName = utilisateurModel.getUtilisateurById(idName)

    if(checkName["code"] == 404) :
        # L'utilisateur n'existe pas
        response = {
            "message" : "L'espèce n'existe pas",
            "code" : 404
        }
        return response
    
    # On vérifie que l'idAnimal existe
    checkAnimal = fiche_animalModel.getById(idAnimal)

    if(checkAnimal["code"] == 404) :
        # L'utilisateur n'existe pas
        response = {
            "message" : "L'espèce n'existe pas",
            "code" : 404
        }
        return response

    # On modifie la note
    noteModel.update(idNote, idName, idAnimal,note)
    response = {
            "message" : "La note a été correctement modifié",
            "code" : 200
        }

    # On renvoie une réponse
    return response

def updateNoteByUser(idName, idNote, note) :
    if(not idName) :
        response = {
            "message" : "Il manque l'identifiant de l'utilisateur",
            "code" : 422
        }
        return response

    if(not idNote) :
        response = {
            "message" : "Il manque l'identifiant de la note",
            "code" : 422
        }
        return response

    if(not note) :
        response = {
            "message" : "Il manque la note",
            "code" : 422
        }
        return response
    
    if(note > 5 or note < 1):
        response = {
            "message" : "Note en dehors du scope",
            "code" : 403
        }
        return response
    
    # On vérifie que l'idName existe
    checkName = utilisateurModel.getUtilisateurById(idName)

    if(checkName["code"] == 404) :
        # L'utilisateur n'existe pas
        response = {
            "message" : "L'espèce n'existe pas",
            "code" : 404
        }
        return response
    
    # On vérifie que l'idNote existe
    checkNote = noteModel.getNoteById(idNote)

    if(checkNote["code"] == 404) :
        # La note n'existe pas
        response = {
            "message" : "La note n'existe pas",
            "code" : 404
        }
        return response

    # On modifie la note
    noteModel.updateNoteByUser(idName, idNote, note)
    response = {
            "message" : "La note a été correctement modifié",
            "code" : 200
        }

    # On renvoie une réponse
    return response


def deleteNote(idNote) :
    # On vérifie qu'on a bien un identifiant
    if(not idNote) :
        response = {
            "message" : "Il manque l'identifiant",
            "code" : 422
        }
        return response

    # On vérifie que la note existe
    check = noteModel.getNoteById(idNote)

    if(check["code"] == 404) :
        response = {
            "message" : "La note n'existe pas",
            "code" : 404
        }

    else :
        # On supprime la note
        response = noteModel.delete(idNote)

    # On renvoie une réponse
    return response