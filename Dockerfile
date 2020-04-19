FROM python:3.7-alpine
ENV PYTHONUNBUFFERED 1

RUN mkdir /yamlapp
COPY requirements.txt /yamlapp/requirements.txt

WORKDIR /yamlapp
RUN pip install -r requirements.txt

COPY . /yamlapp/
