FROM python:3.10-slim-buster

RUN apt update && apt upgrade -y
RUN apt install dash -y
WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .
RUN  addgroup --gid 1000  non-root && \
     adduser --gid 1000 --uid 1000 non-root --no-create-home --gecos GECOS --disabled-login
RUN chown -R non-root:non-root .

USER 1000

EXPOSE 8000
ENTRYPOINT  python3 app.py