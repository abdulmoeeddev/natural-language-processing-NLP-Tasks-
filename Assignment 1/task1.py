import re

def extract_domain(url):
    pattern = r"(?:https?://)?(?:www\.)?([a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)+)"
    match = re.search(pattern, url)
    return match.group(1) if match else None

# Example
urls = [
    "https://www.example.com",
    "http://example.org",
    "https://sub.example.co.uk",
]
domains = [extract_domain(url) for url in urls]
print(domains) 
 
# Output: ['example.com', 'example.org', 'sub.example.co.uk']
