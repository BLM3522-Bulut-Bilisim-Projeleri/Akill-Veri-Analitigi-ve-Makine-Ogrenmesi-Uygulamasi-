from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()
model = None

class PredictRequest(BaseModel):
    features: list  # Örn: [[14.2, 20.5, 95.0, 600.1, ...]]

def load_model():
    global model
    if model is None:
        model = joblib.load("model.joblib")  # Dockerfile ile aynı dizinde

@app.post("/predict")
def predict(request: PredictRequest):
    try:
        load_model()
        input_data = np.array(request.features)
        prediction = model.predict(input_data).tolist()
        return {"prediction": prediction}
    except Exception as e:
        return {"error": str(e)}  # Hata varsa direkt göster

