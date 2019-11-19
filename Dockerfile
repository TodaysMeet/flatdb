FROM python:3.7

ADD dist/flatdb-0.1.0-py3-none-any.whl /

VOLUME /data

RUN pip install flatdb-0.1.0-py3-none-any.whl


CMD [ "flatdb", "-p", "5001", "-b", "/data/", "-H", "0.0.0.0" ]
