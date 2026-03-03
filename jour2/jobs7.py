import mysql.connector

db= mysql.connector.connect(
    host="localhost",
    user="root",
    password="***********",
    db="travail",)

cursor=db.cursor()
cursor.execute("SELECT * FROM employe WHERE salaire > 3000")
results=cursor.fetchall()
print(results)

cursor.execute( """
SELECT employe.id, employe.nom, employe.prenom, employe.salaire, service.nom
FROM employe
INNER JOIN service ON employe.id_service = service.id
""")

results=cursor.fetchall()
for row in results:
    print(row)

cursor.close()
db.close()

class Employe:
    def __init__(self, nom, prenom, salaire, service):
        self.nom = nom
        self.prenom = prenom
        self.salaire = salaire
        self.service = service

    def ajouter_employe(self):
        db= mysql.connector.connect(
            host="localhost",
            user="root",
            password="***********", 
            db="travail",)
        cursor=db.cursor()
        cursor.execute("INSERT INTO employe (nom, prenom, salaire, id_service) VALUES (%s, %s, %s, %s)",
                       (self.nom, self.prenom, self.salaire, self.service))
        db.commit()
        cursor.close()
        
    def changer_salaire(self, nouveau_salaire):
        db= mysql.connector.connect(
            host="localhost",
            user="root",
            password="***********",
            db="travail",)
        cursor=db.cursor()
        cursor.execute("UPDATE employe SET salaire = %s WHERE nom = %s AND prenom = %s", (nouveau_salaire, self.nom, self.prenom))
        db.commit()
        cursor.close()
        
    def changer_service(self, nouveau_service):
        db= mysql.connector.connect(
            host="localhost",
            user="root",
            password="***********",
            db="travail",)
        cursor=db.cursor()
        cursor.execute("UPDATE employe SET id_service = %s WHERE nom = %s AND prenom = %s", (nouveau_service, self.nom, self.prenom))
        db.commit()
        cursor.close()       
        
Employe1 = Employe("Dupont", "Jean", 3500, 1)
Employe1.ajouter_employe()
Employe1.changer_salaire(4000)
Employe1.changer_service(2)         