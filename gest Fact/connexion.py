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




class FactureBackend:
    # create table Facture(
    # idFact varchar(5),
    # dateFact date,
    # idClient varchar(5),
    # constraint pk_fact foreign key(idClient) References Client(idClient)
    def __init__(self):
        self.curseur=None
    def __init__(self,idFact:str,dateFact:str,idClient:str):
        self.idFact = idFact
        self.dateFact = dateFact
        self.idClient = idClient
        self.curseur = None
    """affichage de toutes les factures dans la base de données"""
    def allFacture(self,cursor):
        try:
            cursor.execute("select * from facture")
            return cursor.fetchall()
        except Exception as e:
            showerror("Affichage",str(e))
            return False
    def afficherUneFacture(self,cursor,factureId):
        try:
            cursor.execute("select * from facture where idFact=%s",(factureId,))
            return cursor.fetchall()
        except Exception as e:
            showerror("Affichage",str(e))
            return False
        

class VenteBackend:
    # codArt, idFact, quantite

    def __init__(self):
        self.curseur=None
    def __init__(self,codArt:str,idFact:str,quantite:int):
        self.codArt = codArt
        self.idFact = idFact
        self.quantite = quantite
        self.curseur = None
    # Récupérer les ventes dans la base de données
    def allVente(self,cursor):
        try:
            cursor.execute("select * from vente")
            return cursor.fetchall()
        except Exception as e:
            showerror("Affichage",str(e))
            return False
    # Recupérer les ventes d'une facture dans la base de données
    def venteFacture(self,cursor,factureId):
        try:
            cursor.execute("select * from vente where idFact=%s",(factureId,))
            return cursor.fetchall()
        except Exception as e:
            showerror("Affichage",str(e))
            return False
    