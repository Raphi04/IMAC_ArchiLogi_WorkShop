from flask import Flask,request,render_template,jsonify,abort
from flask_cors import CORS

import services.utilisateur as userService
import services.fiche_animal as fiche_animalService
import services.espece as especeService
import services.commentaire as commentaireService
import services.activite as activiteService

app = Flask(__name__)
CORS(app)

@app.route("/utilisateur", methods=["POST", "GET", "PUT", "DELETE"])
def utilisateur():
    json = request.get_json()

    if(request.method == "POST") :
        response = userService.createUtilisateur(json["idName"], json["username"], json["pwd"])
        return response

    if(request.method == "GET") :
        response = userService.getUtilisateur(json["idName"])
        return response
    
    if(request.method == "PUT") :
        response = userService.updateUtilisateur(json["previousIdName"], json["idName"], json["username"], json["pwd"])
        return response

    if(request.method == "DELETE") :
        response = userService.deleteUtilisateur(json["idName"])
        return response

@app.route("/fiche_animal", methods=["POST", "GET", "PUT", "DELETE"])
def fiche_animal():
    json = request.get_json()

    if(request.method == "POST") :
        response = fiche_animalService.createFiche_animal(json["name"], json["idName"], json["idEspece"])
        return response

    if(request.method == "GET") :
        response = fiche_animalService.getFiche_animal(json["idAnimal"])
        return response
    
    if(request.method == "PUT") :
        response = fiche_animalService.updateFiche_animal(json["idAnimal"], json["name"], json["idName"], json["idEspece"])
        return response

    if(request.method == "DELETE") :
        response = fiche_animalService.deleteFiche_animal(json["idAnimal"])
        return response

    
@app.route("/espece", methods=["POST", "GET", "PUT", "DELETE"])
def espece():
    json = request.get_json()

    if(request.method == "POST") :
        response = especeService.createEspece(json["name"])
        return response

    if(request.method == "GET") :
        response = especeService.getEspece(json["idEspece"])
        return response
    
    if(request.method == "PUT") :
        response = especeService.updateEspece(json["idEspece"], json["name"])
        return response

    if(request.method == "DELETE") :
        response = especeService.deleteEspece(json["idEspece"])
        return response

@app.route("/commentaire", methods=["POST", "GET", "PUT", "DELETE"])
def commentaire():
    json = request.get_json()

    if(request.method == "POST") :
        response = commentaireService.createCommentaire(json["idName"], json["idAnimal"], json["commentaire"])
        return response

    if(request.method == "GET") :
        response = commentaireService.getCommentaire(json["idName"], json["idAnimal"])
        return response
    
    if(request.method == "PUT") :
        response = commentaireService.updateCommentaire(json["idName"], json["idAnimal"], json["commentaire"])
        return response

    if(request.method == "DELETE") :
        response = commentaireService.deleteCommentaire(json["idName"], json["idAnimal"])
        return response
    
@app.route("/activite", methods=["POST", "GET", "PUT", "DELETE"])
def activite():
    json = request.get_json()

    if(request.method == "POST") :
        response = activiteService.createActivite(json["name"])
        return response

    if(request.method == "GET") :
        response = activiteService.getActivite(json["idActivite"])
        return response
    
    if(request.method == "PUT") :
        response = activiteService.updateActivite(json["idActivite"], json["name"])
        return response

    if(request.method == "DELETE") :
        response = activiteService.deleteActivite(json["idActivite"])
        return response