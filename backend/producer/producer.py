from flask import Blueprint, jsonify, request
from kafka import KafkaProducer
import base64
import json
import cv2
import numpy as np

producer_bp = Blueprint('producer_bp', __name__)

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x: json.dumps(x).encode('utf-8'))

@producer_bp.route('/api/frame', methods=['POST'])
def send_frame():
    # get the frame from the request
    frame_data = request.data
    nparr = np.fromstring(frame_data, np.uint8)
    frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # encode the frame as a base64 string
    retval, buffer = cv2.imencode('.jpg', frame)
    data = base64.b64encode(buffer).decode('utf-8')

    # create a dictionary to store the frame data
    frame_dict = {'data': data}

    # send the frame data to the 'frames' topic using Kafka
    producer.send('frames', value=frame_dict)
    producer.flush()

    return jsonify({'status': 'success'})
