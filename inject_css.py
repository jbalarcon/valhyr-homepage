#!/usr/bin/env python3
import re

# Read the custom CSS
with open('/Users/jean-baptistealarcon/coding/valhyr/header-redesign.css', 'r') as f:
    custom_css = f.read()

# Read the HTML file
with open('/Users/jean-baptistealarcon/coding/valhyr/homepage-redesigned.html', 'r') as f:
    html_content = f.read()

# Find the position after the marker and inject our CSS
marker = '/* Prevent flash when clicking arrow */'
marker_pos = html_content.find(marker)

if marker_pos != -1:
    # Find the end of that comment line
    end_of_line = html_content.find('\n', marker_pos)
    if end_of_line == -1:
        end_of_line = html_content.find('</style>', marker_pos)
    
    # Insert our custom CSS
    html_content = (
        html_content[:end_of_line] + 
        '\n\n' + custom_css + '\n' +
        html_content[end_of_line:]
    )
    
    # Write back
    with open('/Users/jean-baptistealarcon/coding/valhyr/homepage-redesigned.html', 'w') as f:
        f.write(html_content)
    
    print("✓ CSS successfully injected")
else:
    print("✗ Marker not found")
