# Etapa 1: Construir la aplicación React
FROM node:18-alpine AS builder

WORKDIR /app/frontend

# Copia SOLO los archivos de configuración de dependencias PRIMERO
# Esto permite que Docker cachee la instalación de npm/yarn
COPY frontend/package.json ./package.json
COPY frontend/package-lock.json ./package-lock.json 
# Si usas yarn, entonces usa: COPY frontend/yarn.lock ./yarn.lock

RUN npm install --frozen-lockfile

# Copia el resto del código de la aplicación (incluyendo src/, public/, etc.)
COPY frontend/ .

# Construye la aplicación React para producción
RUN npm run build


# Etapa 2: Servir la aplicación con Nginx
FROM nginx:alpine

# Elimina la configuración predeterminada de Nginx para usar la nuestra
RUN rm /etc/nginx/conf.d/default.conf

# Copia la configuración personalizada de Nginx
# Asegúrate de que tu carpeta 'nginx' esté en la raíz del proyecto, NO dentro de 'frontend'
COPY nginx/default.conf /etc/nginx/conf.d/default.conf

# Copia los archivos estáticos construidos desde la etapa 'builder'
COPY --from=builder /app/frontend/build /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]