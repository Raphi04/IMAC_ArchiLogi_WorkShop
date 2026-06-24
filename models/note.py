from database import connectToDB

def create(idName, idAnimal,note) :
    # Connexion à la BDD
    myDb = connectToDB()
    myCursor = myDb.cursor()

    # Créer la note
    sql = f'''
        INSERT INTO notes VALUES 
        (
            NULL,
            "{idName}",
            {idAnimal},
            {note}
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
    sql = f'''SELECT * FROM notes'''
    myCursor.execute(sql)
    datas = myCursor.fetchall()

    if(datas):
        response = {
            "notes" : [],
            "code" : 200
        }

        for data in datas :        
            response["notes"].append(
                {
                    "idNote" : data[0],
                    "idName" : data[1],
                    "idAnimal" : data[2],
                    "note" : data[3],
                }
            )
    
    else :
        response = {
            "message" : "Notes non trouvées",
            "code" : 404
        }

    # Fermeture de la connexion
    myCursor.close()
    myDb.close()

    return response

def getNoteByName(idName, idAnimal) :
    # Connexion à la BDD
    myDb = connectToDB()
    myCursor = myDb.cursor()

    # On récupère les informations de la note
    sql = f'''SELECT idNote, idName, idAnimal, note FROM notes WHERE idName = "{idName}" AND idAnimal ={idAnimal}'''
    myCursor.execute(sql)
    data = myCursor.fetchall()

    if(data):
        response = {
            "note": {
                "idNote" : data[0][0],
                "idName" : data[0][1],
                "idAnimal" : data[0][2],
                "note" : data[0][3],
            },
            "code" : 200
        }
    
    else :
        response = {
            "message" : "Note non trouvée",
            "code" : 404
        }

    # Fermeture de la connexion
    myCursor.close()
    myDb.close()

    return response

def getNoteById(idNote) :
    # Connexion à la BDD
    myDb = connectToDB()
    myCursor = myDb.cursor()

    # On récupère les informations de la note
    sql = f'''SELECT * FROM notes WHERE idNote = {idNote}'''
    myCursor.execute(sql)
    data = myCursor.fetchall()

    if(data):
        response = {
            "note": {
                "idNote" : data[0][0],
                "idName" : data[0][1],
                "idAnimal" : data[0][2],
                "note" : data[0][3],
            },
            "code" : 200
        }
    
    else :
        response = {
            "message" : "Note non trouvée",
            "code" : 404
        }

    # Fermeture de la connexion
    myCursor.close()
    myDb.close()

    return response

def getAllFromUtilisateur(idName) :
    # Connexion à la BDD
    myDb = connectToDB()
    myCursor = myDb.cursor()

    # On récupère les informations de la note
    sql = f'''SELECT * FROM notes WHERE idName = "{idName}"'''
    myCursor.execute(sql)
    datas = myCursor.fetchall()

    if(datas):
        response = {
            "notes" : [],
            "code" : 200
        }

        for data in datas :        
            response["notes"].append(
                {
                    "idNote" : data[0],
                    "idName" : data[1],
                    "idAnimal" : data[2],
                    "note" : data[3],
                }
            )
    
    else :
        response = {
            "message" : "Notes non trouvées",
            "code" : 404
        }

    # Fermeture de la connexion
    myCursor.close()
    myDb.close()

    return response

def getAvgNoteAnimal(idAnimal):
    # Connexion à la BDD
    myDb = connectToDB()
    myCursor = myDb.cursor()

    # On récupère les informations de la note
    sql = f'''SELECT fiches_animal.idAnimal, fiches_animal.name, AVG(note)
    FROM notes 
    JOIN fiches_animal ON fiches_animal.idAnimal = notes.idAnimal
    WHERE {idAnimal} = {idAnimal}'''
    myCursor.execute(sql)
    data = myCursor.fetchall()

    if(data):
        moyenne_clamp = round(data[0][2],2)
        response = {
            "note": {
                "idAnimal" : data[0][0],
                "name" : data[0][1],
                "Moyenne note" : moyenne_clamp,
            },
            "code" : 200
        }
    
    else :
        response = {
            "message" : "Note non trouvée",
            "code" : 404
        }

    # Fermeture de la connexion
    myCursor.close()
    myDb.close()

    return response

def update(idNote, idName, idAnimal,note) :
    # Connexion à la BDD
    myDb = connectToDB()
    myCursor = myDb.cursor()

    # Mise à jour de la note
    sql = f'''
        UPDATE notes SET 
        idNote = "{idNote}",
        idName = "{idName}",
        idAnimal = "{idAnimal}",
        note = {note}
        WHERE idNote = "{idNote}"
    '''
    myCursor.execute(sql)
    myDb.commit()

    # Fermeture de la connexion
    myCursor.close()
    myDb.close()
def update(idNote, idName, idAnimal,note) :
    # Connexion à la BDD
    myDb = connectToDB()
    myCursor = myDb.cursor()

    # Mise à jour de la note
    sql = f'''
        UPDATE notes SET 
        idNote = "{idNote}",
        idName = "{idName}",
        idAnimal = "{idAnimal}",
        note = {note}
        WHERE idNote = "{idNote}"
    '''
    myCursor.execute(sql)
    myDb.commit()

    # Fermeture de la connexion
    myCursor.close()
    myDb.close()

def updateNoteByUser(idName, idNote, note) :
    # Connexion à la BDD
    myDb = connectToDB()
    myCursor = myDb.cursor()

    # Mise à jour de la note
    sql = f'''
        UPDATE notes SET 
        note = {note}
        WHERE idName = "{idName}" AND idNote = {idNote}
    '''
    myCursor.execute(sql)
    myDb.commit()

    # Fermeture de la connexion
    myCursor.close()
    myDb.close()


def delete(idNote) :
    # Connexion à la BDD
    myDb = connectToDB()
    myCursor = myDb.cursor()

    # Suppression de la note
    sql = f'''DELETE FROM notes WHERE idNote = "{idNote}"'''
    myCursor.execute(sql)
    myDb.commit()

    response = {
        "message" : "Note supprimée",
        "code" : 200
    }

    # Fermeture de la connexion
    myCursor.close()
    myDb.close()

    return response