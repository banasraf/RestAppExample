FROM python:latest

COPY . /workspace

WORKDIR /workspace

RUN apt-get update && apt-get install -y dos2unix

RUN dos2unix qa/start_test_server.sh

RUN pip install -r requirements.txt
