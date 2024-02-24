FROM nginx:alpine

RUN rm -rf /etc/nginx/
COPY ./ /etc/nginx/
RUN ls /usr/local/ -a
RUN ls /etc/nginx/ -a
EXPOSE 80

CMD [ "nginx", "-g", "daemon off;" ]
