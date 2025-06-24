from prometheus_client import Counter, Summary, generate_latest,CONTENT_TYPE_LATEST
from fastapi import Request, Response


predictions_counter=Counter(
    "fraud_prediction_total",
    "Total number of fraud model predictions",
    ["label"]
)

prediction_latency = Summary(
    "fraud_prediction_latency_seconds",
    "Time taken for prediction"
)

def metrics_endpoint():
    data=generate_latest()
    return Response(content=data,media_type=CONTENT_TYPE_LATEST)
