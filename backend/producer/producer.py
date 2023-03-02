from flask import Blueprint, jsonify, request
from kafka import KafkaProducer
from PIL import Image
import io
import base64
import json

producer_bp = Blueprint('producer_bp', __name__)

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda x: json.dumps(x).encode('utf-8')
)

@producer_bp.route('/api/frame', methods=['POST'])
def send_frame():
    # get the frame from the request
    frame_data = request.json['imageData']
    image = Image.open(io.BytesIO(base64.b64decode(frame_data.split(',')[1])))

    # encode the frame as a base64 string
    buffer = io.BytesIO()
    image.save(buffer, format='JPEG')
    data = base64.b64encode(buffer.getvalue()).decode('utf-8')

    # create a dictionary to store the frame data
    frame_dict = {'data': data}

    # send the frame data to the 'frames' topic using Kafka
    producer.send('frames', value=frame_dict)
    producer.flush()

    return jsonify({'status': 'success'})
