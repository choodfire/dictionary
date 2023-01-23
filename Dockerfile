FROM python:3.10

RUN apt update;

RUN pip install --upgrade pip
COPY ./requirements.txt /tmp
RUN pip install -r /tmp/requirements.txt; rm /tmp/requirements.txt

COPY . /opt/app
WORKDIR /opt/app

RUN apt install npm -y
RUN npm install bootstrap

EXPOSE 8080

CMD ./manage.py migrate; ./manage.py runserver 0.0.0.0:8080