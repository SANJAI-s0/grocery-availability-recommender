# frontend/Dockerfile (prod)
FROM node:18 AS build
WORKDIR /app

ENV NODE_ENV=production
COPY package*.json ./
RUN npm install --no-audit --no-fund

COPY . .
RUN npm run build

FROM nginx:stable-alpine
RUN rm -rf /usr/share/nginx/html/*
COPY --from=build /app/build /usr/share/nginx/html

HEALTHCHECK --interval=30s --timeout=3s --retries=3 \
  CMD wget -qS --spider http://127.0.0.1/ || exit 1

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
