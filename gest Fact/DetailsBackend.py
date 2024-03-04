import mysql.connector
from tkinter.messagebox import showerror,showinfo
class DetailsBackend:
    def __init__(self,idfact,idArt,Quant,curseur):
        self.idfact=idfact
        self.idArt=idArt
        self.Quant=Quant
        self.curseur=curseur

    def getdataArticle(self):
        sql = 'SELECT article.codArt FROM article'
        self.curseur.execute(sql)
        resultat= self.curseur.fetchall()
        return resultat



        