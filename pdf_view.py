import io
import tkinter as tk
import tkinter.messagebox as tkmessagebox
from PIL import Image, ImageTk
import PyPDF2

class PDFViewer(tk.Frame):
    def __init__(self, root, filename):
        super().__init__(root)
        self.filename = filename
        self.page_num = 1

        # Create canvas widget for displaying the PDF image
        self.canvas = tk.Canvas(self)
        self.image_id = None
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Create button widgets for navigation
        self.prev_button = tk.Button(self, text="Previous", command=self.prev_page)
        self.prev_button.pack(side=tk.LEFT)
        self.next_button = tk.Button(self, text="Next", command=self.next_page)
        self.next_button.pack(side=tk.RIGHT)

        self.load_page()

    def load_page(self):
        # Open the PDF file
        with open(self.filename, 'rb') as f:
            try:
                # Create a PDF reader
                    pdf_reader = PyPDF2.PdfReader(f)
                    page = pdf_reader.pages[self.page_num - 1]

                    # Extract the page image using PIL
                    image = page.extract_image(open_file=False)
                    img_pil = Image.open(io.BytesIO(image))

                    # Resize the image to fit within the canvas
                    img_pil = img_pil.resize((self.canvas.winfo_width(), self.canvas.winfo_height()), Image.ANTIALIAS)

                    # Convert the image to a Tkinter image format
                    self.img_tk = ImageTk.PhotoImage(img_pil)
                    if self.image_id:
                        self.canvas.delete(self.image_id)
                    self.image_id = self.canvas.create_image(0, 0, anchor=tk.NW, image=self.img_tk)

               
            except Exception as e:  
                print(e)
                tkmessagebox.showerror("Erreur",str(e))

        # Get the current page object
        

    def prev_page(self):
        if self.page_num > 1:
            self.page_num -= 1
            self.load_page()

    def next_page(self):
        if self.page_num < len(PyPDF2.PdfReader(open(self.filename, 'rb')).pages):
            self.page_num += 1
            self.load_page()

# Create the Tkinter interface
root = tk.Tk()
root.title("PDF Viewer")

# Instantiate the PDFViewer class, passing the filename
viewer = PDFViewer(root, "articles.pdf")
viewer.pack(fill=tk.BOTH, expand=True)

# Start the main event loop
root.mainloop()
