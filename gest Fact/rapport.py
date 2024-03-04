from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from datetime import datetime

def create_pdf_with_custom_header_and_table(file_name, company_name, title, data):
    doc = SimpleDocTemplate(file_name, pagesize=letter)
    
    # Define styles
    styles = getSampleStyleSheet()
    header_style = styles['Heading1']
    
    # Custom header
    header_text = f"<font size=14>{company_name}</font><br/><font color=grey>{title}</font><br/><font color=grey>{datetime.now().strftime('%Y-%m-%d')}</font>"
    header = Paragraph(header_text, header_style)
    
    # Table
    table_style = TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
                              ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
                              ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                              ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                              ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                              ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                              ('GRID', (0, 0), (-1, -1), 1, colors.black)
                              ])
    table_data = data
    table = Table(table_data)
    table.setStyle(table_style)
    
    # Build the document
    doc.build([header, table])

data = [
    ['Name', 'Age', 'Country'],
    ['John Doe', '30', 'USA'],
    ['Jane Smith', '25', 'UK'],
    ['Doe Smith', '40', 'Australia'],
]

create_pdf_with_custom_header_and_table("table_with_custom_header_example.pdf", "ABC Company", "Example Report", data)
