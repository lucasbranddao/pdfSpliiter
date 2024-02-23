import PyPDF2
import os

def split_pdf(pdf_path):
    # Open the original PDF
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        num_pages = len(pdf_reader.pages)
        
        # Directory where the split PDFs will be saved
        output_directory = os.path.splitext(pdf_path)[0] + '_split'
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)
        
        # Creating a PDF for each page
        for i in range(num_pages):
            pdf_writer = PyPDF2.PdfWriter()
            pdf_writer.add_page(pdf_reader.pages[i])
            
            # Saving the PDF of the current page
            output_filename = os.path.join(output_directory, f'page_{i+1}.pdf')
            with open(output_filename, 'wb') as output_file:
                pdf_writer.write(output_file)
            
            print(f'Page {i+1} saved as {output_filename}')

# Replace 'path_to_your_pdf.pdf' with the path to your PDF file
split_pdf('path_to_your_pdf.pdf')
