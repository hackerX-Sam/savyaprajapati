import re

with open('stories.1', 'r', encoding='utf-8') as f:
    html = f.read()

# Force header to be relative
style_to_inject = '''
<style>
body:not(.home) header[data-elementor-type="header"],
body:not(.home) .elementor-location-header,
body:not(.home) .elementor-sticky {
    position: relative !important;
    top: auto !important;
}
</style>
</head>
'''
html = html.replace('</head>', style_to_inject)

# Remove the margin-top: 250px from the iframe container
html = html.replace('margin-top: 250px;', 'margin-top: 0px;')

with open('stories.1', 'w', encoding='utf-8') as f:
    f.write(html)
print('Updated stories.1')
