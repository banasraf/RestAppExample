FROM python:latest

COPY . /workspace

WORKDIR /workspace

RUN apt-get update && apt-get install -y dos2unix

RUN dos2unix qa/test-migrate.sh && \
    chmod +x wait-for-it.sh

RUN pip install -r requirements.txt
