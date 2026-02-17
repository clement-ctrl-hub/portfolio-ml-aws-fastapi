
# 🚀 Dynamic Pricing API – Projet End-to-End Machine Learning & Cloud AWS

## 📌 Présentation du projet : Dynamic Pricing pour la prédiction du prix d'un bien immobilier en fonction de certaines caractéristiques.

Ce projet démontre le **cycle complet de mise en production d’un modèle de Machine Learning**, depuis l’entraînement local jusqu’à l’exposition publique d’une API dans le cloud.

Il illustre une architecture **ML + DevOps + Cloud AWS** prête pour un environnement professionnel.

---

##  Objectifs du projet

Le projet couvre :

- Entraînement du modèle  
- Conteneurisation avec Docker  
- Registry privé avec Amazon ECR  
- Déploiement sur Amazon EC2  
- Sécurisation IAM  
- Exposition publique via FastAPI  

---

# PARTIE MACHINE LEARNING

- Modèle entraîné dans un **Notebook Jupyter**
- Sérialisation du modèle avec **joblib**
- Chargement automatique du modèle au démarrage de l’API
- Endpoint `/predict` exposé via **FastAPI**

### Fonctionnement

1. Le modèle est entraîné localement
2. Il est exporté en fichier `.joblib`
3. L’API charge le modèle au lancement
4. Les requêtes HTTP sur `/predict` retournent une prédiction en JSON

---

# Conteneurisation avec Docker

L’application est entièrement conteneurisée afin de garantir :

- Reproductibilité  
- Portabilité  
- ohérence d’environnement  
- Déploiement simplifié  

Chaque composant (API + modèle) est intégré dans une image Docker prête à être déployée.

---

# 🔐 Sécurisation IAM

Bonne pratique Cloud respectée :

- Le compte **root n’a pas été utilisé**
- Création d’un utilisateur IAM dédié
- Génération de clés d’accès sécurisées
- Configuration via : aws configure



**Déploiement sur AWS**

Tag de l’image 
Push vers ECR

**Amazon EC2**

instance : t3.micro
Région : Europe (Paris)
Groupe de sécurité configuré manuellement

**Lancement du conteneur sur EC2**
**API accessible via : http://<IP_PUBLIQUE_EC2>:8000/docs**

# Environnement de développement

- Système : Linux
- Shell : Bash
- Gestion d’environnement : venv
- Langage : Python 3.10+
- Notebook : Jupyter
- Framework API : FastAPI
- Conteneurisation : Docker
- Cloud : AWS (EC2, ECR, IAM)
- CLI : AWS CLI
- Versioning : Git / GitHub


---

# Auteur : Clément AMEGADJAKA

