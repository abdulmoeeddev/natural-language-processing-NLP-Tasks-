from transformers import BertTokenizer, BertForTokenClassification
import torch

# Load pre-trained BERT model and tokenizer
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertForTokenClassification.from_pretrained('dbmdz/bert-large-cased-finetuned-conll03-english')

def bert_sentence_segmentation(text):
    # Tokenize the input text
    tokens = tokenizer.tokenize(text)
    input_ids = tokenizer.convert_tokens_to_ids(tokens)
    input_ids = torch.tensor([input_ids])
    
    # Predict sentence boundaries
    with torch.no_grad():
        outputs = model(input_ids)
        predictions = torch.argmax(outputs.logits, dim=2)
    
    # Convert predictions to sentence boundaries
    sentences = []
    current_sentence = []
    for token, prediction in zip(tokens, predictions[0]):
        current_sentence.append(token)
        if prediction == 1:  # Assuming 1 indicates a sentence boundary
            sentences.append(tokenizer.convert_tokens_to_string(current_sentence))
            current_sentence = []
    
    # Add the last sentence if any
    if current_sentence:
        sentences.append(tokenizer.convert_tokens_to_string(current_sentence))
    
    return sentences

# Test the function
text = "Hello world! This is a test. Mr. Smith went to the store. He bought some apples?"
segmented_sentences = bert_sentence_segmentation(text)
for sentence in segmented_sentences:
    print(sentence)