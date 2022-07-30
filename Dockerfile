FROM python:3.9-slim-bullseye

WORKDIR /core_app

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONBUFFERED=1

COPY . .

RUN apt-get update && apt-get install --no-install-recommends -y \
    gcc libc-dev libpq-dev  python-dev libxml2-dev libxslt1-dev python3-lxml && apt-get install -y cron &&\
    pip install --no-cache-dir -r requirements.txt