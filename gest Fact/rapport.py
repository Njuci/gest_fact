from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, inch, landscape,letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph,Image,Spacer
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
import datetime
from tkinter.messagebox import showinfo
from reportlab.pdfgen import canvas


# fonction pour generer le rapport de paiement 
def genererRapportPaiement(paymentData):
    # data : liste de : datepaie,montant,idFacture,montantRestant, desiganationProduit
    doc = SimpleDocTemplate("Rapport_paiement.pdf", pagesize=A4, rightMargin=30,leftMargin=30, topMargin=30,bottomMargin=18)
    doc.pagesize = landscape(A4)
    elements = []
    # logo
    logo = "logo.png"
    imgw = 130
    imgh = 100
    im = Image(logo, width=imgw, height=imgh)
    im.hAlign = 'LEFT'
    # style en tete
    
    headstyle = ParagraphStyle(
        name='MyHeader',
        fontName='Helvetica-Bold',
        fontSize=18,
        leading =11
    )
    normalstyle = ParagraphStyle(
        name='MyDoctorHeader',
        fontName='Helvetica',
        fontSize=13,
        leading =10,
        textColor = 'green',
        spaceAfter=14
    )

    # entete
    data = [[Paragraph("Boutique Gest_fact", style = headstyle)], [Paragraph("Facturation", style = normalstyle)], [Paragraph("ENT Specialist", style = normalstyle)], [Paragraph("Rapport de paiement", style = normalstyle)]]
    col1 = Table([[im]])
    col2 = Table(data, repeatRows=1)
    tblrow1 = Table([[col1, col2]], colWidths=None)
    tblrow1.setStyle(
        TableStyle([
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ]))
    elements.append(tblrow1)
    # adding a line break
    elements.append(Paragraph("<br></br>", normalstyle))
    # adding a centered title
    elements.append(Paragraph("<center>Rapport de paiement<center>", headstyle))
    # adding a spacer
    elements.append(Spacer(1, 12))
    # adding a line break
    elements.append(Paragraph("<br></br>", normalstyle))
    # TABLE
    style = TableStyle([('ALIGN',(1,1),(-2,-2),'CENTER'),
                        # fistr line is the header , font bold
                        ('TEXTCOLOR',(0,0),(-1,0),colors.black),
                    #    ('TEXTCOLOR',(1,1),(-2,-2),colors.red),
                       ('VALIGN',(0,0),(0,-1),'TOP'),
                    #    ('TEXTCOLOR',(0,0),(0,-1),colors.blue),
                       ('ALIGN',(0,-1),(-1,-1),'CENTER'),
                       ('VALIGN',(0,-1),(-1,-1),'MIDDLE'),
                    #    ('TEXTCOLOR',(0,-1),(-1,-1),colors.green),
                       ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                       ('BOX', (0,0), (-1,-1), 0.25, colors.black),
                   
                       ])


    s = getSampleStyleSheet()
    s = s["BodyText"]
    s.wordWrap = 'CJK'
    
    headers = ["Date de paiement", "ID Facture", "Montant", "Date Facture", "Reduction", "Qté", "Designation", "Prix", "ID Client", "Nom Clt", "Adresse", "Numero","Montant restant"]
    # adding the headers to the table
    data2 = [headers]
    # header style
    
    # adding the data to the table
    print(paymentData)
    for row in paymentData:
        data2.append(list(row.values()))
    t=Table(data2)
    t.setStyle(style)
    elements.append(t)
    # adding a space
    elements.append(Spacer(1, 12))
    # Footer
    footer = "Rapport complet "+str(datetime.datetime.now())
    elements.append(Paragraph(footer, normalstyle))


    # generate the pdf
    doc.build(elements,canvasmaker=FooterCanvas)
    showinfo("Fichier pdf","Votre rapport a été genérer avec succès")


