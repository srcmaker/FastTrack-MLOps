from fastapi import FastAPI, Query
import joblib
import uvicorn
import os
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI(title="Simple MLOps Prediction API")

model = None

@app.on_event("startup")
def load_model():
    global model
    model_path = "model/linear_model.pkl"
    if os.path.exists(model_path):
        model = joblib.load(model_path)
        print("Model loaded successfully.")
    else:
        print("Model not found. Please run train.py first.")

@app.get("/predict")
def predict(x: float = Query(..., description="Input value for prediction")):
    if model is None:
        return {"error": "Model not loaded."}
    prediction = model.predict([[x]])[0]
    return {"x": x, "prediction": prediction}

Instrumentator().instrument(app).expose(app)

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
