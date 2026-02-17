**Présentation du projet : Dynamique pricing**
Ce projet démontre le cycle complet de mise en production d’un modèle de Machine Learning, depuis l’entraînement local jusqu’à l’exposition publique d’une API dans le cloud.


**Le projet couvre** : Entraînement du modèle ; Conteneurisation avec Docker ; Registry privé avec Amazon ECR ; Déploiement sur Amazon EC2 ; Sécurisation IAM ; Exposition publique via FastAPI.

**PARTIE MACHINE LEARNING**

Modèle entraîné dans un notebook Jupyter
Sérialisation avec joblib
Chargement automatique du modèle au démarrage de l’API
Endpoint /predict exposé via FastAPI

**Conteneurisation avec Docker**
L’application est entièrement conteneurisée afin de garantir :
Reproductibilité
Portabilité
Cohérence d’environnement
Déploiement simplifié
