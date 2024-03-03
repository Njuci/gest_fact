from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Table, TableStyle, SimpleDocTemplate
import tkinter as tk
from tkinter import ttk
from tkinter import *

# Fonction pour générer un PDF à partir des données d'un TreeView
def generate_pdf(tree):
    doc = SimpleDocTemplate("table.pdf", pagesize=letter)
    elements = []

    # Extraire les données du TreeView
    data = []
    for child in tree.get_children():
        values = tree.item(child)['values']
        data.append(values)

    # Créer une table à partir des données
    table = Table(data)

    # Styles de la table
    style = TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                        ('GRID', (0, 0), (-1, -1), 1, colors.black)])

    table.setStyle(style)
    elements.append(table)

    # Générer le PDF
    doc.build(elements)

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

root.mainloop()