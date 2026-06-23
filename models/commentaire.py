from database import connectToDB

def create(idName, idAnimal, commentaire) :
    # Connexion à la BDD
    myDb = connectToDB()
    myCursor = myDb.cursor()

    # Créer le commentaire
    sql = f'''
        INSERT INTO commentaires VALUES 
        (
            "{idName}",
            {idAnimal},
            "{commentaire}"
        )
    '''
    myCursor.execute(sql)
    myDb.commit()

    # Fermeture de la connexion
    myCursor.close()
    myDb.close()

def get(idName, idAnimal) :
    # Connexion à la BDD
    myDb = connectToDB()
    myCursor = myDb.cursor()

    # On récupère les informations de l'animal
    sql = f'''SELECT idName, idAnimal, commentaire FROM commentaires WHERE idName = "{idName}" AND idAnimal = {idAnimal}'''
    myCursor.execute(sql)
    data = myCursor.fetchall()

    if(data):
        response = {
            "commentaire": {
                "idName" : data[0][0],
                "idAnimal" : data[0][1],
                "commentaire" : data[0][2],
            },
            "code" : 200
        }
    
    else :
        response = {
            "message" : "Commentaire non trouvé",
            "code" : 404
        }

    # Fermeture de la connexion
    myCursor.close()
    myDb.close()

    return response

def update(idName, idAnimal, commentaire) :
    # Connexion à la BDD
    myDb = connectToDB()
    myCursor = myDb.cursor()

    # Mise à jour de la fiche animal
    sql = f'''
        UPDATE commentaires SET 
        idName = "{idName}",
        idAnimal = {idAnimal},
        commentaire = "{commentaire}"
        WHERE idName = "{idName}" AND idAnimal = {idAnimal}
    '''
    myCursor.execute(sql)
    myDb.commit()

    # Fermeture de la connexion
    myCursor.close()
    myDb.close()

def delete(idName, idAnimal) :
    # Connexion à la BDD
    myDb = connectToDB()
    myCursor = myDb.cursor()

    # Suppression de la fiche animal
    sql = f'''DELETE FROM commentaires WHERE idName = "{idName}" AND idAnimal = {idAnimal}'''
    myCursor.execute(sql)
    myDb.commit()

    response = {
        "message" : "Commentaire supprimée",
        "code" : 200
    }

    # Fermeture de la connexion
    myCursor.close()
    myDb.close()

    return response