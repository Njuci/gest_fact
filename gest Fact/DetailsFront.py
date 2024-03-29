from tkinter import *
from tkinter.messagebox import showerror,showinfo
from connexion import DetailsBackend
from tkinter import ttk


from reportlab.lib.pagesizes import letter
from reportlab.platypus import Table, TableStyle, SimpleDocTemplate
from reportlab.platypus import Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
import datetime


class DetailsFrontend:
    def __init__(self,Curseur,InfosFacture):

        self.fen = Tk()
        self.fen.title("GESTION DE LA FACTURATION")
        self.fen.geometry("800x600")
        self.InfosFacture=InfosFacture
        self.IdentifiantArticle=""
        #Creation du conteneur menu et ses elements
        self.MenuContainer=Frame(self.fen,height=800,width=230,bg='#51a596')
        self.MenuContainer.place(x=0,y=0)
        self.titre = Label(self.MenuContainer, text = "GEST - FACT", font = "Arial 15 bold",bg='#51a596',fg='white').place(x=30, y=20)

        self.gest_article=Button(self.MenuContainer,text='ARTICLES')
        self.gest_article.place(x=20,y=80, width=190,height=40)

        self.gest_Clients=Button(self.MenuContainer,text='CLIENTS')
        self.gest_Clients.place(x=20,y=140, width=190,height=40)

        self.gest_Clients=Button(self.MenuContainer,text='FACTURE')
        self.gest_Clients.place(x=20,y=200, width=190,height=40)

        self.gest_Clients=Button(self.MenuContainer,text='PAIEMENT')
        self.gest_Clients.place(x=20,y=260, width=190,height=40)

        self.gest_Clients=Button(self.MenuContainer,text='RAPPORT')
        self.gest_Clients.place(x=20,y=320, width=190,height=40)


        #Conteneur des elements de chaque section
        self.ContainerRight=Frame(self.fen,height=800,width=760)
        self.ContainerRight.place(x=250,y=20)
        self.titresection = Label(self.ContainerRight, text = "Details Facture", font = "Arial 15 bold").place(x=0, y=0)

        # Creation du formulaire et les actions 
        self.HeaderContainer=Frame(self.ContainerRight,height=270,width=780,bg='gray')
        self.HeaderContainer.place(x=0,y=50)

        self.form=Frame(self.HeaderContainer,height=320,width=450,bg='gray')
        self.form.place(x=0,y=0)


        #Les elements de conteneur action
        self.Actions=Frame(self.HeaderContainer,height=320,width=200,bg='gray')
        self.Actions.place(x=430,y=20)

        #les actions sur le formulaire
        self.ajouter_btn= Button(self.Actions,bg='#51a596',text='Ajouter',fg='white',command=self.save)
        self.ajouter_btn.place(x=0,y=20, width=120,height=40)
        self.modifier_btn= Button(self.Actions,bg='#51a596',text='Modifier',fg='white', command=self.Update)
        self.modifier_btn.place(x=0,y=70, width=120,height=40)
        self.Supprimer_btn= Button(self.Actions,bg='brown',text='Supprimer',fg='white')
        self.Supprimer_btn.place(x=0,y=120, width=120,height=40)

        self.pdf= Button(self.Actions,bg='red',text='PDF',fg='white')
        self.pdf.place(x=0,y=180, width=120,height=40)

        self.IdLab = Label(self.form, text='Code Facture',bg='gray',fg='white',font='20')
        self.IdLab.place(x=20,y=50, height=30)
        self.DateLab = Label(self.form, text='Nom Client',bg='gray',fg='white',font='20')
        self.DateLab.place(x=20,y=100, height=30)

        self.IdLab = Label(self.form, text='Code Facture',bg='gray',fg='white',font='20')
        self.IdLab.place(x=20,y=50, height=30)
        self.DateLab = Label(self.form, text='Nom Client',bg='gray',fg='white',font='20')
        self.DateLab.place(x=20,y=100, height=30)

        self.IdFactLab = Label(self.form, text=self.InfosFacture[0],bg='gray',fg='white',font='20')
        self.IdFactLab.place(x=150,y=50, height=30)
        self.NomClientLab = Label(self.form, text=self.InfosFacture[3],bg='gray',fg='white',font='20')
        self.NomClientLab.place(x=150,y=100, height=30)

        self.ReduLab = Label(self.form, text='Code Article',bg='gray',fg='white',font='20')
        self.ReduLab.place(x=20,y=150, height=30)
        self.IdCliLab = Label(self.form, text='Quantite',bg='gray',fg='white',font='20')
        self.IdCliLab.place(x=20,y=200, height=30)
        
     

        self.QuantEnt=Entry(self.form)
        self.QuantEnt.place(x=150,y=200,width=250, height=30)
        
        #Creation de la section de tableau
        self.TabSection=Frame(self.ContainerRight,height=250,width=580,bg='blue')
        self.TabSection.place(x=0,y=330)

        #Creation du tableau
        self.tableau=ttk.Treeview(self.TabSection, columns=('IdArt','Nom','Quantite','Prix','PrixTotal'), show='headings')
        self.tableau.heading('IdArt', text='Id Article')
        self.tableau.heading('Nom', text='Nom Article')
        self.tableau.heading('Quantite', text='Quant')
        self.tableau.heading('Prix', text='PU')
        self.tableau.heading('PrixTotal', text='PT')

        self.tableau.column('IdArt',width=100,anchor='center')
        self.tableau.column('Quantite',width=100,anchor='center')
        self.tableau.column('Prix',width=100,anchor='center')
        self.tableau.column('PrixTotal',width=100,anchor='center')


        #Ajouts des elements dans le tableau 

        self.curseur=Curseur
        self.DataDetails=DetailsBackend(self.InfosFacture[0],self.IdentifiantArticle,self.QuantEnt.get())
        Data =  self.DataDetails.getdataArticle(self.curseur)
        option=[]
        for i, row in enumerate(Data):
             option.append(row[0])
        self.CodeArtEnt=ttk.Combobox(self.form,values=option)
        self.CodeArtEnt.place(x=150,y=150,width=250, height=30)
        self.CodeArtEnt.bind("<<ComboboxSelected>>",self.selectCombo)

        Data =  self.DataDetails.getDetails(self.curseur)
        for i, row in enumerate(Data):
            self.tableau.insert('','end',values=(row[3],row[0],row[2],row[1],row[1]*row[2]))

        self.tableau.bind('<Double-Button-1>',self.GetValue)
        self.tableau.pack()

    # La fonction de reinitialisationde champ
    def Actualiser(self):
        Data = self.DataDetails.getDetails(self.curseur)
        for record in self.tableau.get_children():
            self.tableau.delete(record)
        for i, row in enumerate(Data):
            self.tableau.insert('','end',values=(row[3],row[0],row[2],row[1],row[1]*row[2]))
        self.tableau.pack()

    def selectCombo (self,event):
        self.IdentifiantArticle=self.CodeArtEnt.get()
        
    def ReseteInput(self):
        self.QuantEnt.delete(0,END)

    def GetValue(self,event):
        self.ReseteInput()
        row_id=self.tableau.selection()[0]
        select = self.tableau.set(row_id)
        self.QuantEnt.insert(0,select['Quantite'])
        self.CodeArtEnt.insert(0,select['IdArt'])

    def Update (self):
        self.DataDetails=DetailsBackend(self.InfosFacture[0],self.IdentifiantArticle,self.QuantEnt.get())
        self.DataDetails.UpdateData(self.curseur)
        self.Actualiser()
        self.ReseteInput()
    def save(self):
        self.selectCombo
        self.DataDetails=DetailsBackend(self.InfosFacture[0],self.IdentifiantArticle,self.QuantEnt.get())
        self.DataDetails.save(self.curseur)
        self.Actualiser()
        self.ReseteInput()
 
    def fenetre (self):
        return self.fen