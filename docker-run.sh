#! /bin/sh

set -ex

docker run --rm -it -e login="$1" -e password="$2" eu_auto_auth