FROM ubuntu:22.04 

ENV PYTHONUNBUFFERED 1
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get -y update && apt-get -y upgrade
RUN apt-get -y install \
    python3.11 \
    python3-pip \
    postgresql \
    postgresql-contrib

WORKDIR /usr/app
COPY ./requirements.txt ./

RUN pip3 install --upgrade pip setuptools wheel
RUN pip3 install -r ./requirements.txt
RUN pip3 install psycopg2-binary --no-binary psycopg2-binary

COPY ./ ./

RUN chmod +x ./scripts/*

RUN useradd admin
RUN chown -R admin:admin ./
USER admin

EXPOSE 8000

ENTRYPOINT ["sh", "./scripts/entrypoint.sh"]