def genereRapportArticle(articlesData):
      # data : liste de : datepaie,montant,idFacture,montantRestant, desiganationProduit
    doc = SimpleDocTemplate("rapport_articles.pdf", pagesize=A4, rightMargin=30,leftMargin=30, topMargin=30,bottomMargin=18)
    doc.pagesize = landscape(A4)
    elements = []
    # logo
    logo = "logo.png"
    imgw = 130
    imgh = 100
    im = Image(logo, width=imgw, height=imgh)
    im.hAlign = 'LEFT'
    # style en tete
    
    headstyle = ParagraphStyle(
        name='MyHeader',
        fontName='Helvetica-Bold',
        fontSize=18,
        leading =11
    )
    normalstyle = ParagraphStyle(
        name='MyDoctorHeader',
        fontName='Helvetica',
        fontSize=13,
        leading =10,
        textColor = 'green',
        spaceAfter=14
    )

    # entete
    data = [[Paragraph("Boutique Gest_fact", style = headstyle)], [Paragraph("Facturation", style = normalstyle)], [Paragraph("ENT Specialist", style = normalstyle)], [Paragraph("Rapport de paiement", style = normalstyle)]]
    col1 = Table([[im]])
    col2 = Table(data, repeatRows=1)
    tblrow1 = Table([[col1, col2]], colWidths=None)
    tblrow1.setStyle(
        TableStyle([
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ]))
    elements.append(tblrow1)
    # adding a line break
    elements.append(Paragraph("<br></br>", normalstyle))
    # adding a centered title
    elements.append(Paragraph("<center>Rapport Articles <center>", headstyle))
    # adding a spacer
    elements.append(Spacer(1, 12))
    # adding a line break
    elements.append(Paragraph("<br></br>", normalstyle))
    # TABLE
    style = TableStyle([('ALIGN',(1,1),(-2,-2),'CENTER'),
                        # fistr line is the header , font bold
                        ('TEXTCOLOR',(0,0),(-1,0),colors.black),
                    #    ('TEXTCOLOR',(1,1),(-2,-2),colors.red),
                       ('VALIGN',(0,0),(0,-1),'TOP'),
                    #    ('TEXTCOLOR',(0,0),(0,-1),colors.blue),
                       ('ALIGN',(0,-1),(-1,-1),'CENTER'),
                       ('VALIGN',(0,-1),(-1,-1),'MIDDLE'),
                    #    ('TEXTCOLOR',(0,-1),(-1,-1),colors.green),
                       ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                       ('BOX', (0,0), (-1,-1), 0.25, colors.black),
                   
                       ])


    s = getSampleStyleSheet()
    s = s["BodyText"]
    s.wordWrap = 'CJK'
    
    headers = ["Code Article","Designation","Prix"]
    # adding the headers to the table
    data2 = [headers]
    # header style
    
   
    for row in articlesData:
        data2.append(list(row))
    t=Table(data2)
    t.setStyle(style)
    elements.append(t)
    # adding a space
    elements.append(Spacer(1, 12))
    # Footer
    footer = "Rapport genere le "+str(datetime.datetime.now())
    elements.append(Paragraph(footer, normalstyle))


    # generate the pdf
    doc.build(elements,canvasmaker=FooterCanvas)
    showinfo("Rapport facture pdf","Votre rapport a été genérer avec succès")

def generateRapportFacture(factureData):
    doc = SimpleDocTemplate("rapport_facture.pdf", pagesize=A4, rightMargin=30,leftMargin=30, topMargin=30,bottomMargin=18)
    doc.pagesize = landscape(A4)
    elements = []
    # logo
    logo = "logo.png"
    imgw = 130
    imgh = 100
    im = Image(logo, width=imgw, height=imgh)
    im.hAlign = 'LEFT'
    # style en tete
    
    headstyle = ParagraphStyle(
        name='MyHeader',
        fontName='Helvetica-Bold',
        fontSize=18,
        leading =11
    )
    normalstyle = ParagraphStyle(
        name='MyDoctorHeader',
        fontName='Helvetica',
        fontSize=13,
        leading =10,
        textColor = 'green',
        spaceAfter=14
    )

    # entete
    data = [[Paragraph("Boutique Gest_fact", style = headstyle)], [Paragraph("Facturation", style = normalstyle)], [Paragraph("ENT Specialist", style = normalstyle)], [Paragraph("Rapport de paiement", style = normalstyle)]]
    col1 = Table([[im]])
    col2 = Table(data, repeatRows=1)
    tblrow1 = Table([[col1, col2]], colWidths=None)
    tblrow1.setStyle(
        TableStyle([
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ]))
    elements.append(tblrow1)
    # adding a line break
    elements.append(Paragraph("<br></br>", normalstyle))
    # adding a centered title
    elements.append(Paragraph("<center>Rapport Ventes <center>", headstyle))
    # adding a spacer
    elements.append(Spacer(1, 12))
    # adding a line break
    elements.append(Paragraph("<br></br>", normalstyle))
    # TABLE
    style = TableStyle([('ALIGN',(1,1),(-2,-2),'CENTER'),
                        # fistr line is the header , font bold
                        ('TEXTCOLOR',(0,0),(-1,0),colors.black),
                    #    ('TEXTCOLOR',(1,1),(-2,-2),colors.red),
                       ('VALIGN',(0,0),(0,-1),'TOP'),
                    #    ('TEXTCOLOR',(0,0),(0,-1),colors.blue),
                       ('ALIGN',(0,-1),(-1,-1),'CENTER'),
                       ('VALIGN',(0,-1),(-1,-1),'MIDDLE'),
                    #    ('TEXTCOLOR',(0,-1),(-1,-1),colors.green),
                       ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                       ('BOX', (0,0), (-1,-1), 0.25, colors.black),
                   
                       ])


    s = getSampleStyleSheet()
    s = s["BodyText"]
    s.wordWrap = 'CJK'
    
    headers = ["Id Facture","Date de la facture","Client","Adresse Client","Numéro"]
    # adding the headers to the table
    data2 = [headers]
    # header style
    
    # adding the data to the table
    print(factureData)
    for row in factureData:
        data2.append(list(row))
    t=Table(data2)
    t.setStyle(style)
    elements.append(t)
    # adding a space
    elements.append(Spacer(1, 12))
    # Footer
    footer = "Rapport genere le "+str(datetime.datetime.now())
    elements.append(Paragraph(footer, normalstyle))


    # generate the pdf
    doc.build(elements,canvasmaker=FooterCanvas)
    showinfo("Fichier pdf","Votre rapport a été genérer avec succès")

