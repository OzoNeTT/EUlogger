#! /bin/sh

set -ex

./docker-build.sh
./docker-run.sh "$1" "$2"