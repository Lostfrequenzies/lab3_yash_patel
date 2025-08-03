from fastapi import FastAPI, HTTPException
from google.cloud import storage
import os
from dotenv import load_dotenv
import xgboost as xgb
import logging
import json

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()
app = FastAPI()

try:
    client = storage.Client()
    bucket_name = os.getenv("GCS_BUCKET_NAME", "penguin-model-bucket-yash")
    blob_name = os.getenv("GCS_BLOB_NAME", "model.json")
    bucket = client.get_bucket(bucket_name)
    blob = bucket.get_blob(blob_name)
    if not blob.exists():
        raise FileNotFoundError(f"Model file {blob_name} not found in bucket {bucket_name}")
    model_data = blob.download_as_bytes()
    model = xgb.Booster()
    model.load_model(model_data)
    logger.info("Model loaded from GCS successfully.")
except Exception as e:
    logger.error(f"Failed to load model: {str(e)}")
    raise HTTPException(status_code=500, detail=f"Model loading failed: {str(e)}")

@app.post("/predict")
async def predict(data: dict):
    try:
        # Example: Convert input to DMatrix (adjust based on your Lab 3 code)
        dmatrix = xgb.DMatrix(json.dumps(data))
        prediction = model.predict(dmatrix)[0]
        species = ["Adelie", "Chinstrap", "Gentoo"][int(prediction)]  # Adjust based on your label encoder
        return {"species": species}
    except Exception as e:
        logger.error(f"Prediction failed: {str(e)}")
        raise HTTPException(status_code=400, detail=f"Prediction failed: {str(e)}")