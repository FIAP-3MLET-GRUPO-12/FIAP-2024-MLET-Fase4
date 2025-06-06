import pytest
from fastapi.testclient import TestClient
import numpy as np
from api.main import app

client = TestClient(app)

def test_health_check():
    """Test the health check endpoint."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

def test_predict_endpoint():
    """Test the prediction endpoint with sample data."""
    # Create sample input data
    sample_data = {
        "sequence": [
            {
                "open": float(100 + i),
                "high": float(105 + i),
                "low": float(95 + i),
                "close": float(102 + i),
                "volume": float(1000000)
            }
            for i in range(60)  # 60 days of sample data
        ]
    }

    # Make prediction request
    response = client.post("/predict", json=sample_data)
    
    # Check response
    assert response.status_code == 200
    prediction = response.json()
    assert "predicted_close" in prediction
    assert "confidence_interval" in prediction
    assert isinstance(prediction["predicted_close"], float)
    assert isinstance(prediction["confidence_interval"], dict)
    assert "lower" in prediction["confidence_interval"]
    assert "upper" in prediction["confidence_interval"]

def test_predict_invalid_input():
    """Test the prediction endpoint with invalid input."""
    # Test with missing data
    response = client.post("/predict", json={"sequence": []})
    assert response.status_code == 422  # Validation error

    # Test with invalid data structure
    response = client.post("/predict", json={"wrong_field": []})
    assert response.status_code == 422  # Validation error 