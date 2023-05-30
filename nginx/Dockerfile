FROM nginx:latest as production-stage

RUN rm /etc/nginx/conf.d/default.conf
COPY ./nginx.conf /etc/nginx/conf.d
COPY ./nginx-backend-not-found.conf /etc/nginx/extra-conf.d/backend-not-found.conf

#COPY /frontend/dist/ /usr/share/nginx/html


EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]