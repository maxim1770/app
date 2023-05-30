#! /usr/bin/env bash

sleep 10
pipenv run python app/initial_data.py

pipenv run uvicorn app.main:app --host=0.0.0.0 --port=8000