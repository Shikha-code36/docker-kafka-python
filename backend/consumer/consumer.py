from kafka import KafkaConsumer
import cv2
import numpy as np
import json

consumer = KafkaConsumer('frames', bootstrap_servers=['localhost:9092'],
                         value_deserializer=lambda x: json.loads(x.decode('utf-8')))

for frame in consumer:
    nparr = np.fromstring(frame.value, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    # TODO: do some processing on the frame
