#! /usr/bin/env bash

sleep 10

pipenv run gunicorn --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000 app.main:app
