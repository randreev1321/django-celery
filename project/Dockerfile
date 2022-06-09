# pull official base image
FROM python:3.9-alpine

# Install dependencies required for psycopg2 python package
RUN apk update && apk add libpq
RUN apk update && apk add --virtual .build-deps gcc postgresql-dev musl-dev


# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

# Remove dependencies only required for psycopg2 build
RUN apk del .build-deps

# copy project
COPY . /usr/src/app/

# run entrypoint.sh
CMD ["gunicorn", "core.wsgi", "0:8000"]
