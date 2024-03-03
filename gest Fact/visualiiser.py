import tkinter as tk
from tkinter import ttk
import webbrowser

# Fonction pour ouvrir le PDF dans un navigateur web
def open_pdf():
    webbrowser.open('pdf')

# Créer une fenêtre tkinter
root = tk.Tk()
root.title("Visualisation PDF")

# Créer un Notebook (onglets)
notebook = ttk.Notebook(root)
notebook.pack(expand=1, fill="both")

# Ajouter l'onglet pour visualiser le PDF
pdf_frame = ttk.Frame(notebook)
notebook.add(pdf_frame, text="PDF Viewer")

# Bouton pour ouvrir le PDF
btn_open_pdf = ttk.Button(pdf_frame, text="Visualiser PDF", command=open_pdf)
btn_open_pdf.pack(pady=20)

root.mainloop()