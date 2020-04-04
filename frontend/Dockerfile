FROM node:10.19.0-alpine3.11

WORKDIR /app

COPY ./app /app

RUN yarn

EXPOSE 8080

CMD ["yarn", "serve"]
