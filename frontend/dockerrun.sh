#!/bin/bash

project=${1}

case $project in
    "course-app") port=9000
    ;;
    "admin-app") port=9001
    ;;
    "proans-app") port=9002
    ;;
    *) echo "Parameter not right, check it!"
    exit
    ;;
esac

echo "Building ${project} image ..."

docker build -t $project "./${project}"

echo "Deleting former ${project}-dev ..."

docker rm -f $(docker ps -a | grep "${project}-dev" | awk '{print $1}')

echo "Starting ${project}-dev ..."

echo "Running on http://127.0.0.1:${port}/"

docker container run -it --name "${project}-dev" -p "${port}:8080" $project
