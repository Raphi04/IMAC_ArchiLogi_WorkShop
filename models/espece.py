from database import connectToDB

def create(name) :
    # Connexion à la BDD
    myDb = connectToDB()
    myCursor = myDb.cursor(dictionary=True)

    # Créer l'espèce
    sql = f'''
        INSERT INTO especes VALUES 
        (
            NULL,
            "{name}"
        )
    '''
    myCursor.execute(sql)
    myDb.commit()

    # Fermeture de la connexion
    myCursor.close()
    myDb.close()

def getAllEspece() :
    # Connexion à la BDD
    myDb = connectToDB()
    myCursor = myDb.cursor()

    # On récupère les informations d'une espèce
    sql = f'''SELECT * FROM especes'''
    myCursor.execute(sql)
    datas = myCursor.fetchall()

    if(datas):
        response = {
            "especes" : [],
            "code" : 200
        }

        for data in datas :        
            response["especes"].append(
                {
                    "idEspece" : data[0],
                    "name" : data[1],
                }
            )
    
    else :
        response = {
            "message" : "Espèces non trouvées",
            "code" : 404
        }
    
    # Fermeture de la connexion
    myCursor.close()
    myDb.close()

    return response

def getEspeceById(idEspece) :
    # Connexion à la BDD
    myDb = connectToDB()
    myCursor = myDb.cursor()

    # On récupère les informations de la note
    sql = f'''SELECT idEspece, name FROM especes WHERE idEspece = "{idEspece}"'''
    myCursor.execute(sql)
    data = myCursor.fetchall()

    if(data):
        response = {
            "espece": {
                "idEspece" : data[0][0],
                "name" : data[0][1],
            },
            "code" : 200
        }
    
    else :
        response = {
            "message" : "Espèce non trouvée",
            "code" : 404
        }

    # Fermeture de la connexion
    myCursor.close()
    myDb.close()

    return response 

def update(idEspece, name) :
    # Connexion à la BDD
    myDb = connectToDB()
    myCursor = myDb.cursor()

    # Mise à jour de l'espèce
    sql = f'''
        UPDATE especes SET 
        name = "{name}"
        WHERE idEspece = {idEspece}
    '''
    myCursor.execute(sql)
    myDb.commit()

    # Fermeture de la connexion
    myCursor.close()
    myDb.close()

def delete(idEspece) :
    # Connexion à la BDD
    myDb = connectToDB()
    myCursor = myDb.cursor()

    # Suppression de l'espèce
    sql = f'''DELETE FROM especes WHERE idEspece = "{idEspece}"'''
    myCursor.execute(sql)
    myDb.commit()

    response = {
        "message" : "Espèce supprimé",
        "code" : 200
    }

    # Fermeture de la connexion
    myCursor.close()
    myDb.close()

    return response