def generateRapportCustomer(customerdata):
    doc = SimpleDocTemplate("rapport_clients.pdf", pagesize=A4, rightMargin=30,leftMargin=30, topMargin=30,bottomMargin=18)
    doc.pagesize = landscape(A4)
    elements = []
    # logo
    logo = "logo.png"
    imgw = 130
    imgh = 100
    im = Image(logo, width=imgw, height=imgh)
    im.hAlign = 'LEFT'
    # style en tete
    
    headstyle = ParagraphStyle(
        name='MyHeader',
        fontName='Helvetica-Bold',
        fontSize=18,
        leading =11
    )
    normalstyle = ParagraphStyle(
        name='MyDoctorHeader',
        fontName='Helvetica',
        fontSize=13,
        leading =10,
        textColor = 'green',
        spaceAfter=14
    )

    # entete
    data = [[Paragraph("Boutique Gest_fact", style = headstyle)], [Paragraph("Facturation", style = normalstyle)], [Paragraph("ENT Specialist", style = normalstyle)], [Paragraph("Rapport de clients", style = normalstyle)]]
    col1 = Table([[im]])
    col2 = Table(data, repeatRows=1)
    tblrow1 = Table([[col1, col2]], colWidths=None)
    tblrow1.setStyle(
        TableStyle([
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ]))
    elements.append(tblrow1)
    # adding a line break
    elements.append(Paragraph("<br></br>", normalstyle))
    # adding a centered title
    elements.append(Paragraph("<center>Rapport Clients <center>", headstyle))
    # adding a spacer
    elements.append(Spacer(1, 12))
    # adding a line break
    elements.append(Paragraph("<br></br>", normalstyle))
    # TABLE
    style = TableStyle([('ALIGN',(1,1),(-2,-2),'CENTER'),
                        # fistr line is the header , font bold
                        ('TEXTCOLOR',(0,0),(-1,0),colors.black),
                    #    ('TEXTCOLOR',(1,1),(-2,-2),colors.red),
                       ('VALIGN',(0,0),(0,-1),'TOP'),
                    #    ('TEXTCOLOR',(0,0),(0,-1),colors.blue),
                       ('ALIGN',(0,-1),(-1,-1),'CENTER'),
                       ('VALIGN',(0,-1),(-1,-1),'MIDDLE'),
                    #    ('TEXTCOLOR',(0,-1),(-1,-1),colors.green),
                       ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                       ('BOX', (0,0), (-1,-1), 0.25, colors.black),
                   
                       ])


    s = getSampleStyleSheet()
    s = s["BodyText"]
    s.wordWrap = 'CJK'
    
    headers = ["Id Client","Nom du client","Adresse du client","Numéro de télephone"]
    # adding the headers to the table
    data2 = [headers]
    # header style
    
    # adding the data to the table
    print(customerdata)
    for row in customerdata:
        data2.append(list(row))
    t=Table(data2)
    t.setStyle(style)
    elements.append(t)
    # adding a space
    elements.append(Spacer(1, 12))
    # Footer
    footer = "Rapport genere le "+str(datetime.datetime.now())
    elements.append(Paragraph(footer, normalstyle))


    # generate the pdf
    doc.build(elements,canvasmaker=FooterCanvas)
    showinfo("Fichier pdf","Votre rapport a été genérer avec succès")

class FooterCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        canvas.Canvas.__init__(self, *args, **kwargs)
        self.pages = []

    def showPage(self):
        self.pages.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        page_count = len(self.pages)
        for page in self.pages:
            self.__dict__.update(page)
            footer = "Rapport genere le "+str(datetime.datetime.now())
            self.setFont("Helvetica", 10)
            self.drawString(letter[0]/2, 30, footer)
            canvas.Canvas.showPage(self)
        canvas.Canvas.save(self)