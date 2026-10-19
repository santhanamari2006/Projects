# DevSecOps Three-Tier Application on AWS EKS

## Project Overview
This project demonstrates a DevSecOps workflow for deploying a three-tier application on AWS using CI/CD automation, containerization, GitOps, security scanning, and monitoring.

## Technologies Used
- **AWS:** EC2, EKS, ECR, IAM
- **CI/CD:** Jenkins
- **Infrastructure as Code:** Terraform
- **Containerization:** Docker
- **GitOps:** Argo CD
- **Security:** SonarQube, Trivy
- **Monitoring:** Prometheus, Grafana
- **Orchestration:** Kubernetes

## Workflow
1. Provision infrastructure using Terraform.
2. Build and containerize the application using Jenkins and Docker.
3. Scan code and container images using SonarQube and Trivy.
4. Push container images to Amazon ECR.
5. Deploy the application to Amazon EKS using Argo CD.
6. Monitor application and cluster metrics using Prometheus and Grafana.

## Key Learnings
- CI/CD pipeline automation
- Kubernetes deployment on AWS EKS
- GitOps with Argo CD
- DevSecOps security scanning
- Infrastructure automation and monitoring

**Note:** Update the workflow and technologies to match your actual implementation.
