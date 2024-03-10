FROM alpine:latest
LABEL authors="hochmuch"

WORKDIR /app

COPY main.py /app/main.py

RUN apk update && apk add py3-psycopg2 py3-flask
CMD ["python3", "/app/main.py"]
