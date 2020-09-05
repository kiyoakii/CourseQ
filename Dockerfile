FROM node:10.19.0-alpine3.11 AS builder

RUN mkdir /app

WORKDIR /app
RUN mkdir /app/course-app
RUN mkdir /app/admin-app
RUN mkdir /app/proans-app

COPY ./frontend/course-app /app/course-app
COPY ./frontend/admin-app /app/admin-app
COPY ./frontend/proans-app /app/proans-app

RUN cd /app/course-app && yarn install --registry=https://registry.npm.taobao.org/
RUN cd /app/admin-app && yarn install --registry=https://registry.npm.taobao.org/
RUN cd /app/proans-app && yarn install --registry=https://registry.npm.taobao.org/

RUN cd /app/course-app && yarn run build
RUN cd /app/admin-app && yarn run build
RUN cd /app/proans-app && yarn run build

FROM nginx:stable-alpine
ENV TZ=Asia/Shanghai
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

COPY --from=builder /app/course-app/dist /usr/share/nginx/course
COPY --from=builder /app/admin-app/dist /usr/share/nginx/admin
COPY --from=builder /app/proans-app/dist /usr/share/nginx/proans

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]