from tkinter import *
from tkinter.messagebox import showinfo,showerror
from connexion import ArticleBackend
from report import generate_pdf
from FactureFront import FactureFrontend
from tkinter import ttk
import webbrowser 
import datetime
from ClientBackend import ClientBackend 

#from PaiementFrontend import PaiementFrontend
#from RapportFontend import RapportFrontend
class ClientFrontend:
    def __init__(self,curseur):
        self.curseur=curseur
        self.fen = Tk()
        self.fen.title("GESTION DE LA FACTURATION")
        self.fen.geometry("800x600")

        # self.sidebar=Sidebar(self.fen,self.curseur)
        # self.sidebar.place(0,0)
        
        #Creation du conteneur menu et ses elements
        self.MenuContainer=Frame(self.fen,height=800,width=230,bg='#51a596')
        self.MenuContainer.place(x=0,y=0)
        self.titre = Label(self.MenuContainer, text = "GEST - FACT", font = "Arial 15 bold",bg='#51a596',fg='white').place(x=30, y=20)

        self.gest_article=Button(self.MenuContainer,text='ARTICLES', command=self.save)
        self.gest_article.place(x=20,y=80, width=190,height=40)

        self.gest_Clients=Button(self.MenuContainer,text='CLIENTS', command=self.save)
        self.gest_Clients.place(x=20,y=140, width=190,height=40)

        self.gest_Clients=Button(self.MenuContainer,text='FACTURE', command=self.call_facture)
        self.gest_Clients.place(x=20,y=200, width=190,height=40)

        self.gest_Clients=Button(self.MenuContainer,text='PAIEMENT', command=self.save)
        self.gest_Clients.place(x=20,y=260, width=190,height=40)

        self.gest_Clients=Button(self.MenuContainer,text='RAPPORT', command=self.save)
        self.gest_Clients.place(x=20,y=320, width=190,height=40)


        #Conteneur des elements de chaque section
        self.ContainerRight=Frame(self.fen,height=900,width=760)
        self.ContainerRight.place(x=250,y=20)
        self.titresection = Label(self.ContainerRight, text = "Gestion clients", font = "Arial 15 bold").place(x=0, y=0)

        # Creation du formulaire et les actions 
        self.HeaderContainer=Frame(self.ContainerRight,height=200,width=580,bg='gray')
        self.HeaderContainer.place(x=0,y=50)

        self.form=Frame(self.HeaderContainer,height=490,width=450,bg='gray')
        self.form.place(x=0,y=0)
 
        #Les elements de conteneur action
        self.Actions=Frame(self.HeaderContainer,height=320,width=200,bg='gray')
        self.Actions.place(x=430,y=20)
        #les actions sur le formulaire
        self.ajouter_btn= Button(self.Actions,bg='#51a596',text='Ajouter',fg='white', command=self.ajouter_client)
        self.ajouter_btn.place(x=0,y=20, width=120,height=40)
        self.modifier_btn= Button(self.Actions,bg='#51a596',text='Modifier',fg='white', command=self.modifier_client)
        self.modifier_btn.place(x=0,y=70, width=120,height=40)
        self.Supprimer_btn= Button(self.Actions,bg='brown',text='Supprimer',fg='white', command=self.supprimer_client)
        self.Supprimer_btn.place(x=0,y=120, width=120,height=40)

        self.IdLab = Label(self.form, text='Id Client',bg='gray',fg='white',font='20')
        self.IdLab.place(x=20,y=50, height=30)
        self.NomLab = Label(self.form, text='Nom client',bg='gray',fg='white',font='20')
        self.NomLab.place(x=20,y=100, height=30)
        self.AdressLab = Label(self.form, text='Adresse client',bg='gray',fg='white',font='20')
        self.AdressLab.place(x=20,y=150, height=30)
        self.NumeroLab = Label(self.form, text='Numéro ',bg='gray',fg='white',font='20')
        self.NumeroLab.place(x=20,y=180, height=30)
        
        self.IdEnt=Entry(self.form)
        self.IdEnt.place(x=150,y=50,width=250, height=30)
        self.NomEnt=Entry(self.form)
        self.NomEnt.place(x=150,y=100,width=250, height=30)
        self.AdressEnt=Entry(self.form)
        self.AdressEnt.place(x=150,y=150,width=250, height=30)
        self.NumeroEnt=Entry(self.form)
        self.NumeroEnt.place(x=150,y=180,width=250, height=30)

        self.TabSection=Frame(self.ContainerRight,height=550,width=580,bg='blue')
        self.TabSection.place(x=0,y=330)
        #Creation du tableau
        self.tableau=ttk.Treeview(self.TabSection, columns=('Code','Nom client','Adresse','Numéro'), show='headings')
        self.tableau.heading('Code', text='Code')
        self.tableau.heading('Nom client', text='Nom client')
        self.tableau.heading('Adresse', text='Adresse')
        self.tableau.heading('Numéro', text='Numéro')
        self.valeur_id_client=None
        self.valeur_nom_client=None
        self.valeur_adress_client=None
        self.valeur_numero_client=None

        #Ajouts des elements dans le tableau
        self.afficher()


        self.tableau.pack()

    def get_entry(self):
        self.valeur_id_client=self.IdEnt.get()
        self.valeur_nom_client=self.NomEnt.get()
        self.valeur_adress_client=self.AdressEnt.get()
        self.valeur_numero_client=self.NumeroEnt.get()

     #Creation de la section de tableau   
    def get_table_selected_row(self,event):        
        self.clean_entry()
        row=self.tableau.selection()[0]
        self.elemen_selected=self.tableau.set(row)
        self.IdEnt.insert(0,self.elemen_selected['Code'])
        self.NomEnt.insert(0,self.elemen_selected['Nom client'])
        self.AdressEnt.insert(0,self.elemen_selected['Adresse'])
        self.NumeroEnt.insert(0,self.elemen_selected['Numéro'])
        self.get_entry()
    """modifier un client"""
    def modifier_client(self):
        if self.valeur_id_client is  not None:
            self.get_entry()
        print(self.IdEnt.get(),self.NomEnt.get(),self.AdressEnt.get(),self.NumeroEnt.get())
        client=ClientBackend(self.curseur)
        if client.updateClient(self.IdEnt.get(),self.NomEnt.get(),self.AdressEnt.get(),self.NumeroEnt.get()):
            showinfo("Gest Fact","Client Modifié")
            self.clean_entry()
            self.afficher()
            
        
    """supprimer un client"""
    def supprimer_client(self):
        client=ClientBackend(self.curseur)
        print(self.IdEnt.get())
        if client.deleteClient(clientId=self.IdEnt.get()):
            showinfo("Gest Fact","Client Supprimé")
            self.afficher()
            self.clean_entry()
    """afficher les clients"""
    def afficher(self):
        a = ClientBackend(self.curseur)
        data=a.allClients()
        if data is not None:
            for record in self.tableau.get_children():
                self.tableau.delete(record)
            for i, row in enumerate(data):
                self.tableau.insert('','end',values=(row[0],row[1],row[2]))
            self.tableau.bind('<Double-Button-1>',self.get_table_selected_row)
    def clear_selected_value(self):
        self.valeur_code_art=None
        self.valeur_designation=None
        self.valeur_prix=None

    def clean_entry(self):
        self.IdEnt.delete(0,END)
        self.NomEnt.delete(0,END)
        self.AdressEnt.delete(0,END)
        self.NumeroEnt.delete(0,END) 
    def ajouter_client (self):
        ajout=ClientBackend(self.curseur)
        if ajout.addClient(self.IdEnt.get(),self.NomEnt.get(),self.AdressEnt.get(),self.NumeroEnt.get()):
            showinfo("Gest Fact","Client Enrégistré")
            self.clean_entry()
            self.afficher()
            # self.tableau.pack()
    def save(self):
        pass
    def call_facture(self):
        facture=FactureFrontend(self.curseur)
        facture.fenetre().mainloop()
        self.fen.destroy()
    def fenetre (self):
        return self.fen
    """    def ouvri_paiement(self):
        paiement = PaiementFrontend(self.curseur)
        self.fen.destroy()
        paiement.fenetre().mainloop()
    def ouvrir_rapport(self):
        rapport = RapportFrontend(self.curseur)
        self.fen.destroy()
        rapport.fenetre().mainloop()
        """
# Path: gest%20Fact/connexion.py
