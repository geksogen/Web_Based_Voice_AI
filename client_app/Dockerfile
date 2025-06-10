FROM nginx:latest

COPY nginx.conf /etc/nginx/nginx.conf
# Удаляем стандартный конфигурационный файл Nginx, если он не нужен
RUN rm /etc/nginx/conf.d/default.conf

COPY ./index.html /usr/share/nginx/html/index.html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]