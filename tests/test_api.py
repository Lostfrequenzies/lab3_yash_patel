from fastapi.testclient import TestClient
from app.main import app  # Adjust import based on your structure
import pytest

client = TestClient(app)

def test_predict_endpoint_valid_input():
    """Test prediction with valid penguin data"""
    sample_data = {
        "bill_length_mm": 39.1,
        "bill_depth_mm": 18.7,
        "flipper_length_mm": 181,
        "body_mass_g": 3750,
        "year": 2007,
        "sex": "male",
        "island": "Torgersen"
    }
    response = client.post("/predict", json=sample_data)
    assert response.status_code == 200
    assert "species" in response.json()

def test_predict_endpoint_missing_field():
    """Test handling of missing required field"""
    sample_data = {
        "bill_depth_mm": 18.7,
        "flipper_length_mm": 181,
        "body_mass_g": 3750,
        "year": 2007,
        "sex": "male",
        "island": "Torgersen"
    }
    response = client.post("/predict", json=sample_data)
    assert response.status_code == 422  # Unprocessable Entity

def test_predict_endpoint_invalid_type():
    """Test handling of invalid data type"""
    sample_data = {
        "bill_length_mm": "invalid",
        "bill_depth_mm": 18.7,
        "flipper_length_mm": 181,
        "body_mass_g": 3750,
        "year": 2007,
        "sex": "male",
        "island": "Torgersen"
    }
    response = client.post("/predict", json=sample_data)
    assert response.status_code == 400

def test_predict_endpoint_out_of_range():
    """Test handling of out-of-range value"""
    sample_data = {
        "bill_length_mm": 39.1,
        "bill_depth_mm": 18.7,
        "flipper_length_mm": 181,
        "body_mass_g": -1000,  # Negative value
        "year": 2007,
        "sex": "male",
        "island": "Torgersen"
    }
    response = client.post("/predict", json=sample_data)
    assert response.status_code == 400