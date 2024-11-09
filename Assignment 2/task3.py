# The evaluation functions calculate accuracy, precision, and recall 
# for the disambiguation algorithm. We’ll compute the values by 
# comparing actual versus predicted labels.

class EvaluationMetrics:
    def __init__(self, predictions, actuals):
        self.predictions = predictions
        self.actuals = actuals

    def accuracy(self):
        correct = sum(1 for p, a in zip(self.predictions, self.actuals) if p == a)
        return correct / len(self.actuals)

    def precision(self, label):
        tp = sum(1 for p, a in zip(self.predictions, self.actuals) if p == a == label)
        fp = sum(1 for p, a in zip(self.predictions, self.actuals) if p == label and a != label)
        return tp / (tp + fp) if (tp + fp) > 0 else 0

    def recall(self, label):
        tp = sum(1 for p, a in zip(self.predictions, self.actuals) if p == a == label)
        fn = sum(1 for p, a in zip(self.predictions, self.actuals) if p != label and a == label)
        return tp / (tp + fn) if (tp + fn) > 0 else 0

# Example usage
predictions = ['company', 'fruit', 'fruit', 'company', 'unknown']
actuals = ['company', 'fruit', 'company', 'company', 'fruit']
evaluator = EvaluationMetrics(predictions, actuals)

print("Accuracy:", evaluator.accuracy())
print("Precision (company):", evaluator.precision('company'))
print("Recall (company):", evaluator.recall('company'))
print("Precision (fruit):", evaluator.precision('fruit'))
print("Recall (fruit):", evaluator.recall('fruit'))
