import pickle
from fastapi import FastAPI
import numpy as np

# Load the model using pickle
with open('app/model.pkl', 'rb') as f:
    model = pickle.load(f)

class_names = np.array(['setosa', 'versicolor', 'virginica'])

app = FastAPI()

@app.get('/')
def read_root():
    return {'message': 'Iris model API'}

@app.post('/predict')
def predict(data: dict):
    features = np.array(data['features']).reshape(1, -1)
    prediction = model.predict(features)
    class_name = class_names[prediction][0]
    return {'predicted_class': class_name}
