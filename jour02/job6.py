import getpass
import mysql.connector

paw = getpass.getpass("Entrer le mdp :")
db = mysql.connector.connect(
  host = "localhost",
  user = "root",
  password = paw,
  database = "LaPlateforme"
)

cursor = db.cursor()
cap = 0
cursor.execute("SELECT capacite FROM salle")
for ligne in cursor.fetchall():
    cap += ligne[0]
print(f"La capacite de toute les salles est de : {cap}")