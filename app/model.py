import joblib
import os

MODEL_PATH = os.path.join("models","fraud_model.pkl")
model = joblib.load(MODEL_PATH)


with open("models/features.txt") as f:
    feature_names = [line.strip() for line in f]

def predict(features: list):
    return model.predict([features])[0], model.predict_proba([features])[0][1]