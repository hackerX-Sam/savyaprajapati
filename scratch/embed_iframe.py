import re

iframe_html = '''
<div style="width: 100%; height: 100vh; margin-top: 150px; margin-bottom: 50px;">
    <iframe src="https://weddingsbysabhya.pic-time.com/client" width="100%" height="100%" frameborder="0" allowfullscreen></iframe>
</div>
'''

for filepath in ['c:/Users/samir/OneDrive/Desktop/confidential/ninaanddarek.com/stories.1', 'c:/Users/samir/OneDrive/Desktop/confidential/ninaanddarek.com/stories/index.html']:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except:
        print(f"Could not read {filepath}")
        continue
    
    # We want to replace everything between </header> and <footer
    # So we'll use regex to find </header>.*<footer (with DOTALL)
    pattern = re.compile(r'(</header>)(.*?)(<footer)', re.DOTALL)
    
    if pattern.search(content):
        new_content = pattern.sub(r'\g<1>' + iframe_html + r'\g<3>', content)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Embedded iframe in {filepath}")
    else:
        print(f"Could not find header/footer boundary in {filepath}")
