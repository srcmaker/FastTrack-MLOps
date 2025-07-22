import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib
import os

def load_data():
    data = pd.DataFrame({
        'x': range(100),
        'y': [i * 2 + 1 for i in range(100)]
    })
    return data

def train_model():
    data = load_data()
    X = data[['x']]
    y = data['y']

    model = LinearRegression()
    model.fit(X, y)

    os.makedirs("model", exist_ok=True)
    joblib.dump(model, "model/linear_model.pkl")
    print("Model saved to model/linear_model.pkl")

if __name__ == "__main__":
    train_model()
