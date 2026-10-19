# CI/CD Pipeline Using GitHub Actions and Amazon EKS

## Project Overview
This project demonstrates automated application deployment to Amazon EKS using GitHub Actions, Docker, and Kubernetes. The pipeline automates building container images and deploying application updates to a Kubernetes cluster.

## Technologies Used
- AWS: Amazon EKS, Amazon ECR, IAM
- GitHub Actions
- Docker
- Kubernetes
- AWS CLI
- Git & GitHub

## Workflow
1. Push application code to GitHub.
2. GitHub Actions triggers the CI/CD workflow.
3. Build the Docker image.
4. Push the image to Amazon ECR.
5. Deploy the application to Amazon EKS using Kubernetes manifests.
6. Verify the deployment and service status.

## Key Learnings
- CI/CD automation with GitHub Actions
- Docker image creation and management
- Kubernetes deployments on Amazon EKS
- AWS integration and cloud deployment automation