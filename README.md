Platform Engineering Assignment - AWS/EKS Platform
Overview
This project implements a robust platform on AWS/EKS for deploying FastAPI applications with proper CI/CD, security, and observability.

Prerequisites
AWS CLI configured
Terraform v1.0+
kubectl
helm
Python 3.9+
Infrastructure Deployment cd terraform terraform init terraform plan -var="environment=dev" terraform apply -var="environment=dev"

Configure kubectl aws eks update-kubeconfig --region us-east-1 --name my_eks_cluster

Deploy Application cd ../helm/sample-app helm upgrade --install sample-app . -f values/dev.yaml

CI/CD Setup

GitHub Actions Configuration

Fork this repository
Add these secrets to your GitHub repository: · AWS_ACCOUNT_ID: Your AWS account ID · AWS_ROLE_ARN: ARN of the OIDC role (created by Terraform)
Workflow Triggers

· Push to dev branch → deploys to dev · Push to stage branch → deploys to stage · Release created → deploys to prod (with manual approval)

Dev Tooling Script

Log Tail Script

python src/scripts/log_tail.py --env dev --app sample-app --follow

Options:

· --env: Environment (dev/stage/prod) · --app: sample-app · --follow: Follow logs · --lines: Number of lines to show

Monitoring & Alerting

Access Prometheus:

kubectl port-forward -n monitoring svc/prometheus-k8s 9090

View Grafana:

kubectl port-forward -n monitoring svc/grafana 3000

Cleanup terraform destroy -var="environment=dev"

