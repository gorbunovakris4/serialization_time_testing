FROM python:3.10

COPY . /app/

WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 2001/udp

ENTRYPOINT ["python3", "-u", "pickle_tst.py"]
