FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt .

RUN apt-get update && \
    apt-get install -y libqt5gui5 && \
    rm -rf /var/lib/apt/lists/*

ENV QT_DEBUG_PLUGINS=1

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "consumer.py" ]
