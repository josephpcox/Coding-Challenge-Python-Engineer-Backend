FROM python:3.7.4
MAINTAINER Code-Challenge-Developer
COPY *.py ./
WORKDIR /usr/local/bin
cmd ["hello.py"]