from database import connectToDB

def create(name, idName, idEspece) :
    # Connexion à la BDD
    myDb = connectToDB()
    myCursor = myDb.cursor()

    # Créer la fiche animal
    sql = f'''
        INSERT INTO fiches_animal VALUES 
        (
            NULL,
            "{name}",
            "{idName}",
            {idEspece}
        )
    '''
    myCursor.execute(sql)
    myDb.commit()

    # Fermeture de la connexion
    myCursor.close()
    myDb.close()

def get(idAnimal) :
    # Connexion à la BDD
    myDb = connectToDB()
    myCursor = myDb.cursor()

    # On récupère les informations de l'animal
    sql = f'''SELECT name, idName, idEspece FROM fiches_animal WHERE idAnimal = "{idAnimal}"'''
    myCursor.execute(sql)
    data = myCursor.fetchall()

    if(data):
        response = {
            "fiche_animal": {
                "name" : data[0][0],
                "idName" : data[0][1],
                "idEspece" : data[0][2],
            },
            "code" : 200
        }
    
    else :
        response = {
            "message" : "Fiche animal non trouvé",
            "code" : 404
        }

    # Fermeture de la connexion
    myCursor.close()
    myDb.close()

    return response

def update(idAnimal, name, idName, idEspece) :
    # Connexion à la BDD
    myDb = connectToDB()
    myCursor = myDb.cursor()

    # Mise à jour de la fiche animal
    sql = f'''
        UPDATE fiches_animal SET 
        idAnimal = {idAnimal},
        name = "{name}",
        idName = "{idName}",
        idEspece = {idEspece}
        WHERE idAnimal = {idAnimal}
    '''
    myCursor.execute(sql)
    myDb.commit()

    # Fermeture de la connexion
    myCursor.close()
    myDb.close()

def delete(idAnimal) :
    # Connexion à la BDD
    myDb = connectToDB()
    myCursor = myDb.cursor()

    # Suppression de la fiche animal
    sql = f'''DELETE FROM fiches_animal WHERE idAnimal = "{idAnimal}"'''
    myCursor.execute(sql)
    myDb.commit()

    response = {
        "message" : "Fiche animal supprimée",
        "code" : 200
    }

    # Fermeture de la connexion
    myCursor.close()
    myDb.close()

    return response