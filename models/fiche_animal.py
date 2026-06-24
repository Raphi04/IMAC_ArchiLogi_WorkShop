from database import connectToDB

def create(name, description, idName, idEspece, imageUrl) :
    # Connexion à la BDD
    myDb = connectToDB()
    myCursor = myDb.cursor()

    # Créer la fiche animal
    sql = f'''
        INSERT INTO fiches_animal VALUES 
        (
            NULL,
            "{name}",
            "{description}",
            "{idName}",
            {idEspece},
            "{imageUrl}"
        )
    '''
    myCursor.execute(sql)
    myDb.commit()

    # Fermeture de la connexion
    myCursor.close()
    myDb.close()

def getAll() :
    # Connexion à la BDD
    myDb = connectToDB()
    myCursor = myDb.cursor()

    # On récupère les informations de la note
    sql = f'''
        SELECT fiches_animal.name, fiches_animal.description, utilisateurs.idName, utilisateurs.username, especes.idEspece, especes.name, fiches_animal.imageURL
        FROM fiches_animal
        INNER JOIN utilisateurs ON fiches_animal.idName = utilisateurs.idName
        INNER JOIN especes ON fiches_animal.idEspece = especes.idEspece
        '''

    myCursor.execute(sql)
    datas = myCursor.fetchall()

    if(datas):
        response = {
            "fiches_animal" : [],
            "code" : 200
        }

        for data in datas :        
            response["fiches_animal"].append(
                {
                    "animal" : {
                        "name" : data[0],
                        "description" : data[1],
                        "imageUrl" : data[6]
                    },
                    
                    "user" : {
                        "idName" : data[2],
                        "username" : data[3]
                    },
                    
                    "espece" : {
                        "idEspece" : data[4],
                        "name" : data[5]
                    }
                },
            )
    
    else :
        response = {
            "message" : "Fiches animaux non trouvées",
            "code" : 404
        }

    # Fermeture de la connexion
    myCursor.close()
    myDb.close()

    return response

def getById(idAnimal) :
    # Connexion à la BDD
    myDb = connectToDB()
    myCursor = myDb.cursor()

    # On récupère les informations de l'animal
    sql = f'''
        SELECT fiches_animal.name, fiches_animal.description, utilisateurs.idName, utilisateurs.username, especes.idEspece, especes.name, fiches_animal.imageURL
        FROM fiches_animal
        INNER JOIN utilisateurs ON fiches_animal.idName = utilisateurs.idName
        INNER JOIN especes ON fiches_animal.idEspece = especes.idEspece
        WHERE idAnimal = "{idAnimal}"
        '''

    myCursor.execute(sql)
    data = myCursor.fetchall()

    if(data):
        response = {
            "fiche_animal": {
                "animal" : {
                    "name" : data[0][0],
                    "description" : data[0][1],
                    "imageUrl" : data[0][6]
                },
                "user" : {
                    "idName" : data[0][2],
                    "username" : data[0][3]
                },
                "espece" : {
                    "idEspece" : data[0][4],
                    "name" : data[0][5]
                }
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

def update(idAnimal, name, description, idName, idEspece, imageUrl) :
    # Connexion à la BDD
    myDb = connectToDB()
    myCursor = myDb.cursor()

    # Mise à jour de la fiche animal
    sql = f'''
        UPDATE fiches_animal SET 
        idAnimal = {idAnimal},
        name = "{name}",
        description = "{description}",
        idName = "{idName}",
        idEspece = {idEspece},
        imageUrl = "{imageUrl}"
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