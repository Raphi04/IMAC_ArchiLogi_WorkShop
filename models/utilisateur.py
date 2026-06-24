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

def getAllUtilisateur() :
    # Connexion à la BDD
    myDb = connectToDB()
    myCursor = myDb.cursor()

    # On récupère les informations d'un utilisateur
    sql = f'''SELECT idName, username FROM utilisateurs '''
    myCursor.execute(sql)
    datas = myCursor.fetchall()
    if(datas):
        response = {
            "users" : [],
            "code" : 200
        }

        for data in datas :        
            response["users"].append(
                {
                    "idName" : data[0],
                    "username" : data[1],
                }
            )
    
    else :
        response = {
            "message" : "Utilisateurs non trouvés",
            "code" : 404
        }
    
    # Fermeture de la connexion
    myCursor.close()
    myDb.close()

    return response

def getUtilisateurById(idName) :
    # Connexion à la BDD
    myDb = connectToDB()
    myCursor = myDb.cursor()

    # On récupère les informations de la note
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

def connectUtilisateur(idName, pwd) :
    # Connexion à la BDD
    myDb = connectToDB()
    myCursor = myDb.cursor()

    # On vérifie le mot de passe de l'utilisateur
    sql = f'''SELECT pwd FROM utilisateurs WHERE idName = "{idName}"'''
    myCursor.execute(sql)
    data = myCursor.fetchall()

    if(data[0][0] == pwd):
        response = {
            "message": "L'utilisateur est connecté",
            "code" : 200
        }
    
    else :
        response = {
            "message" : "Le mot de passe n'est pas le bon",
            "code" : 400
        }
    
    # Fermeture de la connexion
    myCursor.close()
    myDb.close()

    return response
