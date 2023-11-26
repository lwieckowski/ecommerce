# syntax = docker/dockerfile:1.4

FROM python:3.10

WORKDIR /api

COPY ./requirements.txt /api/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /api/requirements.txt

ENV PYTHONPATH "${PYTHONPATH}:/api/src"

COPY ./src /api/src
COPY ./test /api/test
