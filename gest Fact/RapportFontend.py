from tkinter import *
from tkinter.messagebox import showinfo
import webbrowser 

from RapportBackend import RapportBackend
from rapport import genererRapportPaiement, genereRapportArticle,generateRapportFacture,generateRapportCustomer
from articlebackend import ArticleBackend

import os

import datetime


class RapportFrontend:
    def __init__(self,curseur):
        self.curseur=curseur
        self.fen = Tk()
        self.fen.title("GESTION DE LA FACTURATION - RAPPORTS")
        self.fen.geometry("800x600") 
        #Creation du conteneur menu et ses elements
        self.MenuContainer=Frame(self.fen,height=800,width=230,bg='#51a596')
        self.MenuContainer.place(x=0,y=0)
        self.titre = Label(self.MenuContainer, text = "GEST - FACT", font = "Arial 15 bold",bg='#51a596',fg='white').place(x=30, y=20)

        self.gest_article=Button(self.MenuContainer,text='ARTICLES', command=self.save)
        self.gest_article.place(x=20,y=80, width=190,height=40)

        self.gest_Clients=Button(self.MenuContainer,text='CLIENTS', command=self.save)
        self.gest_Clients.place(x=20,y=140, width=190,height=40)

        self.gest_Clients=Button(self.MenuContainer,text='FACTURE', command=self.save)
        self.gest_Clients.place(x=20,y=200, width=190,height=40)

        self.gest_Clients=Button(self.MenuContainer,text='PAIEMENT', command=self.save, bg='white',fg='#51a596')
        self.gest_Clients.place(x=20,y=260, width=190,height=40)

        self.gest_Clients=Button(self.MenuContainer,text='RAPPORT', command=self.save)
        self.gest_Clients.place(x=20,y=320, width=190,height=40)


        #Conteneur des elements de chaque section
        self.ContainerRight=Frame(self.fen,height=900,width=760)
        self.ContainerRight.place(x=250,y=20)
        self.titresection = Label(self.ContainerRight, text = "Gestion des articles", font = "Arial 15 bold").place(x=0, y=0)

  
        # conteneur des elements de la section article (boutton )
        self.ContainerArticle=Frame(self.ContainerRight,height=900,width=760)
        self.ContainerArticle.place(x=0,y=40)
        self.titresection = Label(self.ContainerArticle, text = "Rapport des articles", font = "Arial 15 bold").place(x=0, y=0)
        # btn pour afficher le rapport des articles en pdf
        self.btn_article=Button(self.ContainerArticle,text='Rapport des articles', command=self.rapport_article)
        self.btn_article.place(x=20,y=40, width=190,height=40)
        # btn pour afficher le rapport des ventes en pdf
        self.btn_vente=Button(self.ContainerArticle,text='Rapport des ventes', command=self.rapport_vente)
        self.btn_vente.place(x=20,y=100, width=190,height=40)
        # btn pour afficher le rapport des paiements en pdf
        self.btn_paiement=Button(self.ContainerArticle,text='Rapport des paiements', command=self.rapport_paiement)
        self.btn_paiement.place(x=20,y=160, width=190,height=40)
        # btn pour afficher le rapport des factures en pdf
        self.btn_facture=Button(self.ContainerArticle,text='Rapport des factures', command=self.rapport_facture)
        self.btn_facture.place(x=20,y=220, width=190,height=40)
        # btn pour afficher le rapport des clients en pdf
        self.btn_client=Button(self.ContainerArticle,text='Rapport des clients', command=self.rapport_client)
        self.btn_client.place(x=20,y=280, width=190,height=40)

    def fenetre(self):
        self.fen
    def save(self):
        pass
    def rapport_article(self):
        article= ArticleBackend("test","eye",10)
        data = article.all(self.curseur)
        genereRapportArticle(data)

      
        # ouverture du fichier pdf avec tout les paths
        webbrowser.open_new(r'rapport_articles.pdf')

    def rapport_vente(self):
        # creation du fichier pdf
        f=open('rapport_vente.pdf','w')
        f.write('Rapport des ventes')
        f.close()
        # ouverture du fichier pdf
        webbrowser.open_new(r'rapport_vente.pdf')
    def rapport_paiement(self):
        rapportBac = RapportBackend()
        data = rapportBac.afficherPaiementVenteArticle(self.curseur)
        genererRapportPaiement(data)
        # ouverture du fichier pdf
        webbrowser.open_new(r'rapport_paiement.pdf')
    def rapport_facture(self):
        rapportback = RapportBackend()
        data = rapportback.afficherFactureClient(self.curseur)
        generateRapportFacture(data)

        # ouverture du fichier pdf
        webbrowser.open_new(r'rapport_facture.pdf')
    def rapport_client(self):
        rapportBac = RapportBackend()
        data = rapportBac.afficherClient(self.curseur)
        generateRapportCustomer(data)

        # generate rapport
       

        
        # ouverture du fichier pdf
        webbrowser.open_new(r'rapport_clients.pdf')
    



       