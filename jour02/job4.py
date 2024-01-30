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

cursor.execute("SELECT nom,capacite FROM salle")
for ligne in cursor.fetchall():
    print(ligne)