# Utilise l'image de base Python
FROM python:3.8

# Copie le code source dans le conteneur
COPY requirements.txt /app/requirements.txt
COPY connection.cfg /app/connection.cfg 
COPY app.py /app/app.py
COPY templates /app/templates

# Définit le répertoire de travail
WORKDIR /app

# Installe les dépendances
RUN pip install mysql-connector-python
RUN pip install -r requirements.txt --no-cache-dir

# Expose le port 5000 utilisé par l'application Flask
#EXPOSE 5000

# Exécute l'application Flask
CMD ["flask", "run", "--host=0.0.0.0", "--port=80"]
