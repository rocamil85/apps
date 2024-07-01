# Usa una imagen base de Python estándar
FROM python:3.12-slim

# Normalmente se usa WORKDIR /app 
# pero por cuestión de organización se reemplaza app por el nombre de la app actual 
# para que tanto el container como la aplicación local tengan la misma estructura
WORKDIR /billionApp

# Copia el archivo requirements.txt desde el contexto de construcción actual (la misma carpeta que el Dockerfile)
# al directorio raíz del contenedor (.)
# esto quedaría en el container como billionApp/requirements.txt
COPY requirements.txt .

# Instala las dependencias especificadas en requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo el contenido del contexto de construcción actual (la misma carpeta que el Dockerfile)
# al directorio raíz del contenedor (.)
# Excluye cualquier archivo especificado en .dockerignore
# como en un paso anterior ya se copió el requirements.txt en esta última copia se excluye
COPY . .

# Expone el puerto en el que Flask correrá
EXPOSE 8080

# Usa Gunicorn para ejecutar la aplicación con 3 workers y un timeout de 3600 segundos
# El comando `src.billion-test:app` asume que el archivo billion-test.py dentro del directorio src 
# contiene una instancia de Flask llamada `app` o sea
# app = Flask(__name__)
CMD ["gunicorn", "-b", ":8080", "src.billion-test:app", "--workers", "3", "--timeout", "3600"]
