import mysql.connector

db= mysql.connector.connect(
    host="localhost",
    user="root",
    password="***********",
    db="Laplateforme",)

cursor=db.cursor()
cursor.execute("SELECT capacite FROM salle")
results=cursor.fetchall()
capacite_totale = sum(row[0] for row in results)

print(f"CapacitÃ© totale des salles est de : {capacite_totale}")

cursor.close()
db.close()

