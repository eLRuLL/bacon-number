FROM node:16
WORKDIR /app
COPY package*.json ./
# COPY yarn*.lock ./
RUN npm update --depth 5 @babel/preset-env
RUN npm update --depth 5 @babel/compat-data
RUN npm install
COPY ./ .
ARG VUE_APP_API_URL
ENV VUE_APP_API_URL $VUE_APP_API_URL

RUN yarn run build
