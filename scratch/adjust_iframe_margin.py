import os

old_wrapper = '<div style="width: 100%; height: 100vh; margin-top: 150px; margin-bottom: 50px;">'
new_wrapper = '<div style="width: 100%; height: 100vh; margin-top: 250px; margin-bottom: 0px;">'

for filepath in ['c:/Users/samir/OneDrive/Desktop/confidential/ninaanddarek.com/stories.1', 'c:/Users/samir/OneDrive/Desktop/confidential/ninaanddarek.com/stories/index.html']:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f'Could not read {filepath}: {e}')
        continue
        
    if old_wrapper in content:
        new_content = content.replace(old_wrapper, new_wrapper)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f'Updated margin in {filepath}')
    else:
        print(f'Could not find old wrapper in {filepath}')
