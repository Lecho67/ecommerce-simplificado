# Usa una imagen base de Python oficial
FROM python:3.11-slim-buster

# Evita que Python escriba archivos .pyc en el contenedor
ENV PYTHONDONTWRITEBYTECODE 1
# Asegura que la salida del log de Python no esté buferizada
ENV PYTHONUNBUFFERED 1

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app/backend

# Copia los archivos de requerimientos e instala las dependencias
# Usa COPY --from=builder si tienes una etapa de build separada para dependencias,
# pero para simplicidad, esto es suficiente.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del código de la aplicación
COPY . .

# Expone el puerto que Django usará
EXPOSE 8000

# Comando para iniciar el servidor de Django (después de las migraciones)
# Nota: Usaremos 'gunicorn' para un servidor de producción en Docker, no 'runserver'.
# Necesitarás instalar gunicorn: pip install gunicorn
# También, usaremos 'command' en docker-compose.yml para las migraciones y el inicio.
# Por ahora, puedes dejarlo como un marcador de posición o usar un comando simple.
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"] # Esto es para desarrollo local, no para Docker en producción