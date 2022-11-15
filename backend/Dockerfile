# pull official base image
FROM python:3.10.8

# set work directory
WORKDIR /backend

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# # install psycopg2 dependencies for alpine
# RUN apk update \
#     && apk add postgresql-dev gcc python3-dev musl-dev

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# # copy project
# COPY . .
