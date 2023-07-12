FROM node:lts-alpine as build-stage

WORKDIR /frontend

COPY frontend/package*.json .


RUN apk update && apk add --no-cache bash
RUN npm install -g npm@latest
RUN npm install

COPY frontend/ .

ARG FRONTEND_ENV=production

ENV VUE_APP_ENV=${FRONTEND_ENV}

RUN npm run build


FROM nginx:latest as production-stage

#COPY ./nginx.conf /etc/nginx/conf.d
#COPY ./nginx-backend-not-found.conf /etc/nginx/extra-conf.d/backend-not-found.conf

# RUN rm -rf /usr/share/nginx/html/*
#COPY --from=frontend /frontend/dist /usr/share/nginx/html


COPY --from=build-stage /frontend/dist /usr/share/nginx/html

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]