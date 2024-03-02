from tkinter import *
from tkinter.messagebox import showinfo,showerror
from connexion import ArticleBackend

class Article_frontend:
    def __init__(self,curseur):
        self.fen=Tk()
        self.fen.title("Articles")
        self.fen.geometry("800x600")
        self.titre=Label(self.fen,text="Ajout articles",font="Times 35 bold").place(x=290,y=50)
        self.frame1=Frame(self.fen,height=200,width=760,bg='gray')
        self.frame1.place(x=20,y=180)
        #self.espace=Label(self.frame1,text='').grid(column=0,row=0,columnspan=2)
        self.idlabel=Label(self.frame1,text="Code Article",bg='gray')
        self.idlabel.place(x=20,y=20,width=180)
        self.mdpLabel=Label(self.frame1,text="Designation ",bg='gray')
        self.mdpLabel.place(x=20,y=60,width=100)
        self.codArt_text=Entry(self.frame1)
        self.codArt_text.place(x=350,y=20,width=100)
        self.desi_text=Entry(self.frame1)
        self.desi_text.place(x=350,y=60,width=100)
        self.prix_labl=Label(self.frame1,text="Prix",bg='gray')
        self.prix_labl.place(x=20,y=100)
        self.prix_text=Entry(self.frame1)
        self.prix_text.place(x=350,y=100,width=100)
        self.btn_validation=Button(self.frame1,text="Enregistrer".upper(),bg="lightblue",font="Times 20 bold",command=self.save)
        self.btn_validation.place(x=200,y=150,width=300,height=50)
        self.frame2=Frame(self.fen,height=200,width=760,bg='gray')
        self.frame2.place(x=20,y=400)
        
        """tableau des articles dans la base de donnees"""
        self.tableau=Listbox(self.frame2)
        self.tableau.place(x=20,y=20,width=720,height=150)
        self.tableau.insert(0,"Code Article | Designation | Prix")
        self.affiche()
        
        self.curseur=curseur
        
        self.curseur=curseur
    """affichage dans un tableau tkinter  des articles dans la base de donnees"""
    def affiche(self):
        self.tableau.delete(1,END)  
        article=ArticleBackend()
        articles=article.all(self.curseur)
        for art in articles:
            self.tableau.insert(END,art[0]+" | "+art[1]+" | "+str(art[2]))
            
        

    def fenetre(self):
        return self.fen
    def save(self):
        article=ArticleBackend(cod=self.codArt_text.get(),desi=self.desi_text.get(),prix=self.prix_text.get())
        if article.save(self.curseur):
            showinfo("Enregistrement","Enregistrement reussi")
        else:
            showerror("Enregistrement","Echec d'enregistrement")

        self.codArt_text.delete(0,END)
        self.desi_text.delete(0,END)
        self.prix_text.delete(0,END)
    