import os
import cv2
import numpy as np
from kafka import KafkaConsumer

# Set up Kafka consumer
consumer = KafkaConsumer(
    'frames',
    bootstrap_servers=['kafka:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='my-group')

# Set up output directory for processed frames
output_dir = 'processed_frames'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Process frames up to a certain limit
frame_limit = 100
for i, message in enumerate(consumer):
    # Break if we have reached the frame limit
    if i >= frame_limit:
        break

    # Convert message to OpenCV image
    nparr = np.frombuffer(message.value, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # Apply image processing
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blurred, 50, 150)
    kernel = np.ones((5, 5), np.uint8)
    dilation = cv2.dilate(edges, kernel, iterations=1)
    img = cv2.cvtColor(dilation, cv2.COLOR_GRAY2BGR)

    # Save processed image to disk
    output_path = os.path.join(output_dir, f'frame_{i}.jpg')
    cv2.imwrite(output_path, img)
