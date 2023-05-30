FROM tiangolo/uvicorn-gunicorn:python3.11

RUN python -m pip install --upgrade pip
COPY ./app/Pipfile .
COPY ./app/Pipfile.lock .
RUN pip install pipenv
RUN pipenv lock
RUN pipenv --rm
RUN pipenv install --ignore-pipfile

COPY ./app /app
ENV PYTHONPATH=/app

EXPOSE 8000