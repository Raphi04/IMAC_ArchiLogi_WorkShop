from database import connectToDB

def create(idEspece,idActivite) :
    # Connexion à la BDD
    myDb = connectToDB()
    myCursor = myDb.cursor()

    # Créer l'inclusion
    sql = f'''
        INSERT INTO inclue VALUES 
        (
            NULL,
            {idEspece},
            {idActivite}
        )
    '''
    myCursor.execute(sql)
    myDb.commit()

    # Fermeture de la connexion
    myCursor.close()
    myDb.close()

def get(idInclue) :
    # Connexion à la BDD
    myDb = connectToDB()
    myCursor = myDb.cursor()

    # On récupère les informations de l'animal
    sql = f'''SELECT idInclue, idEspece, idActivite FROM inclue WHERE idInclue = "{idInclue}"'''
    myCursor.execute(sql)
    data = myCursor.fetchall()

    if(data):
        response = {
            "inclue": {
                "idInclue" : data[0][0],
                "idEspece" : data[0][1],
                "idActivite" : data[0][2],
            },
            "code" : 200
        }
    
    else :
        response = {
            "message" : "Inclusion non trouvée",
            "code" : 404
        }

    # Fermeture de la connexion
    myCursor.close()
    myDb.close()

    return response

def update(idInclue,idEspece,idActivite) :
    # Connexion à la BDD
    myDb = connectToDB()
    myCursor = myDb.cursor()

    # Mise à jour de l'inclusion
    sql = f'''
        UPDATE inclue SET 
        idInclue = "{idInclue}",
        idEspece = "{idEspece}",
        idActivite = "{idActivite}"
        WHERE idInclue = "{idInclue}"
    '''
    myCursor.execute(sql)
    myDb.commit()

    # Fermeture de la connexion
    myCursor.close()
    myDb.close()

def delete(idInclue) :
    # Connexion à la BDD
    myDb = connectToDB()
    myCursor = myDb.cursor()

    # Suppression de l'inclusion
    sql = f'''DELETE FROM inclue WHERE idInclue = "{idInclue}"'''
    myCursor.execute(sql)
    myDb.commit()

    response = {
        "message" : "Inclusion supprimée",
        "code" : 200
    }

    # Fermeture de la connexion
    myCursor.close()
    myDb.close()

    return response