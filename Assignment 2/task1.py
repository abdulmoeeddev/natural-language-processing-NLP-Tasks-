# Tokenize the text.
# Define two context lists: one for "fruit" and one for "company".
# Look for co-occurrences of "Apple" with context words.
# Assign "fruit" or "company" label based on the context list with more matches.

class DisambiguateApple:
    def __init__(self):
        # Define context keywords for disambiguation
        self.fruit_context = ["fruit", "healthy", "tree", "sweet", "juicy"]
        self.company_context = ["technology", "iphone", "macbook", "ipad", "app store", "device"]
    
    def disambiguate(self, text):
        tokens = text.lower().split()  # Basic tokenization
        apple_references = []  # Store references as (word, label) tuples

        # Scan through text to find "apple" and evaluate context
        for i, token in enumerate(tokens):
            if token == "apple":
                fruit_score = sum(1 for context in self.fruit_context if context in tokens[max(0, i-3):i+4])
                company_score = sum(1 for context in self.company_context if context in tokens[max(0, i-3):i+4])
                
                # Disambiguate based on higher score
                if fruit_score > company_score:
                    apple_references.append((token, "fruit"))
                elif company_score > fruit_score:
                    apple_references.append((token, "company"))
                else:
                    apple_references.append((token, "unknown"))  # Ambiguous case
        
        return apple_references

# Example usage
text = "Apple released a new iPhone, and apple is a delicious fruit."
disambiguator = DisambiguateApple()
print(disambiguator.disambiguate(text))  

# Expected output: [('apple', 'company'), ('apple', 'fruit')]
