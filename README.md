# USTC-SE-2020
This repository contains project built for Software Engineering course of USTC in Spring, 2020

## Backend Environment

```shell
$ cd backend
$ docker build -t backend .
$ docker run -d --name backend-server -p 9001:80 backend
$ docker run -it --name backend-dev -p 9001:80 -v $(pwd)/app:/app -e FLASK_APP=app/main.py -e FLASK_DEBUG=1 backend bash -c "flask run --host=0.0.0.0 --port=80"
```
