import datetime as dt
from tkinter import *
from article_modifier import Article_frontend_Modifier
from tkinter.messagebox import showinfo,showerror
from connexion import ArticleBackend
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from tkPDFViewer import tkPDFViewer as pdf
class Article_frontend_Ajout:
    def __init__(self,curseur):
        self.fen=Tk()
        self.fen.title("Articles")
        self.fen.geometry("800x600")
        self.menu=Menu(self.fen)
        """menu  Article"""

        self.fichier=Menu(self.menu,tearoff=0)
        self.fichier.add_command(label="Modifier",command=self.modifier)
        self.fichier.add_command(label="Supprimer",command=self.delete)
        self.menu.add_cascade(label="Fichier",menu=self.fichier)
        self.supprimer_art=Menu(self.menu,tearoff=0)
        self.menu.add_cascade(label="Quiter",menu=self.fen,command=self.fen.quit)    
        self.fen.config(menu=self.menu)
        
        
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
        self.curseur=curseur
        self.fen2=None
        self.pr_pdf=None
        """tableau des articles dans la base de donnees"""
        self.tableau=Listbox(self.frame2)
        self.tableau.place(x=20,y=20,width=220,height=100)
        self.tableau.insert(0,"Code Article | Designation | Prix")
        self.affiche()
        self.previsualiser_pdf=Button(self.frame2,text="Previsualiser",bg="lightblue",font="Times 15 bold",command=self.previsualiser)

        self.previsualiser_pdf.place(x=20,y=140,width=150,height=30)
        self.visualiser_pdf=Button(self.frame2,text="Visualiser",bg="lightblue",font="Times 15 bold",command=self.visualiser_pdf)
        self.visualiser_pdf.place(x=180,y=140,width=100,height=30)
    def previsualiser(self):
            now=dt.datetime.now()      
            """formatage de la date pour le nom du fichier pdf""" 
            now2=now.strftime("%Y-%m-%d%H-%M-%S")                   
            c=canvas.Canvas("pdf/articles_dispo/articles"+str(now2)+".pdf",pagesize=letter)
            """entete du fichier pdf et affichage des articles dans la base de donnees"""
            c.setFillColorRGB(1, 0, 0)  # Red color
            # Set font size for the title
            now3=now.strftime("%Y-%m-%d %H:%M:%S")
            c.setFont("Helvetica-Bold", 22) 
            # Draw the title text
            c.drawString(100,700,"Liste des Articles ce "+str(now3))
            """ """

    
            c.drawString(100,600,"Code Article | Designation | Prix")
            article=ArticleBackend("2","2",2)
            articles=article.all(self.curseur)
            y=500            
            for art in articles:
                c.setFillColorRGB(0, 0, 0)  # Noir
                c.setFont("Helvetica-Bold", 16)  # Police standard, taille de police 12

                c.drawString(100,y,art[0]+"   |   "+art[1]+"   |   "+str(art[2]))
                y-=20
            c.save()
            showinfo("Previsualisation","Fichier PDF cree avec succes")
    """vusialisation du fichier pdf des articles"""
    def visualiser_pdf(self):
        self.fen2=Tk()
        self.fen2.geometry("800x600")
        self.fen2.title("Visualisation PDF")
        self.fen2.configure(bg="lightblue")
        
        try:
            self.pdf=pdf.ShowPdf()
            try:
               self.pr_pdf=self.pdf.pdf_view(self.fen2,pdf_location=r"articles.pdf",width=50,height=200) 
               self.pr_pdf.pack(pady=(0,0))
            except Exception as e:
                showerror("Visualisation",str(e))
                
                #self.pdf.pdf_view(self.fen2,pdf_location="articles.pdf",width=50,height=200)
            
        except Exception as e:
            showerror("Visualisation",str(e))
       
        
        
    def modifier(self):
        a=Article_frontend_Modifier(self.curseur)
        self.fen.destroy()
        a.fenetre().mainloop()
        

    def affiche(self):
        self.tableau.delete(1,END)  
        article=ArticleBackend("2","2",2)
        articles=article.all(self.curseur)
        for art in articles:
            self.tableau.insert(END,art[0]+" | "+art[1]+" | "+str(art[2]))
            
    def delete(self):
        pass
  

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
    