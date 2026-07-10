There is an access log at /app/access.log. Analyze the traffic and write a JSON
summary to /app/report.json with exactly these three keys:

- total_requests: the total number of requests (log lines) in access.log
- unique_ips: the number of distinct client IPs that made requests
- top_path: the single most-requested request path

You have 120 seconds to complete this task.
