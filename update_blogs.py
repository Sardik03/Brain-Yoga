import re

# Read the extracted text
with open("blogs_content.txt", "r", encoding="utf-8") as f:
    text = f.read()

blogs = text.split("--- BLOG")
blogs = [b for b in blogs if b.strip()]

html_modals = []

for idx, blog in enumerate(blogs):
    lines = blog.split('\n')
    
    # Extract title from the FILENAME line or Meta Title
    meta_title = ""
    content_lines = []
    
    in_content = False
    for line in lines:
        line = line.strip()
        if not line:
            continue
        if line == "---":
            in_content = True
            continue
        if line.startswith("FILENAME:"):
            title = line.replace("FILENAME:", "").strip().replace(".docx", "").replace("_", "")
        if in_content:
            content_lines.append(line)
            
    # Now generate the HTML body
    body_html = f"            <div class=\"modal-body\">\n"
    body_html += f"                <h2>{title}</h2>\n"
    
    in_list = False
    
    for line in content_lines:
        if line == "---":
            body_html += "                <hr>\n"
            if in_list:
                in_list = False
                body_html += "                </ul>\n"
        elif line.startswith("🟣"):
            if in_list:
                in_list = False
                body_html += "                </ul>\n"
            h3_text = line.replace("🟣", "").strip()
            body_html += f"                <h3>{h3_text}</h3>\n"
        elif not line.endswith(".") and not line.endswith("?") and not line.endswith("!") and not line.startswith("Address:") and not line.startswith("Phone:") and len(line) < 80:
            # Heuristic for lists: lines that don't end in punctuation and are relatively short, immediately following a paragraph
            if not in_list:
                in_list = True
                body_html += "                <ul>\n"
            body_html += f"                    <li>{line}</li>\n"
        else:
            if in_list:
                in_list = False
                body_html += "                </ul>\n"
            body_html += f"                <p>{line}</p>\n"
            
    if in_list:
        body_html += "                </ul>\n"
        
    body_html += "            </div>"
    html_modals.append(body_html)

# Now read blogs.html and replace the modal bodies
with open("blogs.html", "r", encoding="utf-8") as f:
    html_content = f.read()

for i in range(1, 5):
    # Find the modal body
    pattern = rf'<div id="modal{i}" class="modal">.*?<div class="modal-content">.*?<span class="close-modal" onclick="closeModal\(\'modal{i}\'\)">&times;</span>\s*<div class="modal-body">.*?</div>\s*</div>\s*</div>'
    
    # We can replace the <div class="modal-body">...</div> using regex
    body_pattern = rf'(<div id="modal{i}" class="modal">.*?<span class="close-modal" onclick="closeModal\(\'modal{i}\'\)">&times;</span>\s*)<div class="modal-body">.*?</div>(\s*</div>\s*</div>)'
    
    replacement = r'\1' + html_modals[i-1].replace('\\', '\\\\') + r'\2'
    html_content = re.sub(body_pattern, replacement, html_content, flags=re.DOTALL)
    
with open("blogs.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Updated blogs.html")
