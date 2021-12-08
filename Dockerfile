FROM python:3.9.6-slim-buster

WORKDIR /usr/src/epam

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update

RUN pip install --upgrade pip

COPY ./requirements.txt /usr/src/epam/requirements.txt
RUN pip install -r /usr/src/epam/requirements.txt

COPY ./epam /usr/src/epam/

COPY entrypoint.sh /usr/src/epam/
RUN ["chmod", "+x", "/usr/src/epam/entrypoint.sh"]

ENTRYPOINT ["sh", "/usr/src/epam/entrypoint.sh"]