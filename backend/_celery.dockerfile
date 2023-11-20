FROM python:3.11.1

WORKDIR /backend

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y --no-install-recommends gcc
RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir celery[redis] flower

COPY ./app/app .
