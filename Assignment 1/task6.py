import re

def extract_addresses(text):
    pattern = r"\d+\s\w+\s(?:St|Street|Ave|Avenue|Rd|Road|Blvd|Boulevard)"
    return re.findall(pattern, text)

# Example
text = "Addresses are 123 Main St, 456 Elm Avenue, and 789 Maple Rd."
addresses = extract_addresses(text)
print(addresses)  

# Output: ['123 Main St', '456 Elm Avenue', '789 Maple Rd']
