FROM ubuntu:14.04
MAINTAINER Visualizacion de resultados G1 - 17/18

RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y python3-pip python3 build-essential libmysqlclient-dev

ENV DATABASE_URL g1_mariadb
ENV DATABASE_PORT 3306
ENV DATABASE_VOTE_USER votaciones-user
ENV DATABASE_VOTE_PASS votaciones-user-1928

COPY ./vr /app/vr
COPY ./main.py /app
COPY ./test.py /app
COPY ./deploy/requeriments.txt /app
WORKDIR /app

RUN pip3 install --upgrade pip
RUN pip3 install -r requeriments.txt

CMD ["python3", "main.py"]

EXPOSE 5000:52008
