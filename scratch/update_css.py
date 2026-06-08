css_path = r"c:\Users\samir\OneDrive\Desktop\confidential\ninaanddarek.com\wp-content\uploads\elementor\css\post-10.css@ver=1780039997"

with open(css_path, "r", encoding="utf-8") as f:
    content = f.read()

# Replace background-position:center 70%; in the dfd99d5 selectors with center 80%
# 1. Desktop version:
target1 = '.elementor-10 .elementor-element.elementor-element-dfd99d5:not(.elementor-motion-effects-element-type-background), .elementor-10 .elementor-element.elementor-element-dfd99d5 > .elementor-motion-effects-container > .elementor-motion-effects-layer{background-image:url("https://ik.imagekit.io/logicsync/tr:w-2000/photo%202.JPG");background-position:center 70%;'
replacement1 = '.elementor-10 .elementor-element.elementor-element-dfd99d5:not(.elementor-motion-effects-element-type-background), .elementor-10 .elementor-element.elementor-element-dfd99d5 > .elementor-motion-effects-container > .elementor-motion-effects-layer{background-image:url("https://ik.imagekit.io/logicsync/tr:w-2000/photo%202.JPG");background-position:center 80%;'

# 2. @media(max-width:959px) version:
target2 = 'dfd99d5:not(.elementor-motion-effects-element-type-background), .elementor-10 .elementor-element.elementor-element-dfd99d5 > .elementor-motion-effects-container > .elementor-motion-effects-layer{background-position:center 70%;background-size:cover;}'
replacement2 = 'dfd99d5:not(.elementor-motion-effects-element-type-background), .elementor-10 .elementor-element.elementor-element-dfd99d5 > .elementor-motion-effects-container > .elementor-motion-effects-layer{background-position:center 80%;background-size:cover;}'

# 3. @media(max-width:767px) version:
target3 = '@media(max-width:767px){.elementor-10 .elementor-element.elementor-element-dfd99d5:not(.elementor-motion-effects-element-type-background), .elementor-10 .elementor-element.elementor-element-dfd99d5 > .elementor-motion-effects-container > .elementor-motion-effects-layer{background-image:url("https://ik.imagekit.io/logicsync/tr:w-2000/photo%202.JPG");background-position:center 70%;'
replacement3 = '@media(max-width:767px){.elementor-10 .elementor-element.elementor-element-dfd99d5:not(.elementor-motion-effects-element-type-background), .elementor-10 .elementor-element.elementor-element-dfd99d5 > .elementor-motion-effects-container > .elementor-motion-effects-layer{background-image:url("https://ik.imagekit.io/logicsync/tr:w-2000/photo%202.JPG");background-position:center 80%;'

if target1 in content:
    content = content.replace(target1, replacement1)
    print("Updated block 1 (70% -> 80%)")
else:
    print("Warning: target1 not found!")

if target2 in content:
    content = content.replace(target2, replacement2)
    print("Updated block 2 (70% -> 80%)")
else:
    print("Warning: target2 not found!")

if target3 in content:
    content = content.replace(target3, replacement3)
    print("Updated block 3 (70% -> 80%)")
else:
    print("Warning: target3 not found!")

with open(css_path, "w", encoding="utf-8") as f:
    f.write(content)

print("CSS saved.")
