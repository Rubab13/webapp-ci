FROM nginx:alpine
COPY code/ /usr/share/nginx/html
EXPOSE 80