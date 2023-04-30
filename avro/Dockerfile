FROM python:3.10

COPY . /app/

WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 2005/udp

ENTRYPOINT ["python3", "-u", "avro_tst.py"]
