from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
import datetime

# Fonction pour générer un PDF de facture
def generate_invoice_pdf(customer_info, products, total_amount):
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

    data = [["Produit", "Quantité", "Prix unitaire", "Total"]]
    for product in products:
        data.append([product['name'], str(product['quantity']), str(product['unit_price']), str(product['total'])])

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

# Informations de test pour la facture
customer_info = {
    "Nom": "Client Test",
    "Adresse": "123 Rue Test, Ville, Pays",
    "Email": "client@test.com"
}

products = [
    {"name": "Produit 1", "quantity": 2, "unit_price": 10.0, "total": 20.0},
    {"name": "Produit 2", "quantity": 1, "unit_price": 15.0, "total": 15.0}
]

total_amount = 35.0

# Générer la facture PDF
generate_invoice_pdf(customer_info, products, total_amount)