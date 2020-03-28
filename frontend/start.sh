#!/bin/bash

echo "Building frontend image ..."

docker build -t frontend .

for container_id in $(docker ps -a | grep frontend-dev | awk '{print $1}')
do
    echo "Deleting former frontend-dev ..."
    docker rm -f ${container_id}
done

echo "Starting frontend-dev ..."
echo "Running on http://127.0.0.1:9000/"

docker run -it --name frontend-dev -p 9000:8080 -v $(pwd)/app:/app frontend bash -c "yarn && yarn serve"
