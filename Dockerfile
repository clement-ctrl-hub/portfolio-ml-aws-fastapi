# Image Python officielle
FROM python:3.10

# Dossier de travail dans le conteneur
WORKDIR /app

# Copier les fichiers
COPY . .

# Installer les dépendances
RUN pip install --no-cache-dir fastapi uvicorn scikit-learn pandas joblib

# Exposer le port
EXPOSE 8000

# Commande de démarrage
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
