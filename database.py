import os
from dotenv import load_dotenv

import mysql.connector

load_dotenv()

def connectToDB() :
    myDb = mysql.connector.connect(
        host=os.getenv("HOST"),
        user=os.getenv("USER"),
        password=os.getenv("PWD"),
        database=os.getenv("DATABASE")
    )

    return myDb