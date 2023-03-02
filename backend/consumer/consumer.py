from kafka import KafkaConsumer
from PIL import Image
import io
import base64
import json
import cv2
import numpy as np

# create a Kafka consumer instance
consumer = KafkaConsumer(
    'frames',
    bootstrap_servers=['localhost:9092'],
    value_deserializer=lambda x: json.loads(x.decode('utf-8')),
    auto_offset_reset='earliest'
)

# iterate over the messages in the 'frames' topic
for message in consumer:
    # get the frame data from the message value
    frame_data = message.value['data']

    # decode the frame data from base64
    image_data = base64.b64decode(frame_data)

    # open the image
    image = Image.open(io.BytesIO(image_data))

    # process the image
    # convert the image to grayscale
    gray_image = image.convert('L')

    # perform edge detection using the Canny algorithm
    edges = cv2.Canny(np.array(gray_image), 100, 200)

    # convert the edges back to an image
    processed_image = Image.fromarray(edges)

    # display the processed image
    cv2.imshow('Processed Image', np.array(processed_image))
    cv2.waitKey(1)
