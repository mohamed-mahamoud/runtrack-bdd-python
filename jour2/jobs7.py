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
