import os
try:
    import docx
except ImportError:
    os.system("pip3 install python-docx")
    import docx

blog_dir = "All pages/BLOGS"
files = [
    "Turn Weak Memory Into Strong Recall With The Right Learning Methods For Your Child_.docx",
    "Turn Your Child’s Low Focus Into Sharp Concentration With The Right Training_.docx",
    "Make Numbers Easy And Build Strong Thinking Skills In Your Child With The Right Maths Approach_.docx",
    "Bridge The Gap Between Learning And Speaking With The Best Spoken English Classes For Your Child.docx"
]

with open("blogs_content.txt", "w", encoding="utf-8") as f:
    for idx, filename in enumerate(files):
        f.write(f"\n\n--- BLOG {idx+1} ---\n")
        f.write(f"FILENAME: {filename}\n\n")
        path = os.path.join(blog_dir, filename)
        
        try:
            doc = docx.Document(path)
            for para in doc.paragraphs:
                if para.text.strip():
                    f.write(f"{para.text}\n")
        except Exception as e:
            f.write(f"Error reading file: {e}\n")

print("Finished parsing blogs.")
