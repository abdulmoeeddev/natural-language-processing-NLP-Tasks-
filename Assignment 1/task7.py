import re

def extract_hex_colors(css_text):
    pattern = r"#[0-9A-Fa-f]{3}(?:[0-9A-Fa-f]{3})?"
    return re.findall(pattern, css_text)

# Example
css_text = "Colors: #FFF, #FFAABB, and #123456."
hex_colors = extract_hex_colors(css_text)
print(hex_colors)  

# Output: ['#FFF', '#FFAABB', '#123456']
