FROM python:3.7
LABEL Maintainer="maikel-09"

WORKDIR /home
COPY ./app/ .
VOLUME /media
RUN apt-get -y update &&\
    apt-get -y upgrade &&\
    apt-get install -y ffmpeg &&\
    pip install --no-cache-dir -r requirements.txt --upgrade --quiet --disable-pip-version-check
CMD python ./teldit-downloader.py
