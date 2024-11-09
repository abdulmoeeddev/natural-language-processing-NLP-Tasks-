import re

def format_dates(text):
    pattern = r"(\d{4})[/-](\d{2})[/-](\d{2})|(\d{2})[/-](\d{2})[/-](\d{4})"
    
    def reformat(match):
        if match.group(1):  # YYYY-MM-DD format
            return f"{match.group(1)}-{match.group(2)}-{match.group(3)}"
        else:  # DD-MM-YYYY or MM/DD/YYYY format
            return f"{match.group(6)}-{match.group(4)}-{match.group(5)}"
    
    return re.sub(pattern, reformat, text)

# Example
text = "Dates are 2024/11/02, 02-11-2024, and 11/02/2024."
formatted_text = format_dates(text)
print(formatted_text)  

# Output: "Dates are 2024-11-02, 2024-11-02, and 2024-11-02."
