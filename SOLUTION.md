Solution Architecture & Design Decisions

## Architecture Overview
The solution implements a multi-tenant EKS cluster with namespace isolation for different environments (dev, stage, prod). This approach balances operational efficiency with adequate isolation for a SaaS platform.

### Core Components
- EKS Cluster: Single cluster with namespace-based isolation
- ALB Ingress Controller: For secure external access
- Prometheus/Grafana: For observability
- GitHub Actions OIDC: Secure CI/CD without long-lived credentials
- Helm-based Deployments: Standardized application packaging

## Key Design Decisions

### 1. Infrastructure as Code
- Terraform Modules: Reusable modules for EKS, VPC, and IAM
- Environment Parameterization: Single codebase with environment-specific variables
- State Management: Remote state with S3 backend (not shown for simplicity)

### 2. Security Implementation
- IAM Roles for Service Accounts (IRSA): Least privilege access for pods
- OIDC for GitHub Actions: No static credentials in CI/CD
- Network Policies: Default deny between namespaces
- ALB with HTTPS Only: TLS termination and secure ingress

### 3. CI/CD Pipeline
- Environment-based Promotion: Dev → Stage → Prod with approvals
- Automated Rollbacks: Helm rollback on failure detection

### 4. Observability
- Centralized Logging: FluentBit to CloudWatch
- Prometheus Metrics: Application and infrastructure monitoring
- Sample Runbooks: Operational guidance for common alerts


# For Time Constraints:
1. Single EKS Cluster: Production would use separate clusters per environment
2. Basic Monitoring: Limited to core metrics vs comprehensive distributed tracing
3. Simple Rollback Strategy: Basic Helm rollback vs canary/blue-green
4. Manual Secret Management: For demo vs external secrets operator

### Production Enhancements:
- Service Mesh (Istio/Linkerd) for advanced traffic management
- External Secrets Operator for secret management
- Backup/DR strategies for EKS and persistent data
- More granular network policies and pod security standards
- Cost allocation tags and budget alerts

# Solution Overview
This setup provisions AWS EKS using Terraform and deploys a FastAPI app via Helm.

