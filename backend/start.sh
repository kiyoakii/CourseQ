#!/bin/bash

echo "Building backend image ..."

docker build -t backend .

echo "Starting backend-dev ..."

echo "Running on http://127.0.0.1:9001/"

for container_id in $(docker ps -a | grep backend-dev | awk '{print $1}')
do
    docker rm -f ${container_id}
done

docker run -it --name backend-dev -p 9001:80 -v $(pwd)/app:/app -e FLASK_APP=app/main.py -e FLASK_DEBUG=1 backend bash -c "flask run --host=0.0.0.0 --port=80"
