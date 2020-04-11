FROM python:3.7-slim-buster

COPY requirements.txt /tmp/requirements.txt

ENV PACKAGES="gcc \
              build-essential \
              python3-dev"


RUN apt-get update -y &&\
    apt-get install -y curl unzip xvfb libxi6 libgconf-2-4 &&\
    apt-get install -y default-jdk &&\
    curl -sS -o - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - &&\
    echo "deb [arch=amd64]  http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list &&\
    apt-get -y update &&\
    apt-get -y install google-chrome-stable &&\
    wget https://chromedriver.storage.googleapis.com/2.41/chromedriver_linux64.zip &&\
    unzip chromedriver_linux64.zip &&\
    mv chromedriver /usr/bin/chromedriver &&\
    chown root:root /usr/bin/chromedriver &&\
    chmod +x /usr/bin/chromedriver &&\
    wget https://selenium-release.storage.googleapis.com/3.13/selenium-server-standalone-3.13.0.jar &&\
    wget http://www.java2s.com/Code/JarDownload/testng/testng-6.8.7.jar.zip &&\
    unzip testng-6.8.7.jar.zip &&\
    xvfb-run java -Dwebdriver.chrome.driver=/usr/bin/chromedriver -jar selenium-server-standalone.jar


RUN set -ex && \
    apt-get update -y && \
    apt-get install -y $PACKAGES && \
    apt-get install -y chromium &&\
    pip install -r /tmp/requirements.txt  && \
    cd /tmp/ && \
    apt-get remove -y $PACKAGES 

WORKDIR /opt/builder

COPY . /opt/builder
