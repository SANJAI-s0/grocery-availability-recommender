# frontend/Dockerfile
FROM node:18 AS build

WORKDIR /app

ENV NODE_ENV=production

# -----------------------------
# Install deps
# -----------------------------
COPY package*.json ./
RUN npm install --no-audit --no-fund

# -----------------------------
# Build React app
# -----------------------------
COPY . .
RUN npm run build

# -----------------------------
# Nginx runtime
# -----------------------------
FROM nginx:stable-alpine

# Remove default nginx html
RUN rm -rf /usr/share/nginx/html/*

# Copy React build
COPY --from=build /app/build /usr/share/nginx/html

# Health check
HEALTHCHECK --interval=30s --timeout=3s --retries=3 \
  CMD wget -qS --spider http://127.0.0.1/ || exit 1

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
