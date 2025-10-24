from pypdf import PdfReader
import os

def extract_text_from_pdf(pdf_path, start_page, end_page):
    reader = PdfReader(pdf_path)
    text = ""
    
    # Extract text from specified page range
    for page_num in range(start_page - 1, end_page):
        page = reader.pages[page_num]
        text += page.extract_text() + " "
    
    # Create output filename based on PDF name
    basename, extension = os.path.splitext(pdf_path)
    output_file = basename + ".txt"
    
    # Write to text file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(text)
    
    print(f"Text extracted and saved to {output_file}")
    return text

pdf_file = "Harry Potter 4 - Harry Potter and the Goblet of Fire - 4 - Harry Potter and the Goblet of Fire.pdf"
start = 7  
end = 740

extracted_text = extract_text_from_pdf(pdf_file, start, end)
