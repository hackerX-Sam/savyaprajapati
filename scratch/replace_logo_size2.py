import os

workspace_dir = r'c:\Users\samir\OneDrive\Desktop\confidential\ninaanddarek.com'
target = '<img src="https://ik.imagekit.io/logicsync/ChatGPT%20Image%20Jun%2017,%202026,%2010_32_37%20PM.png" alt="Sabhya Prajapati Logo" style="height: 100px; width: auto;" />'
replacement = '<img src="https://ik.imagekit.io/logicsync/ChatGPT%20Image%20Jun%2017,%202026,%2010_32_37%20PM.png" alt="Sabhya Prajapati Logo" style="height: 150px; width: auto;" />'

count = 0

for root, dirs, files in os.walk(workspace_dir):
    for file in files:
        if file.endswith('.html') or file.endswith('.1'):
            filepath = os.path.join(root, file)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                if target in content:
                    content = content.replace(target, replacement)
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(content)
                    count += 1
            except Exception as e:
                print(f"Error processing {filepath}: {e}")

print(f"Total files updated to 150px: {count}")
