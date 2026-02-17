
**Présentation du projet : Dynamique pricing**

Ce projet démontre le cycle complet de mise en production d’un modèle de Machine Learning, depuis l’entraînement local jusqu’à l’exposition publique d’une API dans le cloud.

**Le projet couvre** : 
Entraînement du modèle ; Conteneurisation avec Docker ; Registry privé avec Amazon ECR ; Déploiement sur Amazon EC2 ; Sécurisation IAM ; Exposition publique via FastAPI.

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

**🔐 Sécurisation IAM**

Le compte root n’est jamais utilisé
Création d’un utilisateur IAM dédié
Génération de clés d’accès sécurisées
Configuration via : aws config
Authentification à ECR

**Déploiement sur AWS**

Tag de l’image 
Push vers ECR

**Amazon EC2**

instance : t3.micro
Région : Europe (Paris)
Groupe de sécurité configuré manuellement

**Lancement du conteneur sur EC2**
**API accessible via : http://<IP_PUBLIQUE_EC2>:8000/docs**

Compétences démontrées
Machine Learning

Entraînement de modèle

Sérialisation

Service d’inférence

Cloud AWS

Provisionnement EC2

Configuration Security Groups

Registry privé ECR

Gestion IAM sécurisée

