from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
from fastapi import APIRouter, Response
import time

# Create metrics
REQUESTS = Counter(
    "api_requests_total",
    "Total API requests",
    ["method", "endpoint", "status_code"]
)

LATENCY = Histogram(
    "api_request_latency_seconds",
    "Request latency in seconds",
    ["method", "endpoint"]
)

PREDICTIONS = Counter(
    "model_predictions_total",
    "Total number of predictions made",
    ["status"]
)

# Create router
router = APIRouter()

@router.get("/metrics")
def metrics():
    """Endpoint to expose Prometheus metrics."""
    return Response(
        generate_latest(),
        media_type=CONTENT_TYPE_LATEST
    )

# Helper functions to record metrics
def record_request_metrics(method: str, endpoint: str, status_code: int, duration: float):
    """Record request-related metrics."""
    REQUESTS.labels(method=method, endpoint=endpoint, status_code=status_code).inc()
    LATENCY.labels(method=method, endpoint=endpoint).observe(duration)

def record_prediction(success: bool):
    """Record prediction-related metrics."""
    status = "success" if success else "failure"
    PREDICTIONS.labels(status=status).inc() 