FROM python:3

ENV PYTHONUNBUFFERED 1

ARG projectDir=runn-backend

RUN mkdir ${projectDir}

WORKDIR /${projectDir}

COPY . /${projectDir}

RUN pip install -r requirements.txt