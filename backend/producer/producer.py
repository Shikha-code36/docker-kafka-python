from flask import Blueprint, jsonify, request
from confluent_kafka import Producer
from flask_cors import cross_origin

producer_bp = Blueprint('producer_bp', __name__)

topic = 'frame_topic'

# Create Kafka producer instance
conf = {'bootstrap.servers': 'localhost:9092'}
producer = Producer(conf)

@producer_bp.route('/api/frame', methods=['POST'])
@cross_origin()
def send_frame():
    # Get frame data from request
    frame = request.data

    # Send frame to Kafka
    producer.produce(topic, value=frame)

    # Wait for any outstanding messages to be delivered
    producer.flush()

    return 'Frame sent to Kafka topic: {}'.format(topic)
