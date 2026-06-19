import os
import glob

css_dir = r"c:\Users\samir\OneDrive\Desktop\confidential\ninaanddarek.com\wp-content\uploads\elementor\css"
files = glob.glob(os.path.join(css_dir, "post-1297.css*"))

override_css = """
/* Light Mode Global Overrides */
html, body, .elementor-page, .elementor-kit-1297, .site-main {
    background-color: #FDFBF7 !important;
}

/* Force text colors to black */
h1, h2, h3, h4, h5, h6, p, span, a, div, 
.elementor-heading-title, .elementor-text-editor, 
.elementor-icon-box-title, .elementor-icon-box-description {
    color: #000000 !important;
}

/* Override dark section backgrounds by making them transparent so body shows through */
.elementor-section, .elementor-column, .elementor-background-overlay {
    background-color: transparent !important;
}

/* Fix buttons so they don't disappear */
.elementor-button, .elementor-button * {
    background-color: #222222 !important;
    color: #FFFFFF !important;
}

/* Fix custom logo hover if any */
.custom-logo-text:hover {
    color: #555555 !important;
}
"""

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Update kit base colors
    content = content.replace("background-color:#24211E;", "background-color:#FDFBF7 !important;")
    content = content.replace("color:#DDDDDD;", "color:#000000 !important;")
    
    if "Light Mode Global Overrides" not in content:
        content += override_css
        
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print(f"Updated {len(files)} Elementor global CSS files.")
