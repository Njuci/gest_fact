from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors

def create_pdf_with_table(file_name, data):
    doc = SimpleDocTemplate(file_name, pagesize=letter)
    table_style = TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                              ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                              ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                              ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                              ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                              ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                              ('GRID', (0, 0), (-1, -1), 1, colors.black)
                              ])
    table_data = data
    table = Table(table_data)
    table.setStyle(table_style)

    doc.build([table])

data = [
    ['Name', 'Age', 'Country'],
    ['John Doe', '30', 'USA'],
    ['Jane Smith', '25', 'UK'],
    ['Doe Smith', '40', 'Australia'],
]

create_pdf_with_table("table_example.pdf", data)