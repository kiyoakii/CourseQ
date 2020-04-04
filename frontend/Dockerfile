# FROM node:latest

# COPY ./sources.list /etc/apt/sources.list

# RUN apt-get update && apt-get install -y curl apt-transport-https && \
#     curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - && \
#     echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list && \
#     apt-get update && apt-get install -y yarn

# WORKDIR /app

# CMD ["yarn", "serve"]


# make image smaller.
# this image already containes node(10.19.0) and yarn(1.12.1)
FROM node:10.19.0-alpine3.11

RUN mkdir -p /app/frontend

WORKDIR /app/frontend

COPY ./app/ /app/frontend
RUN cd /app/frontend/ \
    && yarn

EXPOSE 8080
CMD ["yarn", "serve"]
