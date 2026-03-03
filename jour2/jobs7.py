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

cursor.close()
db.close()
