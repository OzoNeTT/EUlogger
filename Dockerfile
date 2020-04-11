FROM python:3.7-slim-buster

RUN set -ex && \
    mkdir /usr/share/man/man1/ &&\
    apt-get update -y &&\
    apt-get install -y gnupg2 \
                       curl \
                       unzip \
                       xvfb \
                       libxi6 \
                       libgconf-2-4 &&\
    curl -sS -o - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - &&\
    echo "deb [arch=amd64]  http://dl.google.com/linux/chrome/deb/ stable main" \
        >> /etc/apt/sources.list.d/google-chrome.list &&\
    apt-get -y update &&\
    apt-get -y install google-chrome-stable &&\
    wget https://chromedriver.storage.googleapis.com/2.41/chromedriver_linux64.zip &&\
    unzip chromedriver_linux64.zip &&\
    rm -rf chromedriver_linux64.zip && \
    mv chromedriver /usr/bin/chromedriver &&\
    chmod +x /usr/bin/chromedriver && \
    apt-get remove -y gnupg2 \
                       curl \
                       unzip \
                       xvfb \
                       libgconf-2-4

COPY requirements.txt /tmp/requirements.txt

RUN pip install -r /tmp/requirements.txt

WORKDIR /opt/builder

COPY . /opt/builder

CMD python logger.py $login $password
