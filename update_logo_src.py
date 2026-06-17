import glob
import re

html_files = glob.glob('*.html')

for filepath in html_files:
    with open(filepath, 'r') as file:
        content = file.read()
    
    # Update all instances of VERTICAL LOGO.png or similar to New logo.jpg
    content = re.sub(r'src="images/VERTICAL LOGO\.png"', 'src="images/New logo.jpg"', content)
    content = re.sub(r'src="images/VERTICAL%20LOGO\.png"', 'src="images/New logo.jpg"', content)
    
    with open(filepath, 'w') as file:
        file.write(content)

print(f"Updated {len(html_files)} files with new logo src.")
