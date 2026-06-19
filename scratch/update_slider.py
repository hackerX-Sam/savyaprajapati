import os
import re

file_path = r"c:\Users\samir\OneDrive\Desktop\confidential\ninaanddarek.com\index.html"

with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

new_hero = """
<section class="custom-hero-section" style="max-width: 1200px; margin: 40px auto; position: relative; padding: 0 20px;">
    <div class="custom-hero-slider" style="position: relative; width: 100%; aspect-ratio: 16/9; overflow: hidden; display: flex; align-items: center; justify-content: center; border-radius: 4px;">
        <img id="hero-slider-img" src="https://ik.imagekit.io/logicsync/tr:w-2000/photo%202.JPG" style="width: 100%; height: 100%; object-fit: cover; transition: opacity 0.3s ease-in-out;" alt="Hero Image">
        
        <div class="slider-arrow left-arrow" onclick="prevSlide()" style="position: absolute; left: 20px; top: 50%; transform: translateY(-50%); width: 45px; height: 45px; background: rgba(255,255,255,0.6); backdrop-filter: blur(5px); -webkit-backdrop-filter: blur(5px); color: #000; display: flex; align-items: center; justify-content: center; cursor: pointer; border-radius: 50%; transition: background 0.3s;">
            <svg viewBox="0 0 24 24" width="24" height="24" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"><polyline points="15 18 9 12 15 6"></polyline></svg>
        </div>
        
        <div class="slider-arrow right-arrow" onclick="nextSlide()" style="position: absolute; right: 20px; top: 50%; transform: translateY(-50%); width: 45px; height: 45px; background: rgba(255,255,255,0.6); backdrop-filter: blur(5px); -webkit-backdrop-filter: blur(5px); color: #000; display: flex; align-items: center; justify-content: center; cursor: pointer; border-radius: 50%; transition: background 0.3s;">
            <svg viewBox="0 0 24 24" width="24" height="24" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"><polyline points="9 18 15 12 9 6"></polyline></svg>
        </div>
    </div>
</section>

<script>
    const images = [
        "https://ik.imagekit.io/logicsync/tr:w-2000/photo%202.JPG",
        "https://ik.imagekit.io/logicsync/IMG.112.jpg?updatedAt=1780925347803",
        "https://ik.imagekit.io/logicsync/0eba3533-9e9f-4609-b167-5d137b160e3e.jpg",
        "https://ik.imagekit.io/logicsync/ce247119-0ef3-483f-90f3-a0275ec101d1.jpg?updatedAt=1780925325760"
    ];
    let currentIndex = 0;
    const heroImg = document.getElementById('hero-slider-img');

    function updateSlide() {
        heroImg.style.opacity = '0.6';
        setTimeout(() => {
            heroImg.src = images[currentIndex];
            heroImg.style.opacity = '1';
        }, 150);
    }

    function prevSlide() {
        currentIndex = (currentIndex > 0) ? currentIndex - 1 : images.length - 1;
        updateSlide();
    }

    function nextSlide() {
        currentIndex = (currentIndex < images.length - 1) ? currentIndex + 1 : 0;
        updateSlide();
    }
    
    // Auto-advance every 5 seconds
    setInterval(nextSlide, 5000);
</script>
"""

pattern = re.compile(r'<section class="custom-hero-section".*?</section>', re.DOTALL)
if pattern.search(html):
    html = pattern.sub(new_hero, html)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print("Updated slider and arrows successfully.")
else:
    print("Could not find the custom hero section.")
