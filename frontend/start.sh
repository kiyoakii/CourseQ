#!/bin/bash

echo "Building frontend image ..."

docker build -t frontend .

echo "Deleting former frontend-dev ..."

docker rm -f $(docker ps -a | grep frontend-dev | awk '{print $1}')

echo "Starting frontend-dev ..."

echo "Running on http://127.0.0.1:9000/"

docker container run -it --name frontend-dev -p 9000:8080 frontend
