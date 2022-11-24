FROM python:3.10.8

RUN mkdir /app
WORKDIR /app
COPY ./driver /app/driver
COPY ./data /app/data
COPY ./utils /app/utils
COPY ./main.py /app/main.py
COPY ./requirements.txt /app

RUN apt update -y
RUN apt install firefox-esr -y
RUN pip3 install -r /app/requirements.txt

CMD ["python", "main.py"]