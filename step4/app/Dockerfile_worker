FROM python:3.6-alpine

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

ENTRYPOINT celery -A worker.celery worker --loglevel=debug
