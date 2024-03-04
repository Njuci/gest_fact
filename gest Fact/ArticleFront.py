from tkinter import *
from tkinter.messagebox import showinfo
from articlebackend import ArticleBackend
from tkinter import ttk
import webbrowser 
from PaiementFrontend import PaiementFrontend
from RapportFontend import RapportFrontend
from FactureFront import FactureFrontend
class ArticleFrontend:
    def __init__(self,curseur):
        self.curseur=curseur
        self.fen = Tk()
        self.fen.title("GESTION DE LA FACTURATION")
        self.fen.geometry("800x600")
        
        #Creation du conteneur menu et ses elements
        self.MenuContainer=Frame(self.fen,height=800,width=230,bg='#51a596')
        self.MenuContainer.place(x=0,y=0)
        self.titre = Label(self.MenuContainer, text = "GEST - FACT", font = "Arial 15 bold",bg='#51a596',fg='white').place(x=30, y=20)

        self.gest_article=Button(self.MenuContainer,text='ARTICLES', command=self.save)
        self.gest_article.place(x=20,y=80, width=190,height=40)

        self.gest_Clients=Button(self.MenuContainer,text='CLIENTS', command=self.save)
        self.gest_Clients.place(x=20,y=140, width=190,height=40)

        self.gest_Clients=Button(self.MenuContainer,text='FACTURE', command=self.open_facture)
        self.gest_Clients.place(x=20,y=200, width=190,height=40)

        self.gest_Clients=Button(self.MenuContainer,text='PAIEMENT', command=self.ouvri_paiement)
        self.gest_Clients.place(x=20,y=260, width=190,height=40)

        self.gest_Clients=Button(self.MenuContainer,text='RAPPORT', command=self.ouvrir_rapport)
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
        self.ajouter_btn= Button(self.Actions,bg='#51a596',text='Ajouter',fg='white', command=self.ajouter_article)
        self.ajouter_btn.place(x=0,y=20, width=120,height=40)
        self.modifier_btn= Button(self.Actions,bg='#51a596',text='Modifier',fg='white', command=self.modifier_article)
        self.modifier_btn.place(x=0,y=70, width=120,height=40)
        self.Supprimer_btn= Button(self.Actions,bg='brown',text='Supprimer',fg='white', command=self.supprimer_article)
        self.Supprimer_btn.place(x=0,y=120, width=120,height=40)

        self.CodeLab = Label(self.form, text='Code',bg='gray',fg='white',font='20')
        self.CodeLab.place(x=20,y=50, height=30)
        self.DesiLab = Label(self.form, text='Désignation',bg='gray',fg='white',font='20')
        self.DesiLab.place(x=20,y=100, height=30)
        self.PrixLab = Label(self.form, text='Prix',bg='gray',fg='white',font='20')
        self.PrixLab.place(x=20,y=150, height=30)
        
        self.CodeEnt=Entry(self.form)
        self.CodeEnt.place(x=150,y=50,width=250, height=30)
        self.desiEnt=Entry(self.form)
        self.desiEnt.place(x=150,y=100,width=250, height=30)
        self.prixEnt=Entry(self.form)
        self.prixEnt.place(x=150,y=150,width=250, height=30)
        
        


        self.PdfSection=Frame(self.ContainerRight,height=50,width=580)
        self.PdfSection.place(x=0,y=270)


        self.visualiser_btn= Button(self.PdfSection,bg='#51a596',text='Visualiser',fg='white', command=self.open_file)
        self.visualiser_btn.place(x=0,y=10, width=120,height=40)

        self.generer_btn= Button(self.PdfSection,bg='#51a596',text='Generer',fg='white', command=self.save)
        self.generer_btn.place(x=150,y=10, width=120,height=40)

        self.TabSection=Frame(self.ContainerRight,height=550,width=580,bg='blue')
        self.TabSection.place(x=0,y=330)
        #Creation du tableau
        self.tableau=ttk.Treeview(self.TabSection, columns=('Code','Designation','Prix'), show='headings')
        self.tableau.heading('Code', text='Code')
        self.tableau.heading('Designation', text='Désignation')
        self.tableau.heading('Prix', text='Prix')
        self.valeur_code_art=None
        self.valeur_designation=None
        self.valeur_prix=None
        self.elemen_selected=None

        #Ajouts des elements dans le tableau
        self.afficher()


        self.tableau.pack()
    def open_file(self):
        webbrowser.open("pdf")
    def get_entry(self):
        self.valeur_code_art=self.CodeEnt.get()
        self.valeur_designation=self.desiEnt.get()
        self.valeur_prix=self.prixEnt.get()

     #Creation de la section de tableau   
    def get_table_selected_row(self,event):        
        self.clean_entry()
        row=self.tableau.selection()[0]
        self.elemen_selected=self.tableau.set(row)
        self.CodeEnt.insert(0,self.elemen_selected['Code'])
        self.desiEnt.insert(0,self.elemen_selected['Designation'])
        self.prixEnt.insert(0,self.elemen_selected['Prix'])
        self.get_entry()
    """modifier un article"""
    def modifier_article(self):
        if self.valeur_code_art is  not None:
            self.get_entry()
        article=ArticleBackend(self.CodeEnt.get(),self.desiEnt.get(),self.prixEnt.get())
        print(self.CodeEnt.get(),self.desiEnt.get(),self.prixEnt.get())
        print([self.elemen_selected['Code'],self.elemen_selected['Designation'],self.elemen_selected['Prix']])
        print([self.valeur_code_art,self.valeur_designation,self.valeur_prix])
        if article.update(self.curseur,[self.elemen_selected['Code'],self.elemen_selected['Designation'],self.elemen_selected['Prix']]):
            self.afficher()

        self.clean_entry()        
        self.clear_selected_value()
    """supprimer un article"""
    def supprimer_article(self):
        article=ArticleBackend(self.CodeEnt.get(),self.desiEnt.get(),self.prixEnt.get())
        article.delete(self.curseur)
        self.afficher()
        self.clean_entry()
        self.clear_selected_value()
    """afficher les articles"""
    def afficher(self):
        a=ArticleBackend("1","2",3)
        data=a.all(self.curseur)
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
        self.CodeEnt.delete(0,END)
        self.desiEnt.delete(0,END)
        self.prixEnt.delete(0,END)    
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
    def ouvri_paiement(self):
        paiement = PaiementFrontend(self.curseur)
        self.fen.destroy()
        paiement.fenetre().mainloop()
    def ouvrir_rapport(self):
        rapport = RapportFrontend(self.curseur)
        self.fen.destroy()
        rapport.fenetre().mainloop()
    def open_facture(self):
        facture = FactureFrontend(self.curseur)
        self.fen.destroy()
        facture.fenetre().mainloop()