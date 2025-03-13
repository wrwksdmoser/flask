# Basis-Image
FROM python:3.10

# Arbeitsverzeichnis setzen
WORKDIR /app

# Restlichen Code kopieren
COPY . .

# Port freigeben
EXPOSE 5000

# Startbefehl
CMD ["python", "app.py"]
