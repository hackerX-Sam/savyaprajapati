import re

file_path = r"c:\Users\samir\OneDrive\Desktop\confidential\ninaanddarek.com\index.html"

with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Replace menu 1
menu1_pattern = re.compile(r'(<ul id="menu-1-fdcd67e" class="elementor-nav-menu">)(.*?)(</ul>)', re.DOTALL)
new_menu1 = r'''\1
    <li class="menu-item"><a href="/" class="elementor-item">HOME</a></li>
    <li class="menu-item"><a href="javascript:void(0);" class="elementor-item">GALLERIES</a></li>
    <li class="menu-item"><a href="https://weddingsbysabhya.pic-time.com/client" target="_blank" rel="noopener noreferrer" class="elementor-item">STORIES</a></li>
    <li class="menu-item"><a href="javascript:void(0);" class="elementor-item">TESTIMONIALS</a></li>
    <li class="menu-item"><a href="about.1" class="elementor-item">ABOUT</a></li>
    <li class="menu-item"><a href="contact.1" class="elementor-item">ENQUIRE</a></li>
\3'''
html = menu1_pattern.sub(new_menu1, html)

# 2. Replace menu 2
menu2_pattern = re.compile(r'(<ul id="menu-2-fdcd67e" class="elementor-nav-menu">)(.*?)(</ul>)', re.DOTALL)
new_menu2 = r'''\1
    <li class="menu-item"><a href="/" class="elementor-item" tabindex="-1">HOME</a></li>
    <li class="menu-item"><a href="javascript:void(0);" class="elementor-item" tabindex="-1">GALLERIES</a></li>
    <li class="menu-item"><a href="https://weddingsbysabhya.pic-time.com/client" target="_blank" rel="noopener noreferrer" class="elementor-item" tabindex="-1">STORIES</a></li>
    <li class="menu-item"><a href="javascript:void(0);" class="elementor-item" tabindex="-1">TESTIMONIALS</a></li>
    <li class="menu-item"><a href="about.1" class="elementor-item" tabindex="-1">ABOUT</a></li>
    <li class="menu-item"><a href="contact.1" class="elementor-item" tabindex="-1">ENQUIRE</a></li>
\3'''
html = menu2_pattern.sub(new_menu2, html)

# 3. Inject new Hero section and CSS
custom_hero_and_css = """
<style>
/* Header Centering */
.elementor-element-5ad641f > .elementor-widget-wrap {
    display: flex !important;
    flex-direction: column !important;
    align-items: center !important;
}
.elementor-element-785a0c6 {
    margin-bottom: 20px !important;
}
.elementor-nav-menu--main {
    justify-content: center !important;
}
.elementor-nav-menu a.elementor-item {
    color: #000000 !important;
    font-size: 13px !important;
    letter-spacing: 2px !important;
}

/* Hide old hero elements */
.elementor-element-dfd99d5,
.elementor-element-e334e2c > .elementor-container > .elementor-column > .elementor-widget-wrap > .elementor-widget-image,
.elementor-element-2e21037,
.elementor-element-c8ef57b,
.elementor-element-69824e2 {
    display: none !important;
}
</style>

<section class="custom-hero-section" style="max-width: 1200px; margin: 40px auto; position: relative; padding: 0 20px;">
    <div class="custom-hero-slider" style="position: relative; width: 100%; aspect-ratio: 16/9; overflow: hidden; display: flex; align-items: center; justify-content: center;">
        <img src="https://ik.imagekit.io/logicsync/tr:w-2000/photo%202.JPG" style="width: 100%; height: 100%; object-fit: cover;" alt="Hero Image">
        
        <div class="slider-arrow left-arrow" style="position: absolute; left: 20px; top: 50%; transform: translateY(-50%); width: 40px; height: 40px; background: rgba(0,0,0,0.3); color: #fff; display: flex; align-items: center; justify-content: center; cursor: pointer; border-radius: 50%;">
            <svg viewBox="0 0 24 24" width="24" height="24" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"><polyline points="15 18 9 12 15 6"></polyline></svg>
        </div>
        
        <div class="slider-arrow right-arrow" style="position: absolute; right: 20px; top: 50%; transform: translateY(-50%); width: 40px; height: 40px; background: rgba(0,0,0,0.3); color: #fff; display: flex; align-items: center; justify-content: center; cursor: pointer; border-radius: 50%;">
            <svg viewBox="0 0 24 24" width="24" height="24" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"><polyline points="9 18 15 12 9 6"></polyline></svg>
        </div>
    </div>
</section>
"""

if "custom-hero-section" not in html:
    hero_pattern = re.compile(r'(<section[^>]*data-id="dfd99d5"[^>]*>)')
    html = hero_pattern.sub(custom_hero_and_css + r'\n\1', html)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("HTML updated successfully.")
