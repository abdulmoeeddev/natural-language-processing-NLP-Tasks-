import re

def extract_prices(text):
    pattern = r"(?:[\$\€¥])\d+(?:,\d{3})*(?:\.\d{2})?"
    return re.findall(pattern, text)

# Example
text = "Prices are $100, €50, ¥5000, and $1,200.50."
prices = extract_prices(text)
print(prices)  

# Output: ['$100', '€50', '¥5000', '$1,200.50']
