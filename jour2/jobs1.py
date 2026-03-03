import mysql.connector

db= mysql.connector.connect(
    host="localhost",
    user="root",
    password="***********",
    db="Laplateforme",)

cursor=db.cursor()
cursor.execute("SELECT * FROM etudiant")
results=cursor.fetchall()
print(results)

cursor.close()
db.close()

