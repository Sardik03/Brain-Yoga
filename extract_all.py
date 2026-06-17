import os
import glob
from pypdf import PdfReader
from docx import Document

out_file = 'extracted_pages.txt'

def read_pdf(filepath):
    try:
        reader = PdfReader(filepath)
        text = ''
        for page in reader.pages:
            text += page.extract_text() + '\n'
        return text
    except Exception as e:
        return f"Error reading PDF: {e}"

def read_docx(filepath):
    try:
        doc = Document(filepath)
        return '\n'.join([p.text for p in doc.paragraphs])
    except Exception as e:
        return f"Error reading DOCX: {e}"

with open(out_file, 'w', encoding='utf-8') as f:
    for root, dirs, files in os.walk('All pages'):
        for file in files:
            path = os.path.join(root, file)
            f.write(f"\\n\\n{'='*50}\\nFILE: {path}\\n{'='*50}\\n")
            if file.endswith('.pdf'):
                f.write(read_pdf(path))
            elif file.endswith('.docx'):
                f.write(read_docx(path))
            elif file.endswith('.txt'):
                with open(path, 'r', encoding='utf-8') as tf:
                    f.write(tf.read())

print("Extraction complete.")
