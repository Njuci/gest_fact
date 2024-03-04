from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, inch, landscape
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph,Image,Spacer
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
import datetime

# fonction pour generer le rapport de paiement 
def genererRapportPaiement(paymentData):
    # data : liste de : datepaie,montant,idFacture,montantRestant, desiganationProduit
    doc = SimpleDocTemplate("Rapport paiement.pdf", pagesize=A4, rightMargin=30,leftMargin=30, topMargin=30,bottomMargin=18)
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
    style = TableStyle([('ALIGN',(1,1),(-2,-2),'RIGHT'),
                       ('TEXTCOLOR',(1,1),(-2,-2),colors.red),
                       ('VALIGN',(0,0),(0,-1),'TOP'),
                       ('TEXTCOLOR',(0,0),(0,-1),colors.blue),
                       ('ALIGN',(0,-1),(-1,-1),'CENTER'),
                       ('VALIGN',(0,-1),(-1,-1),'MIDDLE'),
                       ('TEXTCOLOR',(0,-1),(-1,-1),colors.green),
                       ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                       ('BOX', (0,0), (-1,-1), 0.25, colors.black),

                       ])


    s = getSampleStyleSheet()
    s = s["BodyText"]
    s.wordWrap = 'CJK'
    # getting header first row datepaie idfact montant idFact datfact reduction idcli codArt quantite desiArt prix 
    # format of data [{idFact:01}]
    # getting headers from the first row
    
    # datepaie,idfact,montant,idFact,datfact,reduction,idcli,codArt,quantite,codeArt,desiArt,prix,nomcli,adrcli,numte
    headers = ["Date de paiement", "ID Facture", "Montant", "Date Facture", "Reduction", "ID Client", "Qté", "Designation", "Prix", "ID Client", "Nom Clt", "Adresse", "Numero","Montant restant"]
    # adding the headers to the table
    data2 = [headers]
    # header style
    
    # adding the data to the table
    for row in paymentData:
        data2.append(list(row.values()))
    t=Table(data2)
    t.setStyle(style)
    elements.append(t)
    # adding a space
    elements.append(Spacer(1, 12))
    # Footer
    footer = "Rapport genere le "+str(datetime.datetime.now())
    elements.append(Paragraph(footer, normalstyle))


    # generate the pdf
    doc.build(elements)
