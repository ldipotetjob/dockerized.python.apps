## This is a POC implementando CRU operation in Postgres with python

### Checking is postgres is ready in our docker compose(pg_isready):

´´´shell
healthcheck:
  test: ["CMD-SHELL", "pg_isready"]
  interval: 10s
  timeout: 5s
  retries: 5
´´´
> **Note**
> To check the connection status: https://www.postgresql.org/docs/current/app-pg-isready.html

### Run enviroment 

* docker compose up 

### Turn down environment

1. docker compose down
2. docker-compose down --volumes

> **Warning**
> We could implement Psycopg2 on Alpine in Docker from requirements.txt 
> so we use python:3.9, image from build from [buildpack-deps](https://github.com/docker-library/buildpack-deps)