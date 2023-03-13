FROM python:3.8-slim-buster


WORKDIR /app
ADD . /app

COPY ./requirements.txt .

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . .

RUN pip3 install -r requirements.txt

EXPOSE 8080

ENTRYPOINT ["sh", "./entrypoint.sh"]
