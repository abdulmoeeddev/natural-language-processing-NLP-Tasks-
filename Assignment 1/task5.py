import re

def correct_spelling(text):
    corrections = {
        r"\bteh\b": "the",
        r"\brecieve\b": "receive",
        r"\boccured\b": "occurred"
    }
    
    for mistake, correct in corrections.items():
        text = re.sub(mistake, correct, text)
    return text

# Example
text = "This is teh test to recieve all occured errors."
corrected_text = correct_spelling(text)
print(corrected_text)  

# Output: "This is the test to receive all occurred errors."
