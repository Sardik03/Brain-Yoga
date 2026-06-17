import re

with open("blogs.html", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update CSS
css_additions = """
        .modal-body h3 {
            color: var(--color-purple-dark);
            margin-top: 2.5rem;
            margin-bottom: 1.2rem;
            font-size: 1.4rem;
            position: relative;
            padding-bottom: 0.5rem;
            font-weight: 700;
        }
        
        .modal-body h3::after {
            content: '';
            position: absolute;
            bottom: 0;
            left: 0;
            width: 60px;
            height: 4px;
            background: var(--color-purple-gradient);
            border-radius: 2px;
        }

        .modal-body ul {
            list-style: none;
            padding-left: 0;
            margin-top: 1rem;
            margin-bottom: 1.5rem;
        }
        
        .modal-body li {
            position: relative;
            padding-left: 2rem;
            margin-bottom: 0.8rem;
            font-weight: 500;
            color: #333;
        }
        
        .modal-body li::before {
            content: '🟣';
            position: absolute;
            left: 0;
            top: 2px;
            font-size: 0.8rem;
        }
        
        .highlight-brand {
            font-weight: 800;
            color: var(--color-purple-dark);
            background: linear-gradient(120deg, var(--color-purple-light) 0%, transparent 100%);
            padding: 2px 6px;
            border-radius: 6px;
            display: inline-block;
        }
        
        .modal-body p {
            margin-bottom: 1.2rem;
            letter-spacing: 0.2px;
        }
"""

# Replace old .modal-body CSS
content = re.sub(
    r'\.modal-body h3 \{.*?\n\s*\}', 
    '', 
    content, 
    flags=re.DOTALL
)
content = re.sub(
    r'\.modal-body ul \{.*?\n\s*\}', 
    '', 
    content, 
    flags=re.DOTALL
)
content = re.sub(
    r'\.modal-body li \{.*?\n\s*\}', 
    '', 
    content, 
    flags=re.DOTALL
)

# Insert new CSS just before </style>
content = content.replace('</style>', css_additions + '\n    </style>')

# 2. Highlight text in modal body
# We only want to replace text inside <div class="modal-body"> ... </div>
# But to be safe, replacing "Brain Yoga Classes" globally in the body is fine (won't hurt the rest of the text if any).
# Actually, it might mess up alt text or other attributes if we're not careful. Let's do it carefully.

def highlight_text(match):
    body_text = match.group(0)
    body_text = re.sub(r'\b(Brain Yoga Classes)\b', r'<span class="highlight-brand">\1</span>', body_text)
    # Also highlight "Brain Yoga" if it's not followed by "Classes" (using negative lookahead)
    body_text = re.sub(r'\b(Brain Yoga)(?! Classes)\b', r'<span class="highlight-brand">\1</span>', body_text)
    # Let's also bold "Abacus", "Vedic Maths"
    body_text = re.sub(r'\b(Abacus)\b', r'<strong>\1</strong>', body_text)
    body_text = re.sub(r'\b(Vedic Maths)\b', r'<strong>\1</strong>', body_text)
    return body_text

content = re.sub(r'(<div class="modal-body">.*?</div>\s*</div>)', highlight_text, content, flags=re.DOTALL)

with open("blogs.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Enhanced blogs.html")
