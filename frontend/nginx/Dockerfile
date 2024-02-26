FROM nginx:alpine
COPY ./sites-available/default /etc/nginx/conf.d/default.conf
EXPOSE 80

CMD [ "nginx", "-g", "daemon off;" ]
