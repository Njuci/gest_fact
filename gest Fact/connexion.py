import mysql.connector 
from tkinter.messagebox import showerror,showinfo
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
        try:
            cursor.execute("insert into article values(%s,%s,%s)",(self.cod,self.designation,self.prix))
            return True
        except Exception as e:
            showerror("Enregistrement",str(e))
            return False
        
    
    """recherche d'un article dans la base de données"""
    def search(self,cursor):
        try:
            cursor.execute("select * from article where code=%s",(self.cod,))

            return cursor.fetchall()
        except Exception as e:
            showerror("Recherche",str(e))
            return False
        
        
    """modification d'un article dans la base de données"""
    def update(self,cursor,element):
        try:
            cursor.execute("update article set desiArt=%s,prix=%s , codArt=%s where codArt=%s and desiArt=%s and prix=%s ",
                           (self.designation,self.prix,self.cod,element[0],element[1],element[2]))
            showinfo("Modification",f'Modification de {element[0]} Reussi ')

            return True
        except Exception as e:
            showerror("Modification",str(e))
            return False
    """suppression d'un article dans la base de données"""  
    def delete(self,cursor):
        try:
            cursor.execute("delete from article where codArt=%s",(self.cod,))
            showinfo("Suppression",f'Suppression de {self.code} Reussi ')
            return True
        except Exception as e:
            showerror("Suppression",str(e))
            return False
        

    """affichage de tous les articles dans la base de données"""
    def all(self,cursor):
        try:
            cursor.execute("select * from article")
            return cursor.fetchall()
        except Exception as e:
            showerror("Affichage",str(e))
            return False
        