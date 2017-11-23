FROM python:3-alpine

RUN mkdir /app
VOLUME /app
WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt
ENV PYTHONUNBUFFERED=1

COPY . /app

CMD [ "python", "./app.py" ]