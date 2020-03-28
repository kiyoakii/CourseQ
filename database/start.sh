#!/bin/bash

echo "Pulling mariadb image ..."

docker pull mariadb:latest

for container_id in $(docker ps -a | grep mariadb-dev | awk '{print $1}')
do
    echo "Deleting former mariadb-dev ..."
    docker rm -f ${container_id}
done

echo "Starting mariadb-dev ..."
echo "Running on http://127.0.0.1:9002/"

docker run -d --name mariadb-dev -p 9002:3306 -v $(pwd)/data:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=123456 mariadb
