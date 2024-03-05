from tkinter import *
from tkinter.messagebox import showerror,showinfo
from tkinter import ttk
from DetailsFront import DetailsFrontend
import datetime
from connexion import FactBackend

class FactureFrontend:
    def __init__(self,Curseur):
        self.curseur=Curseur
        self.fen = Tk()
        self.fen.title("GESTION DE LA FACTURATION")
        self.fen.geometry("800x600")
        #Creation du conteneur menu et ses elements
        self.MenuContainer=Frame(self.fen,height=800,width=230,bg='#51a596')
        self.MenuContainer.place(x=0,y=0)
        self.titre = Label(self.MenuContainer, text = "GEST - FACT", font = "Arial 15 bold",bg='#51a596',fg='white').place(x=30, y=20)

        self.gest_article=Button(self.MenuContainer,text='ARTICLES')
        self.gest_article.place(x=20,y=80, width=190,height=40)

        self.gest_Clients=Button(self.MenuContainer,text='CLIENTS')
        self.gest_Clients.place(x=20,y=140, width=190,height=40)
        self.NomClient =""

        self.gest_Clients=Button(self.MenuContainer,text='FACTURE')
        self.gest_Clients.place(x=20,y=200, width=190,height=40)

        self.gest_Clients=Button(self.MenuContainer,text='PAIEMENT')
        self.gest_Clients.place(x=20,y=260, width=190,height=40)

        self.gest_Clients=Button(self.MenuContainer,text='RAPPORT')
        self.gest_Clients.place(x=20,y=320, width=190,height=40)


        #Conteneur des elements de chaque section
        self.ContainerRight=Frame(self.fen,height=800,width=760)
        self.ContainerRight.place(x=250,y=20)
        self.titresection = Label(self.ContainerRight, text = "Gestion des Factures", font = "Arial 15 bold").place(x=0, y=0)

        # Creation du formulaire et les actions 
        self.HeaderContainer=Frame(self.ContainerRight,height=270,width=600,bg='gray')
        self.HeaderContainer.place(x=0,y=50)

        self.form=Frame(self.HeaderContainer,height=320,width=450,bg='gray')
        self.form.place(x=0,y=0)

        #Les elements de conteneur action
        self.Actions=Frame(self.HeaderContainer,height=320,width=200,bg='gray')
        self.Actions.place(x=430,y=20)
        #les actions sur le formulaire
        self.ajouter_btn= Button(self.Actions,bg='#51a596',text='Ajouter',fg='white',command=self.ajouter_fact)
        self.ajouter_btn.place(x=0,y=20, width=120,height=40)
        self.modifier_btn= Button(self.Actions,bg='#51a596',text='Modifier',fg='white', command=self.Update)
        self.modifier_btn.place(x=0,y=70, width=120,height=40)
        self.Supprimer_btn= Button(self.Actions,bg='brown',text='Supprimer',fg='white')
        self.Supprimer_btn.place(x=0,y=120, width=120,height=40)

        self.Details_btn= Button(self.Actions,bg='#51a596',text='Details',fg='white',command=self.AjoutsDetails)
        self.Details_btn.place(x=0,y=180, width=120,height=40)

        self.IdLab = Label(self.form, text='Identifiant',bg='gray',fg='white',font='20')
        self.IdLab.place(x=20,y=50, height=30)
        self.DateLab = Label(self.form, text='Date facture',bg='gray',fg='white',font='20')
        self.DateLab.place(x=20,y=100, height=30)
        self.ReduLab = Label(self.form, text='Reduction',bg='gray',fg='white',font='20')
        self.ReduLab.place(x=20,y=150, height=30)
        self.IdCliLab = Label(self.form, text='ID CLIENT',bg='gray',fg='white',font='20')
        self.IdCliLab.place(x=20,y=200, height=30)
        
        self.idFacEnt=Entry(self.form)
        self.idFacEnt.place(x=150,y=50,width=250, height=30)
        self.DateEnt=Entry(self.form)
        self.DateEnt.place(x=150,y=100,width=250, height=30)
        self.RedEnt=Entry(self.form)
        self.RedEnt.place(x=150,y=150,width=250, height=30)
        self.IdCliEnt=Entry(self.form)
        self.IdCliEnt.place(x=150,y=200,width=250, height=30)
        self.Facture=FactBackend("","","","")
        
        #Creation de la section de tableau
        self.TabSection=Frame(self.ContainerRight,height=250,width=580,bg='blue')
        self.TabSection.place(x=0,y=330)

        #Creation du tableau
        self.tableau=ttk.Treeview(self.TabSection, columns=('IdFac','Date','Reduction','NomCli','IdCli'), show='headings')
        self.tableau.heading('IdFac', text='Id Facture')
        self.tableau.heading('Date', text='Date')
        self.tableau.heading('Reduction',text='Reduction')
        self.tableau.heading('NomCli', text='Nom Client')
        self.tableau.heading('IdCli', text='Id Client')


        #Ajouts des elements dans le tableau 

        
        self.Facture=FactBackend(self.idFacEnt.get(),self.DateEnt.get(),self.RedEnt.get(),self.IdCliEnt.get())
        Data =  self.Facture.getData(self.curseur)
        print(Data)
        for i, row in enumerate(Data):
            self.tableau.insert('','end',values=(row[0],row[1],row[2],row[4],row[3]))
        self.tableau.bind('<Double-Button-1>',self.GetValue)
        self.tableau.column('IdFac',width=100,anchor='center')
        self.tableau.column('Date',width=100,anchor='center')
        self.tableau.column('IdCli',width=100,anchor='center')
        self.tableau.column('Reduction',width=100,anchor='center')
        self.tableau.pack()

    def ReseteInput(self):
        self.idFacEnt.delete(0,END)
        self.DateEnt.delete(0,END)
        self.RedEnt.delete(0,END)
        self.IdCliEnt.delete(0,END)

    # La fonction de recuperation de donnees apres chaque double clic dans le tableau
    def GetValue(self,event):
        self.ReseteInput()
        row_id=self.tableau.selection()[0]
        select = self.tableau.set(row_id)
        self.idFacEnt.insert(0,select['IdFac'])
        self.DateEnt.insert(0,select['Date'])
        self.RedEnt.insert(0,select['Reduction'])
        self.IdCliEnt.insert(0,select['IdCli'])
        self.NomClient=select['NomCli']

    def Actualiser(self):
        Data = self.Facture.getData(self.curseur)
        # suppression des elements du tableau
        for record in self.tableau.get_children():
            self.tableau.delete(record)
        for i, row in enumerate(Data):
            self.tableau.insert('','end',values=(row[0],row[1],row[2],row[4],row[3]))
        self.tableau.pack()

    def Update (self):
        self.Facture=FactBackend(self.idFacEnt.get(),self.DateEnt.get(),self.RedEnt.get(),self.IdCliEnt.get())
        self.Facture.UpdateData(self.curseur)
        self.ReseteInput()
        self.Actualiser()
    """ajouter une facture"""
    def ajouter_fact(self):
        fac=FactBackend(self.idFacEnt.get(),self.DateEnt.get(),self.RedEnt.get(),self.IdCliEnt.get())
        if fac.save(self.curseur):
            showinfo("Gest Fact","Facture Enrégistré")
        self.ReseteInput()
        self.Actualiser()
        


  
    def AjoutsDetails (self):
        if self.idFacEnt.get()=='' and self.DateEnt.get()=='' and self.RedEnt.get()=='':
            showerror('Gest Fact','Veuillez selectionner la facture')
        else:
            Details=DetailsFrontend(self.curseur,[self.idFacEnt.get(),self.DateEnt.get(),self.RedEnt.get(),self.NomClient])
            self.fen.destroy()
            Details.fenetre().mainloop()
    # La fonction de reinitialisationde champ
   
    def fenetre (self):
        return self.fen