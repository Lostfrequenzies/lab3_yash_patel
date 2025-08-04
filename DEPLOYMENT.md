## Load Testing & Analysis
- Tool: Locust, run manually via web UI with locustfile.py
- Test 1 (10 users, 1 spawn): [e.g., 8 req/s, 150ms avg, 0% failure]
- Test 2 (50 users, 5 spawn): [e.g., 20 req/s, 250ms avg, 2% failure]
- Cloud Run Metrics: [e.g., 20 req/s, 260ms latency, 2% errors]
- Bottlenecks: [e.g., High latency at 50 users, resolved with 8GiB memory]
- Optimizations: [e.g., Increased memory to 8GiB, reduced latency]