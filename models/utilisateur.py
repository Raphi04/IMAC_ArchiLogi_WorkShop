from database import connectToDB

def create(idName, username, pwd) :
    # Connexion à la BDD
    myDb = connectToDB()
    myCursor = myDb.cursor()

    # Créer l'utilisateur
    sql = f'''
        INSERT INTO utilisateurs VALUES 
        (
            "{idName}",
            "{username}",
            "{pwd}"
        )
    '''
    myCursor.execute(sql)
    myDb.commit()

    # Fermeture de la connexion
    myCursor.close()
    myDb.close()

def get(idName) :
    # Connexion à la BDD
    myDb = connectToDB()
    myCursor = myDb.cursor()

    # On récupère les informations d'un utilisateur
    sql = f'''SELECT idName, username FROM utilisateurs WHERE idName = "{idName}"'''
    myCursor.execute(sql)
    data = myCursor.fetchall()

    if(data):
        response = {
            "user": {
                "idName" : data[0][0],
                "username" : data[0][1],
            },
            "code" : 200
        }
    
    else :
        response = {
            "message" : "Utilisateur non trouvé",
            "code" : 404
        }
    
    # Fermeture de la connexion
    myCursor.close()
    myDb.close()

    return response

def update(previousIdName, idName, username, pwd) :
    # Connexion à la BDD
    myDb = connectToDB()
    myCursor = myDb.cursor()

    # Mise à jour de l'utilisateur
    sql = f'''
        UPDATE utilisateurs SET 
        idName = "{idName}",
        username = "{username}",
        pwd = "{pwd}"
        WHERE idName = "{previousIdName}"
    '''
    myCursor.execute(sql)
    myDb.commit()

    # Fermeture de la connexion
    myCursor.close()
    myDb.close()

def delete(idName) :
    # Connexion à la BDD
    myDb = connectToDB()
    myCursor = myDb.cursor()

    # Suppression de l'utilisateur
    sql = f'''DELETE FROM utilisateurs WHERE idName = "{idName}"'''
    myCursor.execute(sql)
    myDb.commit()

    response = {
        "message" : "Utilisateur supprimé",
        "code" : 200
    }

    # Fermeture de la connexion
    myCursor.close()
    myDb.close()

    return response