import mysql.connector

db= mysql.connector.connect(
    host="localhost",
    user="root",
    password="MohamedSwain-13010",
    db="Laplateforme",)

cursor=db.cursor()
cursor.execute("SELECT nom, capacite FROM salle")
results=cursor.fetchall()
for nom,capacite in results:
    print(f"Nom de la salle: {nom}, Capacité: {capacite}")

cursor.close()
db.close()
