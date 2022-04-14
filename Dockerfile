FROM python:3.7.9-slim-stretch

MAINTAINER Ilya Gorchakov <brainburst54@gmail.com>

RUN mkdir /app

COPY . /app/
