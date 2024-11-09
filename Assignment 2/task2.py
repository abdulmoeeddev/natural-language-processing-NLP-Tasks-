# Preprocess and vectorize the text.
# Apply NMF to identify sentiment-related topics.
# Create a simple sentiment visualization showing positive and negative sentiments.

import numpy as np

class SentimentAnalysisNMF:
    def __init__(self, text_data):
        self.text_data = text_data
        self.vocab = {}
        self.term_matrix = self.build_term_matrix(text_data)
    
    def tokenize(self, text):
        return text.lower().split()
    
    def build_term_matrix(self, text_data):
        word_index = 0
        # Build vocabulary and term matrix
        matrix = []
        for text in text_data:
            tokens = self.tokenize(text)
            row = [0] * len(self.vocab)
            for token in tokens:
                if token not in self.vocab:
                    self.vocab[token] = word_index
                    word_index += 1
                    row.append(1)
                else:
                    row[self.vocab[token]] += 1
            matrix.append(row)
        return np.array(matrix)

    def apply_nmf(self, n_components=2, iterations=100):
        # Initialize random matrices W (documents x topics) and H (topics x words)
        W = np.random.rand(self.term_matrix.shape[0], n_components)
        H = np.random.rand(n_components, self.term_matrix.shape[1])

        # NMF iterations
        for _ in range(iterations):
            H = H * (W.T @ self.term_matrix) / (W.T @ W @ H + 1e-9)
            W = W * (self.term_matrix @ H.T) / (W @ H @ H.T + 1e-9)
        
        return W, H

# Example usage
texts = [
    "I love my new iPhone, it's amazing!",
    "Apple as a fruit is very healthy and sweet.",
    "The Apple MacBook is a great device for professionals.",
    "Eating an apple a day is good for health."
]
sa_nmf = SentimentAnalysisNMF(texts)
W, H = sa_nmf.apply_nmf(n_components=2)
print("Document-topic matrix W:", W)
print("Topic-term matrix H:", H)
