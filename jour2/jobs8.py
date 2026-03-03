import mysql.connector

class animal:
    def __init__(self, nom, race,id_cage, date_naissance):
        self.nom = nom
        self.race = race
        self.id_cage = id_cage
        self.date_naissance = date_naissance

    def ajouter_animal(self):
        db= mysql.connector.connect(
            host="localhost",
            user="root",
            password="***********", 
            db="travail",)
        cursor=db.cursor()
        cursor.execute("INSERT INTO animal (nom, race, id_cage, date_naissance) VALUES (%s, %s, %s, %s)",
                       (self.nom, self.race, self.id_cage, self.date_naissance))
        db.commit()
        cursor.close()
    
    def suprimer_animal(self):
        db= mysql.connector.connect(
            host="localhost",
            user="root",
            password="***********",
            db="travail",)
        cursor=db.cursor()
        cursor.execute("DELETE FROM animal WHERE nom = %s AND race = %s", (self.nom, self.race))
        db.commit()
        cursor.close()
        
class cage:
    def __init__(self, superficie, capacite):
        self.superficie = superficie
        self.capacite = capacite

    def ajouter_cage(self):
        db= mysql.connector.connect(
            host="localhost",
            user="root",
            password="***********", 
            db="travail",)
        cursor=db.cursor()
        cursor.execute("INSERT INTO cage (superficie, capacite) VALUES (%s, %s)",
                       (self.superficie, self.capacite))
        db.commit()
        cursor.close()
        
    def suprimer_cage(self):
        db= mysql.connector.connect(
            host="localhost",
            user="root",
            password="***********",
            db="travail",)
        cursor=db.cursor()
        cursor.execute("DELETE FROM cage WHERE superficie = %s AND capacite = %s", (self.superficie, self.capacite))
        db.commit()
        cursor.close()         

class zoo(cage, animal):
    def __init__(self, superficie, capacite, nom_animal, race, id_cage, date_naissance):
        cage.__init__(self, superficie, capacite)
        animal.__init__(self, nom_animal, race, id_cage, date_naissance)
        
    def nb_animaux(self):
        db= mysql.connector.connect(
            host="localhost",
            user="root",
            password="***********",
            db="travail",)
        cursor=db.cursor()
        cursor.execute("SELECT COUNT(*) FROM animal")
        result = cursor.fetchone()
        cursor.close()
        return result[0]
    
    def ajourer_dans_zoo(self, nom_animal, race, id_cage, date_naissance):
        self.nom = nom_animal
        self.race = race
        self.id_cage = id_cage
        self.date_naissance = date_naissance
        self.ajouter_animal()

    def nm_animaux_par_cage(self, id_cage):
        db= mysql.connector.connect(
            host="localhost",
            user="root",
            password="***********",
            db="travail",)
        cursor=db.cursor()
        cursor.execute("SELECT COUNT(*) FROM animal WHERE id_cage = %s", (id_cage,))
        result = cursor.fetchone()
        cursor.close()
        return result[0]
    
    def superficie_totale(self):
        db= mysql.connector.connect(
            host="localhost",
            user="root",
            password="***********",
            db="travail",)
        cursor=db.cursor()
        cursor.execute("SELECT SUM(superficie) FROM cage")
        result = cursor.fetchone()
        cursor.close()
        return result[0]


zoo1 = zoo(100, 5, "Lion", "Panthera leo", 1, "2010-05-15")
print("Nombre total d'animaux dans le zoo :", zoo1.nb_animaux())
print("Nombre d'animaux dans la cage 1 :", zoo1.nm_animaux_par_cage(1))
print("Superficie totale du zoo :", zoo1.superficie_totale())
zoo1.ajourer_dans_zoo("Tigre", "Panthera tigris", 2, "2012-03-20")