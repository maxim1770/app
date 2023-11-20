FROM python:3.11.1

RUN mkdir -p ~/.postgresql && \
wget "https://storage.yandexcloud.net/cloud-certs/CA.pem" \
     --output-document ~/.postgresql/root.crt && \
chmod 0600 ~/.postgresql/root.crt

WORKDIR /backend

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1


RUN apt-get update && apt-get install -y --no-install-recommends gcc
RUN python -m pip install --upgrade pip
COPY ./app/Pipfile .
COPY ./app/Pipfile.lock .
RUN pip install pipenv

RUN bash -c "pipenv install --dev"

COPY ./app .
ENV PYTHONPATH=.

COPY ./app/start_server.production.sh /start_server.production.sh
RUN chmod +x /start_server.production.sh
ENTRYPOINT "/start_server.production.sh"

EXPOSE 8000