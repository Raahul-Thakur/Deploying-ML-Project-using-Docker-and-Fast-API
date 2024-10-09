import pickle
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

# Load iris dataset
iris = load_iris()
X, y = iris.data, iris.target

# Train a RandomForestClassifier
model = RandomForestClassifier()
model.fit(X, y)

# Save the model using pickle
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)
