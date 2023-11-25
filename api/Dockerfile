# syntax = docker/dockerfile:1.4

FROM python:3.10

WORKDIR /api

COPY ./requirements.txt /api/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /api/requirements.txt

ENV PYTHONPATH "${PYTHONPATH}:/api/src"

COPY ./src /api/src

CMD ["uvicorn", "src.api:app", "--host", "0.0.0.0", "--port", "80", "--reload"]
