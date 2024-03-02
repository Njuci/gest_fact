from tkinter import *
from tkinter.messagebox import showinfo
from connexion import Login_back
from article_fr import Article_frontend_Ajout
class Login_frontend:
    def __init__(self):
        self.fen=Tk()
        self.fen.title("Authentification")
        self.fen.geometry("800x600")
        self.titre=Label(self.fen,text="Connexion",font="Times 35 bold").place(x=290,y=50)
        self.frame1=Frame(self.fen,height=300,width=760,bg='gray')
        self.frame1.place(x=20,y=180)
        #self.espace=Label(self.frame1,text='').grid(column=0,row=0,columnspan=2)
        self.idlabel=Label(self.frame1,text="Identifiant",bg='gray')
        self.idlabel.place(x=20,y=20,width=180)
        self.mdpLabel=Label(self.frame1,text="Mot de Passe",bg='gray')
        self.mdpLabel.place(x=20,y=60,width=100)
        self.username_text=Entry(self.frame1)
        self.username_text.place(x=350,y=20,width=100)
        self.mdp_text=Entry(self.frame1,show="*")
        self.mdp_text.place(x=350,y=60,width=100)
        self.btn_validation=Button(self.frame1,text="Se connecter".upper(),bg="lightblue",font="Times 20 bold",command=self.login)
        self.btn_validation.place(x=200,y=200,width=300,height=50)
        self.curseur=None

    def fenetre(self):
        return self.fen
    def login(self):
        print(self.username_text.get(),self.mdp_text.get())
        user=Login_back(self.username_text.get(),self.mdp_text.get())
        if user.login():
            showinfo("Factiuration System","Connexion Reussi")
            fen2=Article_frontend_Ajout(user.curseur)
            self.fen.destroy()
            fen2.fenetre().mainloop()
            


if __name__=='__main__':
    fen=Login_frontend()
    fen.fenetre().mainloop()
