# Etapa 1: Construir la aplicación React
FROM node:18-alpine AS builder

WORKDIR /app/frontend

COPY frontend/package.json ./package.json
COPY frontend/package-lock.json ./package-lock.json
RUN npm install --frozen-lockfile

COPY frontend/ .
RUN npm run build

# Etapa 2: Servir la aplicación con Nginx
FROM nginx:alpine

# Elimina la configuración predeterminada de Nginx
RUN rm /etc/nginx/conf.d/default.conf
# Copia nuestra configuración personalizada de Nginx
COPY nginx/default.conf /etc/nginx/conf.d/default.conf

# Copia los staticfiles_collected del backend directamente a la raíz web de Nginx,
# en una subcarpeta llamada 'static'.
# La ruta de origen 'backend/staticfiles_collected' es relativa a la raíz del contexto de construcción (ecommerce-simplificado/)
# La ruta de destino '/usr/share/nginx/html/static/' es dentro del contenedor Nginx.
COPY backend/staticfiles_collected /usr/share/nginx/html/static/

# Copia los archivos estáticos de React compilados desde la etapa 'builder'
# La carpeta 'build' de React se copia a la raíz web de Nginx.
COPY --from=builder /app/frontend/build /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]