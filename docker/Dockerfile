FROM python:3
USER root

RUN apt-get update
RUN pip install --upgrade pip && pip install --upgrade setuptools && pip install kafka-python
WORKDIR /usr/src
