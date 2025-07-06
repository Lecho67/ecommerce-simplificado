FROM python:3.11-slim-buster
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /app/backend
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
# Ejecuta collectstatic durante la construcción de la imagen del backend.
# Los archivos se generarán en /app/backend/staticfiles_collected
RUN python manage.py collectstatic --noinput
EXPOSE 8000