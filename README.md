**Présentation du projet : Dynamique pricing**
Ce projet démontre le cycle complet de mise en production d’un modèle de Machine Learning, depuis l’entraînement local jusqu’à l’exposition publique d’une API dans le cloud.


**Le projet couvre** : Entraînement du modèle ; Conteneurisation avec Docker ; Registry privé avec Amazon ECR ; Déploiement sur Amazon EC2 ; Sécurisation IAM ; Exposition publique via FastAPI

Machine locale
   │
   │ Entraînement (Notebook)
   ▼
Modèle sérialisé (.joblib)
   │
   │ Docker build
   ▼
Image Docker
   │
   │ Push
   ▼
Amazon ECR (Registry privé)
   │
   │ Pull
   ▼
Amazon EC2 (t3.micro)
   │
   │ Docker run
   ▼
Application FastAPI
   │
   ▼
API accessible publiquement (/predict)

