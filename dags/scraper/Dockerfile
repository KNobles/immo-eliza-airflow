FROM python:3.10.8

COPY ./driver /app/driver
COPY ./data /app/data
COPY ./utils /app/utils
COPY ./main.py /app/main.py
COPY ./requirements.txt /app

RUN pip3 install -r /app/requirements.txt

WORKDIR /app

CMD ["python", "main.py"]