from database import connectToDB

def create(idName, idAnimal, idActivite, date) :
    # Connexion à la BDD
    myDb = connectToDB()
    myCursor = myDb.cursor()

    # Créer la participation
    sql = f'''
        INSERT INTO participe VALUES 
        (
            NULL,
            "{idName}",
            {idAnimal},
            {idActivite},
            "{date}"
        )
    '''
    myCursor.execute(sql)
    myDb.commit()

    # Fermeture de la connexion
    myCursor.close()
    myDb.close()

def getParticipeAll():
    # Connexion à la BDD
    myDb = connectToDB()
    myCursor = myDb.cursor()

    # On récupère les informations de la note
    sql = f'''SELECT * FROM participe'''
    myCursor.execute(sql)
    datas = myCursor.fetchall()

    if(datas):
        response = {
            "participes" : [],
            "code" : 200
        }

        for data in datas :        
            response["participes"].append(
                {
                    "idParticipe" : data[0],
                    "idName" : data[1],
                    "idAnimal" : data[2],
                    "idActivite" : data[3],
                    "date" : data[4],
                }
            )
    
    else :
        response = {
            "message" : "Participations non trouvées",
            "code" : 404
        }

    # Fermeture de la connexion
    myCursor.close()
    myDb.close()

    return response

def getParticipeById(idParticipe) :
    # Connexion à la BDD
    myDb = connectToDB()
    myCursor = myDb.cursor()

    # On récupère les informations de l'animal
    sql = f'''SELECT * FROM participe WHERE idParticipe = {idParticipe}'''
    myCursor.execute(sql)
    data = myCursor.fetchall()

    if(data):
        response = {
            "participation": {
                "idParticipe" : data[0][0],
                "idName" : data[0][1],
                "idAnimal" : data[0][2],
                "date" : data[0][3]
            },
            "code" : 200
        }
    
    else :
        response = {
            "message" : "Participation non trouvé",
            "code" : 404
        }

    # Fermeture de la connexion
    myCursor.close()
    myDb.close()

    return response

def update(idParticipe, idName, idAnimal, idActivite, date) :
    # Connexion à la BDD
    myDb = connectToDB()
    myCursor = myDb.cursor()

    # Mise à jour de la fiche animal
    sql = f'''
        UPDATE participe SET 
        idName = "{idName}",
        idAnimal = {idAnimal},
        idActivite = {idActivite},
        date = "{date}"
        WHERE idParticipe = {idParticipe}
    '''
    myCursor.execute(sql)
    myDb.commit()

    # Fermeture de la connexion
    myCursor.close()
    myDb.close()

def delete(idParticipe) :
    # Connexion à la BDD
    myDb = connectToDB()
    myCursor = myDb.cursor()

    # Suppression de la fiche animal
    sql = f'''DELETE FROM participe WHERE idParticipe = {idParticipe}'''
    myCursor.execute(sql)
    myDb.commit()

    response = {
        "message" : "Participation supprimée",
        "code" : 200
    }

    # Fermeture de la connexion
    myCursor.close()
    myDb.close()

    return response