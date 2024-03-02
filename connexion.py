import mysql.connector 
from tkinter.messagebox import showerror
class Connexion:
    def __init__(self):
        self.db = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = '3670njci',
            database = 'Facturation',
            autocommit=True
        )
        self.curseur = self.db.cursor()
    def get_connexion(self):
        return self.curseur
    def get_parametres_connexion(self):
        return self.db

class Login_back:
    def __init__(self,user,pswd):
        self.user=user
        self.password=pswd
        self.db=None
        self.curseur=None
    def login(self):
        """"login de l'utilisateur dans la base de données""" 
        try:
            self.db = mysql.connector.connect(
                host = 'localhost',
                user = self.user,
                password = self.password,
                database = 'Facturation',
                 autocommit=True
            )
            self.curseur = self.db.cursor()
            return True
        except Exception as e:
            showerror("Connexion",str(e))
            return False    


class ArticleBackend:
    
    def __init__(self):
        self.curseur=None


    def __init__(self,cod:str,desi:str,prix:float):
        self.cod = cod
        self.designation = desi
        self.prix = prix
        self.curseur = None
    """sauvegarde de l'article dans la base de données"""
    def save(self,cursor):
        self.curseur=cursor
        self.curseur.execute("insert into article values(%s,%s,%s)",(self.cod,self.designation,self.prix))
        
        return True
    
    """recherche d'un article dans la base de données"""
    def search(self,cursor):
        cursor.execute("select * from article where code=%s",(self.cod,))
        return cursor.fetchall()
    """modification d'un article dans la base de données"""
    def update(self,cursor):
        cursor.execute("update article set designation=%s,prix=%s where code=%s",(self.designation,self.prix,self.cod))
        cursor.commit()
    """suppression d'un article dans la base de données"""  
    def delete(self,cursor):
        cursor.execute("delete from article where code=%s",(self.cod,))
        cursor.commit()

    """affichage de tous les articles dans la base de données"""
    def all(self,cursor):
        cursor.execute("select * from article")
        return cursor.fetchall()
    