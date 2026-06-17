import os
import re
import glob

html_files = glob.glob('*.html')

header_logo_pattern = re.compile(
    r'<a href="index\.html" class="logo">\s*<i class="fa-solid fa-brain"[^>]*></i>\s*<span>.*?</span>\s*</a>',
    re.IGNORECASE | re.DOTALL
)

new_header_logo = '''<a href="index.html" class="logo" style="display: flex; align-items: center; text-decoration: none;">
                <img src="images/VERTICAL LOGO.png" alt="Brain Yoga" style="height: 100px; object-fit: contain;">
            </a>'''

footer_logo_pattern = re.compile(
    r'<a href="index\.html" class="logo">\s*<i class="fa-solid fa-brain"[^>]*></i>\s*<span>.*?</span>\s*</a>',
    re.IGNORECASE | re.DOTALL
)

new_footer_logo = '''<a href="index.html" class="logo" style="display: flex; align-items: center; text-decoration: none; margin-bottom: 15px;">
                        <img src="images/VERTICAL LOGO.png" alt="Brain Yoga" style="height: 80px; object-fit: contain; filter: brightness(0) invert(1);">
                    </a>'''

for filepath in html_files:
    with open(filepath, 'r') as f:
        content = f.read()
    
    # First replace footer logos (we'll identify footer context simply by looking at the whole file)
    # Actually, the footer and header logos have identical HTML structure in my code except for text/color.
    # We can replace the first occurrence with header logo and the second with footer logo, OR
    # just replace all occurrences with a single logo variable and let CSS handle it.
    # To be safe, I'll split by </header> or <footer...
    
    if '</header>' in content:
        parts = content.split('</header>')
        # Replace in header
        parts[0] = header_logo_pattern.sub(new_header_logo, parts[0])
        # Replace in rest (footer)
        parts[1] = footer_logo_pattern.sub(new_footer_logo, parts[1])
        content = '</header>'.join(parts)
    else:
        content = header_logo_pattern.sub(new_header_logo, content)
        
    with open(filepath, 'w') as f:
        f.write(content)

print("Replaced logos in all HTML files.")
