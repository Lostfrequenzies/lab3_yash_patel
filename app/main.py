from google.cloud import storage
import os
from dotenv import load_dotenv

load_dotenv()
client = storage.Client()
bucket = client.get_bucket(os.getenv("GCS_BUCKET_NAME"))
blob = bucket.get_blob(os.getenv("GCS_BLOB_NAME"))
model_data = blob.download_as_bytes()
model.load_model(model_data)  # Adjust based on your XGBoost method