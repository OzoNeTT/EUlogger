FROM python:3.7-slim-buster

COPY requirements.txt /tmp/requirements.txt

ENV PACKAGES="gcc \
              build-essential \
              python3-dev"

RUN set -ex && \
    apt-get update -y && \
    apt-get install -y $PACKAGES && \
    pip install -r requirements.txt  && \
    cd /tmp/ && \
    apt-get remove -y $PACKAGES

WORKDIR /opt/builder

COPY . /opt/builder
