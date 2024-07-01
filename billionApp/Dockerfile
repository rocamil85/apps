# Usa una imagen base de Python estándar
FROM python:3.12-slim

# Normalmente se usa WORKDIR /app 
# pero por cuestión de organización se reemplaza app por el nombre de la app actual 
# para que tanto el container como la aplicación local tengan la misma estructura
WORKDIR /billionApp

# Copiando el requirements.txt que está aquí mismo al lado del Dockerfile 
# hacia la raíz(.) de la aplicación del container 
# esto quedaría en el container como billionApp/requirements.txt
COPY requirements.txt .

# Instala las dependencias especificadas en requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copia el contenido <<interno>> de la carpeta contenedora de mi aplicación local billionApp al interior (.) de la aplicación del container
# ojo que lo que se copia es el interior de mi carpeta local billionApp y no la carpeta en sí, ya que en el container ya está creada la carpeta billionApp
# esto quedaría en el container como billionApp/src   
# como en un paso anterior ya se copió el requirements.txt en esta última copia se excluye
COPY . .

# Expone el puerto en el que Flask correrá
EXPOSE 8080

# Usa Gunicorn para ejecutar la aplicación con 3 workers y un timeout de 3600 segundos
# nota que aquí billion-test es sin .py y :app se refiere al nombre de la instancia de Flask en mi aplicación
# app = Flask(__name__)
CMD ["gunicorn", "-b", ":8080", "src.billion-test:app", "--workers", "3", "--timeout", "3600"]
