import joblib
import sys

def predict(x):
    model = joblib.load("model/linear_model.pkl")
    prediction = model.predict([[x]])
    return prediction[0]

if __name__ == "__main__":
    x_val = float(sys.argv[1]) if len(sys.argv) > 1 else 10.0
    print(f"Prediction for x={x_val}: {predict(x_val)}")
