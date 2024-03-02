import mysql.connector 
from tkinter.messagebox import showerror
class Connexion:
    def __init__(self):
        self.db = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = '3670njci',
            database = 'Facturation'
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
        
            
        try:
            self.db=mysql.connector.connect(
            host = 'localhost',
            user = self.user,
            password = self.password,
            database = 'Facturation'
                 )

            if self.db.is_connected():
                self.curseur=self.db.cursor
                return True
             
        except Exception:
            showerror("Erreur de connesxion","invalid credentials")
    def get_connexion(self):
        return self.curseur
    


class ArticleBackend:
    def _init_(self,cod,desi,prix):
        self.cod = cod
        self.designation = desi
        self.prix = prix
    def save(self,cursor):
        cursor.execute