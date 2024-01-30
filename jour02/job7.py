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
cursor.execute("SELECT * FROM employe WHERE salaire >= 3000")
for ligne in cursor.fetchall():
    print(ligne)

cursor.execute("SELECT employe.nom, employe.prenom, employe.salaire,service.nom FROM employe JOIN service ON employe.id_service = service.id")
for ligne in cursor.fetchall():
    print(ligne)
    

class employe:
    def __init__(self):
        password = getpass.getpass("Entrer le mdp :")
        self.database = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = password,
            database = "LaPlateforme"
        )
        self.cursor = self.database.cursor()
        
    
    def add_employe(self, nom,prenom,salaire,id_service):
        self.cursor.execute(f"INSERT INTO employe (nom,prenom,salaire,id_service) VALUES ('{nom}','{prenom}',{salaire},{id_service})")
        self.database.commit()
    
    def delete_employe(self,nom):
        self.cursor.execute(f"DELETE FROM employe WHERE nom = {nom} OR prenom = {nom}")
        self.database.commit()
    
    def afficher_employe(self):
        self.cursor.execute("SELECT * FROM employe")
        for ligne in self.cursor.fetchall():
            print(ligne)
    
    def modifie_employe(self,nom,prenom,salaire,id_service):
        self.cursor.execute(f"UPDATE employe SET nom = '{nom}' prenom = '{prenom}' salaire = {salaire} id_service = {id_service}")
        self.database.commit()