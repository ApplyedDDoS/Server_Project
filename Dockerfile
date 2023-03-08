<<<<<<< HEAD
FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000"]
=======
#FROM python:3
#ADD requirements.txt /
#RUN pip install -r requirements.txt
#ADD app/manage.py /
#ADD app/db.sqlite3 /
#ADD app/templates /
#ADD app/httpApp /
#ADD app/DDoS /
#ADD app/Clients_net /
#CMD ["python", "./manage.py", "runserver"]

#FROM python:3.7-alpine
FROM python:3
MAINTAINER ISSL

ENV PYTHONUNBUFFERED 1

#COPY ./requirements.txt /requirements.txt
ADD requirements.txt /
#RUN apk add --update --no-cache postgresql-client jpeg-dev
#RUN apk add --update --no-cache --virtual .tmp-build-deps \
#      gcc libc-dev linux-headers postgresql-dev musl-dev zlib zlib-dev
RUN pip install -r requirements.txt
#RUN apk del .tmp-build-deps

RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static
#RUN adduser -D user
#RUN chown -R user:user /vol/
#RUN chmod -R 755 /vol/web
#USER user


#### Command: docker build -t  eminentmineta/ddos_server:0.1 .
>>>>>>> 64326c1293086fd44f077341bd1ec195715b2cbb
