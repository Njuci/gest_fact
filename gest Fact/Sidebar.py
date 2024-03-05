from tkinter import Frame, Label, Button
from FactureFront import FactureFrontend
from PaiementFrontend import PaiementFrontend
from RapportFontend import RapportFrontend
from ClientFronted import ClientFrontend

class Sidebar:
    def __init__(self, fen,cursor=None):
        self.fen = fen
        self.curseur = cursor
        self.MenuContainer = Frame(self.fen, height=800, width=230, bg='#51a596')
        self.MenuContainer.place(x=0, y=0)
        self.titre = Label(self.MenuContainer, text="GEST - FACT", font="Arial 15 bold", bg='#51a596', fg='white')
        self.titre.place(x=30, y=20)

        self.gest_article = Button(self.MenuContainer, text='ARTICLES', command=self.open_article)
        self.gest_article.place(x=20, y=80, width=190, height=40)

        self.gest_Clients = Button(self.MenuContainer, text='CLIENTS', command=self.open_client)
        self.gest_Clients.place(x=20, y=140, width=190, height=40)

        self.gest_Clients = Button(self.MenuContainer, text='FACTURE', command=self.open_facture)
        self.gest_Clients.place(x=20, y=200, width=190, height=40)

        self.gest_Clients = Button(self.MenuContainer, text='PAIEMENT', command=self.open_paiement)
        self.gest_Clients.place(x=20, y=260, width=190, height=40)

        self.gest_Clients = Button(self.MenuContainer, text='RAPPORT', command=self.open_rapport)
        self.gest_Clients.place(x=20, y=320, width=190, height=40)
    def place(self, x, y):
        self.MenuContainer.place(x=x, y=y)
    def open_article(self):
        # article = ArticleFrontend(self.master)
        self.fen.destroy()
        # article.fenetre.mainloop()
    def open_facture(self):
        facture = FactureFrontend(self.curseur)
        # self.fen.destroy()
        facture.fenetre.mainloop()
    
    def open_paiement(self):
        paiement = PaiementFrontend(self.curseur)
        # self.fen.destroy()
        paiement.fenetre.mainloop()
    def open_rapport(self):
        rapport = RapportFrontend(self.curseur)
        # self.fen.destroy()
        rapport.fenetre.mainloop()
    def open_client(self):
        client = ClientFrontend(self.curseur)
        # self.fen.destroy()
        client.fenetre.mainloop()
    