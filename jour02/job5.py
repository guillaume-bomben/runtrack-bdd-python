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
sup = 0
cursor.execute("SELECT superficie FROM etage")
for ligne in cursor.fetchall():
    sup += ligne[0]
print(f"La superficie de La Plateforme est de {sup} m2")