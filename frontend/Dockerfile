FROM node:20.10.0-alpine as build-stage

WORKDIR /frontend

COPY package*.json ./

RUN apk update && apk add --no-cache bash
RUN npm install -g npm@latest --no-cache
RUN npm install

COPY . .

RUN npm run build -f

FROM nginx:stable-alpine as production-stage
COPY --from=build-stage /frontend/dist /usr/share/nginx/html

RUN rm /etc/nginx/nginx.conf
COPY ./nginx.conf /etc/nginx/nginx.conf

# WORKDIR /frontend

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
