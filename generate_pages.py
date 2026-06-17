import os
import re

def main():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract header to Programs Grid
    header_end = content.find('<!-- Hero Section -->')
    footer_start = content.find('<!-- Footer -->')

    if header_end == -1 or footer_start == -1:
        print("Couldn't find markers in index.html")
        return

    header = content[:header_end]
    footer = content[footer_start:]

    pages = [
        ('about', 'About Us'),
        ('programs', 'Programs'),
        ('admissions', 'Admissions'),
        ('faqs', 'FAQs'),
        ('gallery', 'Gallery'),
        ('workshops', 'Workshops'),
        ('blogs', 'Blogs'),
        ('contact', 'Contact')
    ]

    for page, title in pages:
        # Update active state in header
        page_header = header.replace('class="active"', '')
        page_header = page_header.replace(f'href="{page}.html"', f'href="{page}.html" class="active"')

        # Build new page content
        new_content = page_header + f"""
    <!-- Main Content for {title} -->
    <section class="hero" style="min-height: 40vh; padding: 160px 0 60px; text-align: center; display: block; background: var(--cream);">
        <div class="container">
            <h1 class="text-gradient" style="font-size: 3.5rem; margin-bottom: 24px;">{title}</h1>
            <p class="section-subtitle">Discover the full details about {title} at Brain Yoga Classes.</p>
        </div>
    </section>
""" + footer

        with open(f'{page}.html', 'w', encoding='utf-8') as pf:
            pf.write(new_content)

    print("Successfully generated 8 sub-pages with exact header and footer.")

if __name__ == '__main__':
    main()
