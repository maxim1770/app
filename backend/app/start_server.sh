#! /usr/bin/env bash

sleep 10

pipenv run uvicorn app.main:app --host=0.0.0.0 --port=8000