#!/usr/bin/env bash

docker build -t egc-vr .

export DOCKER_ID_USER=$DOCKER_USER

docker login --username=$DOCKER_USER --password=$DOCKER_PASSWORD

docker tag egc-vr $DOCKER_ID_USER/egc-vr

docker push $DOCKER_ID_USER/egc-vr