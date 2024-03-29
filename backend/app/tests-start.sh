#!/usr/bin/env bash

set -e
set -x

pipenv run pytest --cov=app --cov-report=term-missing app/tests "${@}"
