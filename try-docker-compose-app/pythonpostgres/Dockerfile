# syntax=docker/dockerfile:1
FROM python:3.12
WORKDIR /code
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install psycopg2
EXPOSE 5000
COPY . .
CMD ["flask", "run"]