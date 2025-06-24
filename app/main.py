from fastapi import FastAPI
from app.schema import Transaction
from app.model import predict
from app.metrics import predictions_counter,prediction_latency,metrics_endpoint


app = FastAPI()
@app.get("/")
def root():
    return {"message":"Fraud detection API is running"}

@app.post("/predict")
@prediction_latency.time()
def predict_transaction(transaction:Transaction):
    pred,prob = predict(transaction.features)
    
    label = "fraud" if pred==1 else "legit"
    predictions_counter.labels(label=label).inc()
    return{
        "predict":int(pred),
        "probability":round(prob,4)
        
    }
    
@app.get("/metrics")
def prometheus_metrics():
    return metrics_endpoint()
