import os
import re

files = ['about.html', 'admissions.html', 'faqs.html', 'contact.html', 'blogs.html', 'programs.html']

for file in files:
    if not os.path.exists(file):
        print(f"Skipping {file}")
        continue
    with open(file, 'r') as f:
        content = f.read()

    # Find the navbar block
    navbar_pattern = re.compile(r'<!-- Navbar.*?-->\s*<nav class="navbar".*?</nav>', re.DOTALL)
    
    # Generate new navbar
    page = file.split('.')[0]
    
    new_nav = f'''    <!-- Header Navigation -->
    <header>
        <div class="container navbar">
            <a href="index.html" class="logo" style="display: flex; align-items: center; text-decoration: none;">
                <img src="images/VERTICAL LOGO.png" alt="Brain Yoga" style="height: 140px; object-fit: contain;">
            </a>
            <nav>
                <ul class="nav-links">
                    <li><a href="index.html">Home</a></li>
                    <li><a href="about.html"{' class="active"' if page == 'about' else ''}>About Us</a></li>
                    <li><a href="programs.html"{' class="active"' if page == 'programs' else ''}>Programs</a></li>
                    <li><a href="admissions.html"{' class="active"' if page == 'admissions' else ''}>Admissions</a></li>
                    <li><a href="faqs.html"{' class="active"' if page == 'faqs' else ''}>FAQs</a></li>
                    <li><a href="gallery.html">Gallery</a></li>
                    <li><a href="workshops.html">Workshops</a></li>
                    <li><a href="blogs.html"{' class="active"' if page == 'blogs' else ''}>Blogs</a></li>
                    <li><a href="contact.html"{' class="active"' if page == 'contact' else ''}>Contact</a></li>
                </ul>
            </nav>
        </div>
    </header>'''
    
    if navbar_pattern.search(content):
        content = navbar_pattern.sub(new_nav, content)
        print(f"Replaced navbar in {file}")
    
    # Find page header section
    content = content.replace('<header class="page-header"', '<section class="page-header"')
    # Find the closing </header> that comes before the next section
    content = re.sub(r'</header>\s*(?=\s*<!-- [A-Za-z]+ Section -->)', r'</section>', content)
    
    with open(file, 'w') as f:
        f.write(content)
        
