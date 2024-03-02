from tkinter import *
from tkinter.messagebox import showinfo
from connexion import Login_back
class Article_frontend:
    def __init__(self,curseur):
        self.fen=Tk()
        self.fen.title("Articles")
        self.fen.geometry("800x600")
        self.titre=Label(self.fen,text="Ajout articles",font="Times 35 bold").place(x=290,y=50)
        self.frame1=Frame(self.fen,height=300,width=760,bg='gray')
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
        self.btn_validation.place(x=200,y=200,width=300,height=50)
        self.curseur=curseur


    def fenetre(self):
        return self.fen
    def save(self):
        pass