import os
import re
import glob

html_files = glob.glob('*.html')

# The ideal nav links without the "Book a Demo" button
nav_links_html = '''            <nav>
                <ul class="nav-links">
                    <li><a href="index.html"{home_active}>Home</a></li>
                    <li><a href="about.html"{about_active}>About Us</a></li>
                    <li><a href="programs.html"{programs_active}>Programs</a></li>
                    <li><a href="admissions.html"{admissions_active}>Admissions</a></li>
                    <li><a href="faqs.html"{faqs_active}>FAQs</a></li>
                    <li><a href="gallery.html"{gallery_active}>Gallery</a></li>
                    <li><a href="workshops.html"{workshops_active}>Workshops</a></li>
                    <li><a href="blogs.html"{blogs_active}>Blogs</a></li>
                    <li><a href="contact.html"{contact_active}>Contact</a></li>
                </ul>
            </nav>'''

header_pattern = re.compile(r'<header>.*?</header>', re.IGNORECASE | re.DOTALL)

for filepath in html_files:
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Determine which page is active based on filename
    active_flags = {
        'home_active': ' class="active"' if filepath == 'index.html' else '',
        'about_active': ' class="active"' if filepath == 'about.html' else '',
        'programs_active': ' class="active"' if filepath == 'programs.html' else '',
        'admissions_active': ' class="active"' if filepath == 'admissions.html' else '',
        'faqs_active': ' class="active"' if filepath == 'faqs.html' else '',
        'gallery_active': ' class="active"' if filepath == 'gallery.html' else '',
        'workshops_active': ' class="active"' if filepath == 'workshops.html' else '',
        'blogs_active': ' class="active"' if filepath == 'blogs.html' else '',
        'contact_active': ' class="active"' if filepath == 'contact.html' else '',
    }
    
    page_nav = nav_links_html.format(**active_flags)
    
    new_header = f'''    <header>
        <div class="container navbar">
            <a href="index.html" class="logo" style="display: flex; align-items: center; text-decoration: none;">
                <img src="images/VERTICAL LOGO.png" alt="Brain Yoga" style="height: 140px; object-fit: contain;">
            </a>
{page_nav}
        </div>
    </header>'''
    
    if '<header>' in content:
        content = header_pattern.sub(new_header, content)
        with open(filepath, 'w') as f:
            f.write(content)

print("Headers standardized across all HTML files.")
