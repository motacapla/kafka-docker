#!/bin/sh

#  This needs to be executed for the first time
#  sed -i -e 's/KAFKA_ADVERTISED_HOST_NAME:.*/KAFKA_ADVERTISED_HOST_NAME: ${DOCKER_HOST_IP}/g' docker-compose.yml

export DOCKER_HOST_IP=$(ipconfig getifaddr en0)
