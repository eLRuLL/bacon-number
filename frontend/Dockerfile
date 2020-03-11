FROM node:latest
WORKDIR /app
COPY package*.json ./
COPY yarn*.lock ./
RUN yarn install
COPY ./ .
ARG VUE_APP_API_URL
ENV VUE_APP_API_URL $VUE_APP_API_URL

RUN yarn run build
