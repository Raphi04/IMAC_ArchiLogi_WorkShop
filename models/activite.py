from database import connectToDB

def create(name) :
    # Connexion à la BDD
    myDb = connectToDB()
    myCursor = myDb.cursor(dictionary=True)

    # Créer l'activité
    sql = f'''
        INSERT INTO activites VALUES 
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

def get(idActivite) :
    # Connexion à la BDD
    myDb = connectToDB()
    myCursor = myDb.cursor()

    # On récupère les informations d'une activité
    sql = f'''SELECT idActivite, name FROM activites WHERE idActivite = {idActivite}'''
    myCursor.execute(sql)
    data = myCursor.fetchall()

    if(data):
        response = {
            "activite": {
                "idActivite" : data[0][0],
                "name" : data[0][1],
            },
            "code" : 200
        }
    
    else :
        response = {
            "message" : "Activité non trouvé",
            "code" : 404
        }
    
    # Fermeture de la connexion
    myCursor.close()
    myDb.close()

    return response

def update(idActivite, name) :
    # Connexion à la BDD
    myDb = connectToDB()
    myCursor = myDb.cursor()

    # Mise à jour de l'espèce
    sql = f'''
        UPDATE activites SET 
        name = "{name}"
        WHERE idActivite = {idActivite}
    '''
    myCursor.execute(sql)
    myDb.commit()

    # Fermeture de la connexion
    myCursor.close()
    myDb.close()

def delete(idActivite) :
    # Connexion à la BDD
    myDb = connectToDB()
    myCursor = myDb.cursor()

    # Suppression de l'activité
    sql = f'''DELETE FROM activites WHERE idActivite = "{idActivite}"'''
    myCursor.execute(sql)
    myDb.commit()

    response = {
        "message" : "Activité supprimée",
        "code" : 200
    }

    # Fermeture de la connexion
    myCursor.close()
    myDb.close()

    return response