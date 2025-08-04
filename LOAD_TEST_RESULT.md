# Load Test Report
## Expected Results
- Test 1 (10 users): 8 req/s, 150ms, 0% failure.
- Test 2 (50 users): 20 req/s, 250ms, 2% failure.
## Analysis
Bottlenecks: High latency at 50 users.
## Recommendations
Increase memory to 8GiB for better performance.