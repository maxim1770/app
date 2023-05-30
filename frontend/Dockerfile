FROM node:lts-alpine as build-stage

WORKDIR /frontend

COPY package*.json ./

RUN npm install -g npm@latest
RUN npm install

COPY . .

ARG FRONTEND_ENV=production

ENV VUE_APP_ENV=${FRONTEND_ENV}

EXPOSE 5173