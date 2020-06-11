FROM python:3.7-alpine
LABEL maintainer="mcweglowski@gmail.com"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN adduser -D user
RUN chown -R user:user /vol/
RUN chmod -R 755 /vol/
USER user