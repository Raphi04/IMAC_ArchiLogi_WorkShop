from database import connectToDB

def create(idName, idAnimal, commentaire) :
    # Connexion à la BDD
    myDb = connectToDB()
    myCursor = myDb.cursor()

    # Créer le commentaire
    sql = f'''
        INSERT INTO commentaires VALUES 
        (
            NULL,
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

def getAll() :
    # Connexion à la BDD
    myDb = connectToDB()
    myCursor = myDb.cursor()

    # On récupère les informations d'un utilisateur
    sql = f'''
        SELECT commentaires.idCommentaire, commentaires.commentaire, utilisateurs.idName, utilisateurs.username, fiches_animal.idAnimal, fiches_animal.name
        FROM commentaires
        INNER JOIN utilisateurs ON commentaires.idName = utilisateurs.idName
        INNER JOIN fiches_animal ON commentaires.idAnimal = fiches_animal.idAnimal
        '''
    myCursor.execute(sql)
    datas = myCursor.fetchall()
    if(datas):
        response = {
            "commentaires" : [],
            "code" : 200
        }

        for data in datas :        
            response["commentaires"].append(
                {
                    "commentaire": {
                        "idCommentaire" : data[0],
                        "commentaire" : data[1],
                    },

                    "utilisateur": {
                        "idName" : data[2],
                        "username" : data[3],
                    },

                    "fiche_animal" : {
                        "idAnimal" : data[4],
                        "name" : data[5]
                    },
                }
            )
    
    else :
        response = {
            "message" : "Commentaires non trouvés",
            "code" : 404
        }
    
    # Fermeture de la connexion
    myCursor.close()
    myDb.close()

    return response

def getById(idCommentaire) :
    # Connexion à la BDD
    myDb = connectToDB()
    myCursor = myDb.cursor()

    # On récupère les informations du commmentaire
    sql = f'''
        SELECT commentaires.idCommentaire, commentaires.commentaire, utilisateurs.idName, utilisateurs.username, fiches_animal.idAnimal, fiches_animal.name
        FROM commentaires
        INNER JOIN utilisateurs ON commentaires.idName = utilisateurs.idName
        INNER JOIN fiches_animal ON commentaires.idAnimal = fiches_animal.idAnimal
        WHERE idCommentaire = {idCommentaire}
        '''
    myCursor.execute(sql)
    data = myCursor.fetchall()

    if(data):
        response = {
            "commentaire": {
                "idCommentaire" : data[0][0],
                "commentaire" : data[0][1],
            },

            "utilisateur": {
                "idName" : data[0][2],
                "username" : data[0][3],
            },

            "fiche_animal" : {
                "idAnimal" : data[0][4],
                "name" : data[0][5]
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

def getByAnimal(idAnimal) :
    # Connexion à la BDD
    myDb = connectToDB()
    myCursor = myDb.cursor()

    # On récupère les informations d'un utilisateur
    sql = f'''
        SELECT commentaires.idCommentaire, commentaires.commentaire, utilisateurs.idName, utilisateurs.username, fiches_animal.idAnimal, fiches_animal.name
        FROM commentaires
        INNER JOIN utilisateurs ON commentaires.idName = utilisateurs.idName
        INNER JOIN fiches_animal ON commentaires.idAnimal = fiches_animal.idAnimal
        WHERE fiches_animal.idAnimal = {idAnimal}
        '''
    myCursor.execute(sql)
    datas = myCursor.fetchall()
    if(datas):
        response = {
            "commentaires" : [],
            "code" : 200
        }

        for data in datas :        
            response["commentaires"].append(
                {
                    "commentaire": {
                        "idCommentaire" : data[0],
                        "commentaire" : data[1],
                    },

                    "utilisateur": {
                        "idName" : data[2],
                        "username" : data[3],
                    },

                    "fiche_animal" : {
                        "idAnimal" : data[4],
                        "name" : data[5]
                    },
                }
            )
    
    else :
        response = {
            "message" : "Commentaires non trouvés",
            "code" : 404
        }
    
    # Fermeture de la connexion
    myCursor.close()
    myDb.close()

    return response

def update(idCommentaire, commentaire) :
    # Connexion à la BDD
    myDb = connectToDB()
    myCursor = myDb.cursor()

    # Mise à jour de la fiche animal
    sql = f'''
        UPDATE commentaires SET 
        commentaire = "{commentaire}"
        WHERE idCommentaire = {idCommentaire}
    '''
    myCursor.execute(sql)
    myDb.commit()

    # Fermeture de la connexion
    myCursor.close()
    myDb.close()

def delete(idCommentaire) :
    # Connexion à la BDD
    myDb = connectToDB()
    myCursor = myDb.cursor()

    # Suppression de la fiche animal
    sql = f'''DELETE FROM commentaires WHERE idCommentaire = {idCommentaire}'''
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