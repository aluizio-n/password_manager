from dotenv import load_dotenv
import os
import sqlite3

load_dotenv()

DB_PATH = os.getenv("DB_PATH")

def create_db():
    """ create db if it not exists """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""

    CREATE TABLE IF NOT EXISTS passwords (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        site TEXT NOT NULL,
        user TEXT NOT NULL,
        encrypt_password TEXT NOT NULL
                   )    

""")
    conn.commit()
    conn.close()

def save_password(site, user, encrypt_password):
    """" saves credentials in database """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO passwords (site, user, encrypt_password) VALUES (? ,?, ?)", (site, user, encrypt_password))
    conn.commit()
    conn.close()
    
def get_passwords():
    """ returns all passwords """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * from passwords")
    data = cursor.fetchall()
    conn.close()
    return data