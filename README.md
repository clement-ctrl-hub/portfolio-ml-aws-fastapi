# 🚀 Portfolio ML API - Déploiement AWS avec CI/CD

API de Machine Learning développée avec FastAPI et déployée automatiquement sur AWS grâce à GitHub Actions.

## Objectif

Ce projet montre la mise en production complète d'un modèle de Machine Learning.

Fonctionnalités :

- API REST FastAPI
- Modèle Machine Learning
- Docker
- GitHub Actions
- Amazon ECR
- Amazon EC2
- Amazon S3
- AWS Systems Manager (SSM)
- Déploiement automatique (CI/CD)

## Architecture

```text
GitHub
  │
  ▼
GitHub Actions
  ├── Tests Pytest
  ├── Build Docker
  ├── Push vers Amazon ECR
  └── Déploiement via AWS Systems Manager
          │
          ▼
      Amazon EC2
          │
          ├── FastAPI
          └── Téléchargement du modèle depuis Amazon S3