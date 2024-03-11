FROM alpine:latest
LABEL authors="hochmuch"

WORKDIR /app

COPY main.py /app/main.py
EXPOSE 443
RUN apk update && apk add py3-psycopg2 py3-flask py3-requests py3-flask-cors
CMD ["python3", "/app/main.py"]
