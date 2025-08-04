## Cloud Deployment
- Build and tag: Used PowerShell `docker build -t penguin-api .` and Docker Desktop to tag as us-central1-docker.pkg.dev/YOUR_PROJECT_ID/penguin-repo/penguin-api:latest
- Push: Used Docker Desktop Push with gcloud auth
- Deploy: Used GCP Console, set port 8080, allowed unauthenticated access
- URL: [Insert URL, e.g., http://penguin-api-714185561055.us-central1.run.app/]
- Issues: [e.g., None or specific errors]