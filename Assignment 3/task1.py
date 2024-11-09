import re

def basic_sentence_segmentation(text):
    # Define common sentence-ending punctuation marks
    sentence_endings = r'[.!?]'
    
    # Split the text based on sentence-ending punctuation marks
    sentences = re.split(f'({sentence_endings})', text)
    
    # Combine the punctuation marks with the sentences
    combined_sentences = []
    for i in range(0, len(sentences) - 1, 2):
        combined_sentences.append(sentences[i] + sentences[i + 1])
    
    # Handle any remaining text
    if len(sentences) % 2 == 1:
        combined_sentences.append(sentences[-1])
    
    return combined_sentences

# Test the function
text = "Hello world! This is a test. Mr. Smith went to the store. He bought some apples?"
segmented_sentences = basic_sentence_segmentation(text)
for sentence in segmented_sentences:
    print(sentence)