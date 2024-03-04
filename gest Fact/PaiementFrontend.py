from tkinter import *
from tkinter.messagebox import showinfo
from articlebackend import ArticleBackend
from connexion import FactureBackend
from PaiementBackend import PaiementBackend
from connexion import VenteBackend
from tkinter import ttk
import webbrowser 
from tkcalendar import DateEntry
import datetime


class PaiementFrontend:
    def __init__(self,curseur):
        self.curseur=curseur
        self.fen = Tk()
        self.fen.title("GESTION DE LA FACTURATION")
        self.fen.geometry("1000x600")
        self.sel = StringVar()
        self.montantRestant = float
        
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

        # Creation du formulaire et les actions 
        self.HeaderContainer=Frame(self.ContainerRight,height=200,width=580,bg='gray')
        self.HeaderContainer.place(x=0,y=50)





        self.form=Frame(self.HeaderContainer,height=320,width=450,bg='gray')
        self.form.place(x=0,y=0)

        #Les elements de conteneur action
        self.Actions=Frame(self.HeaderContainer,height=320,width=200,bg='gray')
        self.Actions.place(x=430,y=20)
        #les actions sur le formulaire
        self.ajouter_btn= Button(self.Actions,bg='#51a596',text='Ajouter',fg='white', command=self.enregistrer_paiement)
        self.ajouter_btn.place(x=0,y=20, width=120,height=40)
        self.modifier_btn= Button(self.Actions,bg='#51a596',text='Modifier',fg='white', command=self.modifier_article)
        self.modifier_btn.place(x=0,y=70, width=120,height=40)
        self.Supprimer_btn= Button(self.Actions,bg='brown',text='Supprimer',fg='white', command=self.supprimer_paiement)
        self.Supprimer_btn.place(x=0,y=120, width=120,height=40)

        # Creation des elements du formulaire de paiement
        # create table Paiement(
        # datepaie date,
        # idfact varchar(5),
        # montant float(12,2),
        # constraint pk_p_fact foreign key(idFact) References Facture(idFact)

        # adding the date of payment 
        self.dateLab = Label(self.form, text='Date de Paiement',bg='gray',fg='white',font='18')
        self.dateLab.place(x=20,y=50, height=30)
        self.dateEnt=DateEntry(self.form,selectmode='day',textvariable=self.sel)
        self.dateEnt.place(x=200,y=50,width=120, height=30)
        # adding the id of the invoice as combobox
        self.idLab = Label(self.form, text='Id Facture',bg='gray',fg='white',font='18')
        self.idLab.place(x=20,y=100, height=30)
       
        # combobox valu coming from idFact in the database
        self.idEnt=ttk.Combobox(self.form,values=self.get_facture(),state='readonly')
        self.idEnt.place(x=200,y=100,width=100, height=30)
        # label for paiement amount
        self.textPaiment = Label(self.form, text='Paiement',bg='gray',fg='white',font='18')
        self.textPaiment.place(x=320,y=100, height=30)
        self.idEnt.bind('<<ComboboxSelected>>',self.combo_Changed)
        # adding the amount of the payment
        self.montantLab = Label(self.form, text='Montant',bg='gray',fg='white',font='18')
        self.montantLab.place(x=20,y=150, height=30)
        self.montantEnt=Entry(self.form)
        self.montantEnt.place(x=200,y=150,width=120, height=30)
        # adding the buttons for the actions
        self.PdfSection=Frame(self.ContainerRight,height=50,width=580)
        self.PdfSection.place(x=0,y=270)

        
        # self.CodeEnt=Entry(self.form)
        # self.CodeEnt.place(x=150,y=50,width=250, height=30)
        # self.desiEnt=Entry(self.form)
        # self.desiEnt.place(x=150,y=100,width=250, height=30)
        # self.prixEnt=Entry(self.form)
        # self.prixEnt.place(x=150,y=150,width=250, height=30)
        
        


        self.PdfSection=Frame(self.ContainerRight,height=50,width=580)
        self.PdfSection.place(x=0,y=270)


        self.visualiser_btn= Button(self.PdfSection,bg='#51a596',text='Visualiser',fg='white', command=self.open_file)
        self.visualiser_btn.place(x=0,y=10, width=120,height=40)

        self.generer_btn= Button(self.PdfSection,bg='#51a596',text='Generer',fg='white', command=self.save)
        self.generer_btn.place(x=150,y=10, width=120,height=40)

        self.TabSection=Frame(self.ContainerRight,height=550,width=580,bg='blue')
        self.TabSection.place(x=0,y=330)
        #Creation du tableau
        self.tableau=ttk.Treeview(self.TabSection, columns=('Facture','Date','Montant payé'), show='headings')
        self.tableau.heading('Facture', text='Facture')
        self.tableau.heading('Date', text='Date')
        self.tableau.heading('Montant payé', text='Montant payé')
     
        self.date_paiement = None
        self.id_facture = None
        self.montant_paiement = None

        #Ajouts des elements dans le tableau
        self.afficher()


        self.tableau.pack()
    def open_file(self):
        webbrowser.open("pdf")
    def get_entry(self):
        # get the values of the entry fields for payment
        self.date_paiement=self.dateEnt.get()
        self.id_facture=self.idEnt.get()
        self.montant_paiement=self.montantEnt.get()

     #Creation de la section de tableau   
    def get_table_selected_row(self,event):        
        self.clean_entry()
        row=self.tableau.selection()[0]
        elemen_selected=self.tableau.set(row)
        self.dateEnt.insert(0,elemen_selected['Date'])
        self.idEnt.set(elemen_selected['Facture'])
        self.montantEnt.insert(0,elemen_selected['Montant payé'])
        self.get_entry()
    
    # chercher liste des factures dans la base de données
    def get_facture(self):
        # fetch all the invoices from the database
        facture=FactureBackend(idFact="1",dateFact="2021-05-12",idClient="1")
        factures = facture.allFacture(self.curseur)
        print(factures)
        # return only the idFact from the list of invoices
        return [f[0] for f in factures]

    def enregistrer_paiement(self):
        # print(self.dateEnt.get(),self.idEnt.get(),self.montantEnt.get())
        if self.montantRestant < float(self.montantEnt.get()):
            showinfo("Facturation System","Le montant du paiement est superieur au montant restant")
            self.montantEnt.delete(0,END)
            return
        # test for empty fields
        if self.dateEnt.get() == "" or self.idEnt.get() == "" or self.montantEnt.get() == "":
            showinfo("Facturation System","Veuillez remplir tous les champs")
            return
        # format the date to the right format DD-MM-YYYY to YYYY-MM-DD HH:MM:SS
        # get current date
        date = datetime.datetime.now()
    
       
   
        paiement=PaiementBackend(date,self.idEnt.get(),self.montantEnt.get())
        if paiement.savePaiement(self.curseur):
            showinfo("Facturation System","Paiement Enregistré")
            # clear the entry after saving the payment
            self.dateEnt.delete(0,END)
            self.idEnt.delete(0,END)
            self.montantEnt.delete(0,END)
            self.getMontant()
            self.afficher()

            # self.afficher()
            # self.tableau.pack()
            self.clean_entry()
    def combo_Changed(self,event):
        self.getMontant()
        

    def getMontant(self):
        vente = VenteBackend(idFact=self.idEnt.get(),codArt="1",quantite=2)
        ventes = vente.allVente(self.curseur)
        # get all the articles price sold in the invoice
        prix = 0
        for v in ventes:
            print(v)
            articles = ArticleBackend(cod=v[0],desi="test",prix=2)
            article = articles.search(self.curseur)
            prix += article[0][2]*v[2]
        #get all payment made for the invoice
        paiement = PaiementBackend(date="2021-05-12",idfact=self.idEnt.get(),montant=2)
        paiements = paiement.searchPaiement(self.curseur)
        montant = 0
        for p in paiements:
            montant += p[2]
        # get the amount left to be paid
        print(prix,montant)
        self.textPaiment.config(text="Reste: "+str(prix-montant) + " $")
        self.montantRestant = prix-montant

    """modifier un paiement"""
    def modifier_article(self):
        date = datetime.datetime.now()
        paiement=PaiementBackend(self.dateEnt.get(),self.idEnt.get(),self.montantEnt.get())
        if paiement.updatePaiement(self.curseur,[date,self.id_facture,self.montant_paiement]):
            showinfo("Facturation System","Paiement Modifié")
            self.afficher()
            # self.tableau.pack()
            self.clean_entry()
    # supprimer un paiement
    def supprimer_paiement(self):
        paiement=PaiementBackend(self.dateEnt.get(),self.idEnt.get(),self.montantEnt.get())
        if paiement.deletePaiement(self.curseur):
            # show a message after deleting the payment
            showinfo("Facturation System","Paiement Supprimé")
            self.afficher()
            self.clean_entry()
        # else:
        #     showinfo("Facturation System","Paiement non Supprimé")

    """afficher les paiments"""
    def afficher(self):
        a= PaiementBackend(date="2021-05-12",idfact="1",montant=2)
        data=a.allPaiement(self.curseur)
        for record in self.tableau.get_children():
            self.tableau.delete(record)
        for i, row in enumerate(data):
            self.tableau.insert('','end',values=(row[1],row[0],row[2]))
        self.tableau.bind('<Double-Button-1>',self.get_table_selected_row)
        
    def clean_entry(self):
        self.dateEnt.delete(0,END)
        self.idEnt.set("")
        self.montantEnt.delete(0,END)  
    def ajouter_article (self):
        ajout=ArticleBackend(self.CodeEnt.get(),self.desiEnt.get(),self.prixEnt.get())
        ajout.save(self.curseur)
        self.clean_entry()
        self.afficher()
        self.tableau.pack()
    def save(self):
        pass
    def fenetre (self):
        return self.fen
    

