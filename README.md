# Penguin API Project
## Overview
A FastAPI app for penguin species prediction using an XGBoost model.

## Setup Instructions
1. Install Python 3.12.3 and Docker Desktop.
2. Clone this repo: `git clone <your-repo-url>`.
3. Set up `.env` with GCP credentials.
4. Run `uv sync` and `docker build -t penguin-api .`.

## API Documentation
- `/predict`: POST with penguin data (e.g., {"bill_length_mm": 39.1, ...}).

## Questions
1. **Edge cases not in training data?** Unusual species or missing features.
2. **Model file corrupted?** Fallback to a cached copy or retrain.
3. **Realistic load?** 10-50 users/hour for a niche service.
4. **Slow response times?** Increase Cloud Run memory/CPU.
5. **Key metrics?** Latency, error rate, throughput.
6. **Docker layer caching?** Speeds up builds by reusing layers.
7. **Security risks with root?** Privilege escalation; use non-root users.
8. **Cloud auto-scaling?** May mask bottlenecks in load tests.
9. **10x traffic?** Scale resources or add load balancers.
10. **Monitor performance?** Use Cloud Monitoring for latency/errors.
11. **Blue-green deployment?** Deploy new version alongside old, switch traffic.
12. **Deployment fails?** Roll back to last stable version.
13. **Too much memory?** Set memory limits in Cloud Run.
14. **Other?** [Add as needed.]