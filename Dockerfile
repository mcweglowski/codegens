FROM python:3.7-alpine
LABEL maintainer="mcweglowski@gmail.com"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

WORKDIR /
COPY . .

CMD python -m helloworld