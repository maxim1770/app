FROM node:20.8.0-alpine as build-stage

WORKDIR /frontend

COPY package*.json ./

RUN apk update && apk add --no-cache bash
RUN npm install -g npm@latest --no-cache
RUN npm install

COPY . .

RUN npm run build

FROM nginx:stable-alpine as production-stage
COPY --from=build-stage /frontend/dist /usr/share/nginx/html

# RUN rm /etc/nginx/conf.d/default.confe
# COPY ./nginx.conf /etc/nginx/conf.d

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
