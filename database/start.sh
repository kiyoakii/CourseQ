#!/bin/bash

echo "Pulling mariadb image ..."

docker pull mariadb:latest

echo "Deleting former mariadb-dev ..."

docker rm -f $(docker ps -a | grep mariadb-dev | awk '{print $1}')

echo "Starting mariadb-dev ..."

echo "Running on http://127.0.0.1:9002/"

docker run -d --name mariadb-dev -p 9002:3306 mariadb
