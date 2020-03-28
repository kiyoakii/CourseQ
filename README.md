# USTC-SE-2020
This repository contains project built for Software Engineering course of USTC in Spring, 2020

## Backend Environment

### Development Mode

```shell
$ cd backend
$ chmod +x start.sh
$ ./start.sh
```

### Deployment Mode
```shell
$ cd backend
$ docker build -t backend .
$ docker run -d --name backend-server -p 9001:80 backend
```
