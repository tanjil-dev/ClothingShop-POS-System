# syntax=docker/dockerfile:1

FROM python:3.6-slim-buster

ENV PYTHONUNBUFFERED 1
WORKDIR /clothingStore

RUN apt-get update
RUN apt-get install python3-dev default-libmysqlclient-dev gcc  -y
COPY requirement.txt requirement.txt
RUN pip3 install -r requirement.txt

COPY . /clothingStore/
RUN mkdir /clothingStore/media

COPY clothingStore/.env_docker /clothingStore/clothingStore/.env
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8080"]