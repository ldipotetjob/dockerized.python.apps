## This is a POC implementing CRU operation in Postgres with python

### Checking if postgres is ready in our docker compose(pg_isready):

```shell
healthcheck:
  test: ["CMD-SHELL", "pg_isready"]
  interval: 10s
  timeout: 5s
  retries: 5
```
> **Note**
> To check the connection status: https://www.postgresql.org/docs/current/app-pg-isready.html

### Run enviroment 

* docker compose up 
* docker compose up --build: for rebuilding again

### Turn down environment

1. docker compose down
2. docker-compose down --volumes

### call pl into the container when it is up 
1. docker exec -ti lambda-db bash
2. psql -h lambda-db -U genhub

> <picture>
>   <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/Mqxx/GitHub-Markdown/main/blockquotes/badge/light-theme/issue.svg">
>   <img alt="Issue" src="https://raw.githubusercontent.com/Mqxx/GitHub-Markdown/main/blockquotes/badge/dark-theme/issue.svg">
> </picture><br>
>
> We couldn't implement Psycopg2 on Alpine in Docker from requirements.txt. We face a common [Error: pg_config executable not found](https://raw.githubusercontent.com/ldipotetjob/dockerized.python.apps/main/try-docker-compose-app/pythonpostgres/error.txt) 
> so we use python:3.9, image from build from [buildpack-deps](https://github.com/docker-library/buildpack-deps)

</br>

> <picture>
>   <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/Mqxx/GitHub-Markdown/main/blockquotes/badge/light-theme/solution.svg">
>   <img alt="Solution" src="https://raw.githubusercontent.com/Mqxx/GitHub-Markdown/main/blockquotes/badge/dark-theme/solution.svg">
> </picture><br>
>
     ```shell
    RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install psycopg2
    ```
