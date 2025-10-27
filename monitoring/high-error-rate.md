# High Error Rate Alert - Runbook

# Alert Description
The Prometheus alert `HighErrorRate` has fired, indicating elevated HTTP error rates.

# Immediate Actions
1. Check Current Error Rate
Get current error rate from Prometheus
kubectl port-forward -n monitoring svc/prometheus-k8s 9090:9090
# Then query: rate(http_requests_total{status=~"5.."}[5m])

2. Check Application Logs

# Use our log tooling script
python scripts/log_tail.py --env prod --app sample-app --lines 100

# Or directly with kubectl
kubectl logs -n prod -l app=sample-app --tail=100 | grep -i error

3. Check Pod Status

kubectl get pods -n prod -l app=sample-app
kubectl describe pods -n prod -l app=sample-app

4. Check Resource Usage

kubectl top pods -n prod
kubectl describe nodes

5. Check Recent Deployments

kubectl get deployments -n prod
kubectl rollout history deployment/sample-app -n prod


# Investigation Steps

A. Identify Error Patterns

1. Check if errors are specific to certain endpoints:

kubectl logs -n prod -l app=sample-app | grep "ERROR" | awk '{print $NF}' | sort | uniq -c

1. Check application metrics endpoint:

kubectl port-forward -n prod deployment/sample-app 8000:8000
curl http://localhost:8000/metrics | grep http_requests_total

B. Rollback if Needed

If errors started after recent deployment:

helm history sample-app -n prod
helm rollback sample-app <previous-revision> -n prod

C. Scale Resources if Needed

kubectl scale deployment sample-app -n prod --replicas=3

# Resolution
· Document root cause in incident report
· Update monitoring if new error patterns discovered
· Consider adding more specific alerts
