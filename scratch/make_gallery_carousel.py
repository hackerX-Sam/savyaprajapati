import re

gallery_path = r'c:\Users\samir\OneDrive\Desktop\confidential\ninaanddarek.com\gallery.1'

with open(gallery_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Find the section
section_start = content.find('<section class="custom-gradient-gallery-section"')
section_end = content.find('</section>', section_start)

if section_start != -1 and section_end != -1:
    section_end += len('</section>')
    section_html = content[section_start:section_end]
    
    # Extract the gallery grid
    grid_start = section_html.find('<div class="custom-gradient-gallery"')
    grid_end = section_html.rfind('</div>') # end of grid container
    
    # We need to extract all gallery-cell divs
    cells = re.findall(r'<div class="gallery-cell".*?</div>\s*</div>', section_html, flags=re.DOTALL)
    
    # Duplicate them (40 -> 80)
    duplicated_cells = cells * 2
    
    new_cells_html = '\n'.join(duplicated_cells)
    
    # Rebuild the gallery grid with new styles
    new_grid_html = f"""
    <div class="gallery-carousel-wrapper" style="position: relative; width: 100%; display: flex; align-items: center;">
        <button class="gallery-btn gallery-btn-left" aria-label="Scroll left" style="position: absolute; left: 20px; z-index: 100; width: 50px; height: 50px; border-radius: 50%; background: rgba(0,0,0,0.6); color: white; border: 1px solid rgba(255,255,255,0.2); font-size: 24px; cursor: pointer; display: flex; align-items: center; justify-content: center; backdrop-filter: blur(5px); box-shadow: 0 4px 15px rgba(0,0,0,0.3); transition: all 0.3s ease;">&#10094;</button>
        
        <div class="custom-gradient-gallery" style="display: grid; grid-template-rows: repeat(4, 1fr); grid-auto-columns: calc(100% / 10); grid-auto-flow: column; gap: 0; width: 100%; overflow-x: scroll; scrollbar-width: none; -ms-overflow-style: none;">
            {new_cells_html}
        </div>
        
        <button class="gallery-btn gallery-btn-right" aria-label="Scroll right" style="position: absolute; right: 20px; z-index: 100; width: 50px; height: 50px; border-radius: 50%; background: rgba(0,0,0,0.6); color: white; border: 1px solid rgba(255,255,255,0.2); font-size: 24px; cursor: pointer; display: flex; align-items: center; justify-content: center; backdrop-filter: blur(5px); box-shadow: 0 4px 15px rgba(0,0,0,0.3); transition: all 0.3s ease;">&#10095;</button>
    </div>
    
    <style>
        .custom-gradient-gallery::-webkit-scrollbar {{
            display: none;
        }}
        .gallery-btn:hover {{
            background: rgba(0,0,0,0.8) !important;
            transform: scale(1.1);
        }}
        @media (max-width: 1024px) {{
            .custom-gradient-gallery {{
                grid-auto-columns: calc(100% / 6) !important;
            }}
        }}
        @media (max-width: 768px) {{
            .custom-gradient-gallery {{
                grid-auto-columns: calc(100% / 4) !important;
            }}
        }}
        @media (max-width: 480px) {{
            .custom-gradient-gallery {{
                grid-auto-columns: calc(100% / 2) !important;
            }}
        }}
    </style>
    
    <script>
        document.addEventListener('DOMContentLoaded', function() {{
            const gallery = document.querySelector('.custom-gradient-gallery');
            const btnLeft = document.querySelector('.gallery-btn-left');
            const btnRight = document.querySelector('.gallery-btn-right');
            
            if (btnLeft && btnRight && gallery) {{
                btnLeft.addEventListener('click', function() {{
                    gallery.scrollBy({{ left: -gallery.clientWidth / 2, behavior: 'smooth' }});
                }});
                
                btnRight.addEventListener('click', function() {{
                    gallery.scrollBy({{ left: gallery.clientWidth / 2, behavior: 'smooth' }});
                }});
            }}
        }});
    </script>
    """
    
    # We replace the old section with a new section containing the wrapper
    new_section_html = f"""<section class="custom-gradient-gallery-section" style="width: 100%; margin: 60px 0; overflow: hidden; display: flex; justify-content: center; padding: 0;">
{new_grid_html}
</section>"""
    
    content = content.replace(section_html, new_section_html)
    
    with open(gallery_path, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print("Gallery converted to interactive carousel successfully.")
else:
    print("Could not find gallery section.")
