import cv2
from kafka import KafkaConsumer
import numpy as np
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv(dotenv_path="../.env")

# Kafka configuration
KAFKA_TOPIC = os.getenv('KAFKA_TOPIC', 'distributed-streaming-system')
KAFKA_BROKER_URL = os.getenv('KAFKA_BROKER_URL', 'localhost:9092')

# OpenCV display window configuration
WINDOW_NAME = 'frame'

if __name__ == '__main__':
    # Create Kafka consumer
    consumer = KafkaConsumer(
        KAFKA_TOPIC,
        bootstrap_servers=KAFKA_BROKER_URL,
        value_deserializer=lambda x: cv2.imdecode(
            np.frombuffer(x, np.uint8),
            cv2.IMREAD_COLOR
        ),
    )

    # Open display window
    cv2.namedWindow(WINDOW_NAME, cv2.WINDOW_NORMAL)

    for frame in consumer:
        # Display the frame in the OpenCV window
        cv2.imshow(WINDOW_NAME, frame.value)

        # Exit on key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the Kafka consumer and OpenCV resources
    consumer.close()
    cv2.destroyAllWindows()
