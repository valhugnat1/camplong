# Stage 1: build frontend
FROM node:18-alpine AS node-build
WORKDIR /build
COPY frontend/package*.json ./
COPY frontend/vite.config.js ./
COPY frontend/src ./src
RUN npm ci
RUN npm run build

# Stage 2: assemble final image with python + nginx
FROM python:3.11-slim

# install nginx and small utilities
RUN apt-get update && apt-get install -y --no-install-recommends \
    nginx \
    curl \
    ca-certificates \
  && rm -rf /var/lib/apt/lists/*

# create app user & dirs
RUN mkdir -p /usr/share/nginx/html /var/log/nginx
WORKDIR /app

# copy backend
COPY backend /app/backend
COPY backend/requirements.txt /app/backend/requirements.txt
RUN pip install --no-cache-dir -r /app/backend/requirements.txt

# copy built frontend from node-build
COPY --from=node-build /build/dist /usr/share/nginx/html/app

# copy static site
COPY static-site /usr/share/nginx/html/

# copy nginx conf and start script
COPY docker/nginx.conf /etc/nginx/nginx.conf
COPY docker/start.sh /start.sh
RUN chmod +x /start.sh

EXPOSE 80 8000

CMD ["/start.sh"]