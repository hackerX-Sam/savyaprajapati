import os

file_path = r"c:\Users\samir\OneDrive\Desktop\confidential\ninaanddarek.com\index.html"

with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

custom_grid_css = """
<style>
/* Make recent stories grid smaller and standard */
.elementor-element-f3850b1 {
    max-width: 900px !important;
    margin-left: auto !important;
    margin-right: auto !important;
}
/* Make all frames standard (1:1 Square) */
.elementor-element-f3850b1 .elementor-post__thumbnail__link {
    padding-bottom: 100% !important;
}
.elementor-element-f3850b1 .elementor-portfolio-item__img img {
    object-fit: cover !important;
}
</style>
"""

# Append to the end of <head> or right before our previous <section class="custom-hero-section">
html = html.replace('<section class="custom-hero-section"', custom_grid_css + '\n<section class="custom-hero-section"')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Stories grid updated successfully.")
