from flask import Flask,request,render_template,jsonify,abort
from flask_cors import CORS

import services.utilisateur as utilisateurService
import services.fiche_animal as fiche_animalService
import services.espece as especeService
import services.commentaire as commentaireService
import services.activite as activiteService
import services.inclue as inclueService
import services.participe as participeService
import services.note as noteService

app = Flask(__name__)
CORS(app)

@app.route("/utilisateur", methods=["POST", "GET"])
def utilisateur():

    if(request.method == "POST") :
        json = request.get_json()
        response = utilisateurService.createUtilisateur(json["idName"], json["username"], json["pwd"])
        return response

    if(request.method == "GET") :
        response = utilisateurService.getAllUtilisateur()
        return response

@app.route("/utilisateur/<idName>", methods=["GET", "PUT", "DELETE"])
def utilisateurByID(idName):
    if(request.method == "GET") :
        response = utilisateurService.getUtilisateurById(idName)
        return response

    if(request.method == "PUT") :
        json = request.get_json()
        response = utilisateurService.updateUtilisateur(idName, json["newidName"], json["username"], json["pwd"])
        return response

    if(request.method == "DELETE") :
        response = utilisateurService.deleteUtilisateur(idName)
        return response

@app.route("/utilisateur/connect", methods=["GET"])
def utilisateurConnect():
    json = request.get_json()
    response = utilisateurService.connectUtilisateur(json["idName"], json["pwd"])
    return response

@app.route("/fiche_animal", methods=["POST", "GET"])
def fiche_animal():

    if(request.method == "POST") :
        json = request.get_json()
        response = fiche_animalService.createFiche_animal(json["name"], json["description"], json["idName"], json["idEspece"], json["imageUrl"])
        return response

    if(request.method == "GET") :
        response = fiche_animalService.getFiche_animalAll()
        return response

@app.route("/fiche_animal/<idAnimal>", methods=["GET", "PUT", "DELETE"])
def fiche_animalById(idAnimal):
    if(request.method == "GET") :
        response = fiche_animalService.getFiche_animalById(idAnimal)
        return response
    
    if(request.method == "PUT") :
        json = request.get_json()
        response = fiche_animalService.updateFiche_animal(idAnimal, json["name"], json["description"], json["idName"], json["idEspece"], json["imageUrl"])
        return response

    if(request.method == "DELETE") :
        response = fiche_animalService.deleteFiche_animal(idAnimal)
        return response

    
@app.route("/espece", methods=["POST", "GET"])
def espece():
    if(request.method == "POST") :
        json = request.get_json()
        response = especeService.createEspece(json["name"])
        return response

    if(request.method == "GET") :
        response = especeService.getAllEspece()
        return response

@app.route("/espece/<idEspece>", methods=["GET", "PUT", "DELETE"])
def especeById(idEspece):
    if(request.method == "GET") :
        response = especeService.getEspeceById(idEspece)
        return response

    if(request.method == "PUT") :
        json = request.get_json()
        response = especeService.updateEspece(idEspece, json["name"])
        return response

    if(request.method == "DELETE") :
        json = request.get_json()
        response = especeService.deleteEspece(idEspece)
        return response

@app.route("/commentaire", methods=["POST", "GET", "PUT", "DELETE"])
def commentaire():
    json = request.get_json()

    if(request.method == "POST") :
        response = commentaireService.createCommentaire(json["idName"], json["idAnimal"], json["commentaire"])
        return response

    if(request.method == "GET") :
        response = commentaireService.getCommentaire(json["idCommentaire"])
        return response
    
    if(request.method == "PUT") :
        response = commentaireService.updateCommentaire(json["idCommentaire"], json["commentaire"])
        return response

    if(request.method == "DELETE") :
        response = commentaireService.deleteCommentaire(json["idCommentaire"])
        return response
    
@app.route("/activite", methods=["POST", "GET"])
def activite():
    if(request.method == "POST") :
        json = request.get_json()
        response = activiteService.createActivite(json["name"])
        return response

    if(request.method == "GET") :
        response = activiteService.getAllActivite()
        return response

@app.route("/activite/<idActivite>", methods=["GET", "PUT", "DELETE"])
def activiteById(idActivite):
    if(request.method == "GET") :
        response = activiteService.getActiviteById(idActivite)
        return response

    if(request.method == "PUT") :
        json = request.get_json()
        response = activiteService.updateActivite(idActivite, json["name"])
        return response

    if(request.method == "DELETE") :
        response = activiteService.deleteActivite(idActivite)
        return response

@app.route("/inclue", methods=["POST", "GET", "PUT", "DELETE"])
def inclue():
    json = request.get_json()

    if(request.method == "POST") :
        response = inclueService.createInclue(json["idEspece"],json["idActivite"])
        return response

    if(request.method == "GET") :
        response = inclueService.getInclue(json["idInclue"])
        return response
    
    if(request.method == "PUT") :
        response = inclueService.updateInclue(json["idInclue"], json["idEspece"], json["idActivite"])
        return response

    if(request.method == "DELETE") :
        response = inclueService.deleteInclue(json["idInclue"])
        return response

@app.route("/participe", methods=["POST", "GET", "PUT", "DELETE"])
def participe():
    json = request.get_json()

    if(request.method == "POST") :
        response = participeService.createParticipe(json["idName"], json["idAnimal"], json["idActivite"], json["date"])
        return response

    if(request.method == "GET") :
        response = participeService.getParticipe(json["idParticipe"])
        return response
    
    if(request.method == "PUT") :
        response = participeService.updateParticipe(json["idParticipe"], json["idName"], json["idAnimal"], json["idActivite"], json["date"])
        return response

    if(request.method == "DELETE") :
        response = participeService.deleteParticipe(json["idParticipe"])
        return response
    
@app.route("/note", methods=["POST", "GET"])
def note():
    if(request.method == "POST") :
        json = request.get_json()
        response = noteService.createNote(json["idName"],json["idAnimal"],json["note"])
        return response

    if(request.method == "GET") :
        response = noteService.getNoteAll()
        return response

@app.route("/note/<idNote>", methods=["GET", "PUT", "DELETE"])
def noteById(idNote):
    if(request.method == "GET") :
        response = noteService.getNoteById(idNote)
        return response
    if(request.method == "PUT") :
        json = request.get_json()
        response = noteService.updateNote(idNote,json["idName"],json["idAnimal"],json["note"])
        return response

    if(request.method == "DELETE") :
        response = noteService.deleteNote(idNote)
        return response

@app.route("/note/animal/<idAnimal>", methods=["GET"])
def noteByAnimal(idAnimal):
    response = noteService.getAvgNoteAnimal(idAnimal)
    return response

@app.route("/note/<idName>/<idNote>", methods=["PUT"])
def noteByUser(idName, idNote):
        json = request.get_json()
        response = noteService.updateNoteByUser(idName, idNote, json["note"])
        return response

@app.route("/note/utilisateur/<idName>", methods=["GET"])
def noteUtilisateurById(idName):
    response = noteService.getNoteUtilisateurById(idName)
    return response