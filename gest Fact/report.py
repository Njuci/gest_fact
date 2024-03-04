from reportlab.lib.pagesizes import letter
from reportlab.platypus import Table, TableStyle, SimpleDocTemplate, Frame
from reportlab.platypus import Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
import datetime
import tkinter as tk
from tkinter import ttk
from tkinter import *

# Fonction pour générer un PDF à partir des données d'un TreeView avec un tableau plus grand et un titre
def generate_pdf(tree,file_name,heading,titre,dimension:list):
    doc = SimpleDocTemplate(file_name, pagesize=letter)
    elements = []

    # Extraire les données du TreeView
    data = [heading]
    for child in tree.get_children():
        values = tree.item(child)['values']
        data.append(values)

    # Ajouter un titre au-dessus du tableau
    styles = getSampleStyleSheet()
    title = Paragraph(titre, styles['Heading1'])
    elements.append(title)

    # Ajouter la date
    today = datetime.datetime.today().strftime('%Y-%m-%d')
    date_text = Paragraph("Date: " + today, styles['Normal'])
    elements.append(date_text)
    title = Paragraph("", styles['Heading1'])
    elements.append(title)
    title = Paragraph("", styles['Heading1'])
    elements.append(title)


    # Spécifier une largeur et une hauteur plus grandes pour le tableau
    table = Table(data, colWidths=dimension[0], rowHeights=dimension[1])

    # Styles de la table
    style = TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.lightblue),
                        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                        ('GRID', (0, 0), (-1, -1), 1, colors.black)])

    table.setStyle(style)
    
    elements.append(table)

    # Générer le PDF
    doc.build(elements)
    return True

"""
# Créer une fenêtre tkinter avec un TreeView
root = tk.Tk()
tree = ttk.Treeview(root)
tree["columns"] = ("col1", "col2")
tree.heading("#0", text="Item")
tree.heading("col1", text="Colonne 1")
tree.heading("col2", text="Colonne 2")
tree.pack()

# Insérer des données dans le TreeView pour tester
tree.insert("", "end", text="1", values=("A", "B"))
tree.insert("", "end", text="2", values=("C", "D"))

# Bouton pour générer le PDF
btn = Button(root, text="Générer PDF", command=lambda: generate_pdf(tree))
btn.pack()

root.mainloop()"""
def generate_invoice_pdf(customer_info, tree,headimg ,total_amount):
    doc = SimpleDocTemplate("facture.pdf", pagesize=letter)
    elements = []

    styles = getSampleStyleSheet()

    # Entête de la facture
    elements.append(Paragraph("Facture", styles['Title']))

    # Informations du client
    elements.append(Paragraph("Informations du client:", styles['Heading2']))
    for key, value in customer_info.items():
        elements.append(Paragraph(f"{key}: {value}", styles['Normal']))

    # Détails des produits
    elements.append(Paragraph("Détails des produits:", styles['Heading2']))

    data = [headimg]
    for child in tree.get_children():
        values = tree.item(child)['values']
        data.append(values)

    table = Table(data)
    table.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                              ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                              ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                              ('GRID', (0, 0), (-1, -1), 1, colors.black)]))

    elements.append(table)

    # Total
    elements.append(Paragraph(f"Total: {total_amount}", styles['Heading2']))

    # Date de la facture
    today = datetime.datetime.today().strftime('%Y-%m-%d')
    elements.append(Paragraph(f"Date de la facture: {today}", styles['Normal']))

    # Générer le PDF
    doc.build(elements)
    return True