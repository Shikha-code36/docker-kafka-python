FROM python:3.8

RUN apt-get update && apt-get install -y libgl1-mesa-glx \
    libopencv-dev \
    python3-opencv \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD [ "python", "./producer.py" ]
