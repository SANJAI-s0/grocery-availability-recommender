# frontend Dockerfile (prod) - build stage then nginx
FROM node:18 AS build
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

FROM nginx:stable-alpine
COPY --from=build /app/build /usr/share/nginx/html
# simple healthcheck for nginx
HEALTHCHECK --interval=30s --timeout=3s --retries=3 CMD wget -qO- --spider http://127.0.0.1/ || exit 1
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
