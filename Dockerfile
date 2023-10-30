# Utilisez une image officielle Python comme image parente
FROM python:3.9

# Définissez l'environnement de travail dans le conteneur
WORKDIR /usr/src/app

# Copiez les fichiers de dépendance dans le conteneur
COPY requirements.txt ./

# Installez les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copiez le contenu du répertoire local dans le conteneur
COPY . .

# Exposez le port sur lequel l'application s'exécute
EXPOSE 7860

# Commande pour exécuter l'application
CMD ["python", "./main.py"]
