import re

def extract_links(html):
    pattern = r'<a\s+href=["\']([^"\']+)["\']'
    return re.findall(pattern, html)

# Example
html = '<a href="https://example.com">Example</a> <a href="https://another.com">Another</a>'
links = extract_links(html)
print(links)  

# Output: ['https://example.com', 'https://another.com']
