from tkinter.messagebox import showerror

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
    def getPaimentWithFactureAndProduct(self,cursor):
        try:
            cursor.execute("select * from paiement p, facture f, vente v where p.idFact = f.idFact and f.idFact = v.idFact")
            return cursor.fetchall()
        except Exception as e:
            showerror("Affichage",str(e))
            return False

    
