from tkinter.messagebox import showerror

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