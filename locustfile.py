from locust import HttpUser, task, between

class PenguinUser(HttpUser):
    wait_time = between(1, 2)  # Wait 1-2 seconds between requests

    @task
    def predict(self):
        self.client.post("/predict", json={
            "bill_length_mm": 39.1,
            "bill_depth_mm": 18.7,
            "flipper_length_mm": 181,
            "body_mass_g": 3750,
            "year": 2007,
            "sex": "male",
            "island": "Torgersen"
        })