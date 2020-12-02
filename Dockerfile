FROM python:3.8-alpine

COPY . /opt/mdcal

RUN pip install -e /opt/mdcal

CMD ["mdcal"]
