import mysql.connector

db= mysql.connector.connect(
    host="localhost",
    user="root",
    password="MohamedSwain-13010",
    db="Laplateforme",)

cursor=db.cursor()
cursor.execute("SELECT superficie FROM etage")
results=cursor.fetchall()
superficie_totale = sum(row[0] for row in results)

print(f"Superficie totale de la Plateforme est de : {superficie_totale} m2")

cursor.close()
db.close()
