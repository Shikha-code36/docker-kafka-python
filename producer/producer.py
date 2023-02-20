import cv2
from kafka import KafkaProducer
import os

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

# Kafka configuration
KAFKA_TOPIC = os.getenv('KAFKA_TOPIC', 'distributed-streaming-system')
KAFKA_BROKER_URL = os.getenv('KAFKA_BROKER_URL', 'kafka:9092')

# OpenCV camera capture configuration
CAMERA_DEVICE_INDEX = int(os.getenv('CAMERA_DEVICE_INDEX', 0))
CAMERA_WIDTH = int(os.getenv('CAMERA_WIDTH', 640))
CAMERA_HEIGHT = int(os.getenv('CAMERA_HEIGHT', 480))

if __name__ == '__main__':
    # Create Kafka producer
    producer = KafkaProducer(
        bootstrap_servers=KAFKA_BROKER_URL,
        value_serializer=lambda x: x.tobytes(),
    )

    # Open camera capture
    cap = cv2.VideoCapture(CAMERA_DEVICE_INDEX)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, CAMERA_WIDTH)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, CAMERA_HEIGHT)

    while True:
        # Capture a frame from the camera
        ret, frame = cap.read()

        # Check if the frame was successfully captured
        if not ret:
            break

        # Send the frame to the Kafka topic
        producer.send(KAFKA_TOPIC, frame)

    # Release the camera and Kafka producer resources
    cap.release()
    producer.close()
