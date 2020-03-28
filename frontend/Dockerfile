FROM node:latest

COPY ./sources.list /etc/apt/sources.list

RUN apt-get update && apt-get install -y curl apt-transport-https && \
    curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - && \
    echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list && \
    apt-get update && apt-get install -y yarn

WORKDIR /app

COPY ./app /app

RUN yarn 

RUN echo "PATH=$PATH:/app/node_modules" >> /etc/profile

CMD ["yarn", "serve"]
