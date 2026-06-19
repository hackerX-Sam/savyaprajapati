import os

file_path = r"c:\Users\samir\OneDrive\Desktop\confidential\ninaanddarek.com\index.html"

with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Fix the first menu stray items
stray_1 = """</ul>
										</li>
										<li
											class="menu-item menu-item-type-post_type menu-item-object-page menu-item-94">
											<a href="contact.1" class="elementor-item">CONTACT</a></li>
									</ul>"""
html = html.replace(stray_1, "</ul>")

# Fix the second menu stray items
stray_2 = """</ul>
										</li>
										<li
											class="menu-item menu-item-type-post_type menu-item-object-page menu-item-94">
											<a href="contact.1" class="elementor-item" tabindex="-1">CONTACT</a></li>
									</ul>"""
html = html.replace(stray_2, "</ul>")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Removed stray CONTACT button.")
