FROM python:3-alpine

RUN addgroup -S user && adduser user -S -G user

WORKDIR /home/user/

COPY requirements.txt   .
COPY gunicorn_config.py .
COPY setup.py           .
COPY setup.cfg          .
COPY init_entrypoint.sh /

RUN pip install hypercorn
RUN pip install -r requirements.txt

USER user

EXPOSE 5000

ENTRYPOINT []

CMD hypercorn --config python:./gunicorn_config.py magnumopus.index:app

COPY magnumopus         magnumopus
