#!/bin/sh

mkdir -p docker/storage

docker-compose run --user root web /init_entrypoint.sh
docker-compose run web python3 -m magnumopus.initialize
