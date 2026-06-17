import docx
import glob
import os

docx_files = glob.glob("All pages/PROGRAMMES/*.docx")

for file in docx_files:
    print(f"--- {os.path.basename(file)} ---")
    doc = docx.Document(file)
    for i, table in enumerate(doc.tables):
        print(f"Table {i+1}:")
        for row in table.rows:
            row_data = [cell.text.replace('\n', ' ').strip() for cell in row.cells]
            print(" | ".join(row_data))
    print()
