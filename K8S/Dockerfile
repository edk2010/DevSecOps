FROM python:3.8-alpine
COPY ./requirements.txt /app/requirements.txt
COPY ./hostname.py /app
WORKDIR /app
RUN pip install -U pip
RUN pip install -r requirements.txt

CMD python /app/hostname.py
