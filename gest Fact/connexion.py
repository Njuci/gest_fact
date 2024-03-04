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
            cursor.execute("select * from article where codArt=%s",(self.cod,))
            return cursor.fetchall()
        except Exception as e:
            print(e)
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
            showinfo("Suppression",f'Suppression de {self.cod} Reussi ')
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
    def recuperer_codeArticle(self,cursor):
        try:
            cursor.execute("select codArt from article")
            return cursor.fetchall()
        except Exception as e:
            showerror("Affichage",str(e))
            return False

class FactBackend:
    def __init__(self,idFact,DateFac,Reduction,IdCli):
        self.IdFac=idFact
        self.Reduction=Reduction
        self.DateFac=DateFac
        self.IdCli=IdCli
        self.curseur=None
    def save(self,cursor):
        try:
            cursor.execute("insert into facture values(%s,%s,%s,%s)",(self.IdFac,self.DateFac,self.Reduction,self.IdCli))

            return True
        except Exception as e:
            showerror("Enregistrement",str(e))
            return False
        
    def getData(self,cursor):
        try:
            self.curseur=cursor
            sql = 'SELECT Facture.idFact,Facture.datfact,Facture.reduction,Facture.idcli, Customer.nomcli FROM Facture INNER JOIN Customer ON Facture.idcli=Customer.idcli'
            self.curseur.execute(sql)
            resultat= self.curseur.fetchall()
            return resultat
        except Exception as exp :
            showerror('BAC4 INFO', str(exp))
    def UpdateData(self,cursor):
        self.curseur=cursor
        try:
            sql = 'UPDATE Facture SET  datfact=%s,reduction=%s,idcli=%s WHERE idFact = %s'
            val = (self.DateFac,self.Reduction,self.IdCli, self.IdFac)
            self.curseur.execute(sql,val)
            showinfo('BAC4 INFO','Facture Modifié')
        except Exception as exp :
            showerror('BAC4 INFO', str(exp))
        

class DetailsBackend:
    def __init__(self,idfact,idArt,Quant):
        self.idfact=idfact
        self.idArt=idArt
        self.Quant=Quant
        self.curseur=None

    def getdataArticle(self,curseur):
        self.curseur=curseur
        sql = 'SELECT article.codArt FROM article'
        self.curseur.execute(sql)
        resultat= self.curseur.fetchall()
        return resultat
    """ajourter un detail de la facture"""
    def save(self,cursor):

        try:
            cursor.execute("insert into vente values(%s,%s,%s)",(self.idfact,self.idArt,self.Quant))

            return True
        except Exception as e:
            showerror("Enregistrement",str(e))
            return False 
    def getDetails(self,cursor):
        try:
            self.curseur=cursor
            sql = 'SELECT DISTINCT article.desiArt,article.prix,vente.quantite,article.codArt FROM article INNER JOIN vente INNER JOIN facture ON vente.idfact=%s AND vente.codArt=article.codArt'
            val = (self.idfact,)
            self.curseur.execute(sql,val)
            resultat= self.curseur.fetchall()
            return resultat
        except Exception as exp :
            showerror('Gest Fact', str(exp))
    def UpdateData(self,cursor):
        self.curseur=cursor
        try:
            sql = 'UPDATE vente SET  quantite=%s WHERE codArt = %s AND idfact=%s '
            val = (self.Quant, self.idArt,self.idfact)
            self.curseur.execute(sql,val)
            showinfo('BAC4 INFO','Modification reçu')
        except Exception as exp :
            showerror('BAC4 INFO', str(exp))
    
class PaiementBackend:
    # create table Paiement(
    # datepaie date,
    # idfact varchar(5),
    # montant float(12,2),
    # constraint pk_p_fact foreign key(idFact) References Facture(idFact)
    def __init__(self):
        self.curseur=None
    def __init__(self,date:str,idfact:str,montant:float):
        self.date = date
        self.idfact = idfact
        self.montant = montant
        self.curseur = None
    """sauvegarde du paiement dans la base de données"""
    def savePaiement(self,cursor):
        try:
            cursor.execute("insert into paiement values(%s,%s,%s)",(self.date,self.idfact,self.montant))
            return True
        except Exception as e:
            showerror("Enregistrement",str(e))
            return False
    """recherche d'un paiement dans la base de données"""
    def searchPaiement(self,cursor):
        try:
            cursor.execute("select * from paiement where idfact=%s",(self.idfact,))
            return cursor.fetchall()
        except Exception as e:
            showerror("Recherche",str(e))
            return False
    """modification d'un paiement dans la base de données"""
    def updatePaiement(self,cursor,element):
        try:
            # update paiement where idFact and date = %s only
            cursor.execute("update paiement set montant=%s where idFact=%s and datepaie=%s",(self.montant,self.idfact,self.date))
            return True
        except Exception as e:
            showerror("Modification",str(e))
            return False
    """suppression d'un paiement dans la base de données"""
    def deletePaiement(self,cursor):
        try:
            # delete from paiement where idFact and date = %s and montant = %s
            cursor.execute("delete from paiement where idFact=%s and datepaie=%s",(self.idfact,self.date))
            return True
        except Exception as e:
            showerror("Suppression",str(e))
            return False
    """affichage de tous les paiements dans la base de données"""
    def allPaiement(self,cursor):
        try:
            cursor.execute("select * from paiement")
            return cursor.fetchall()
        except Exception as e:
            showerror("Affichage",str(e))
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
    