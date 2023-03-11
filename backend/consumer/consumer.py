from confluent_kafka import Consumer, KafkaError
import cv2

topic = 'frame_topic'

# Create Kafka consumer instance
conf = {'bootstrap.servers': 'localhost:9092', 'group.id': 'my_group',
        'auto.offset.reset': 'earliest'}
consumer = Consumer(conf)
consumer.subscribe([topic])

# Create window to display frames
cv2.namedWindow('frame', cv2.WINDOW_NORMAL)

def process_frame(frame):
    # Process frame here (e.g. apply filters, etc.)
    # Return processed frame
    return frame

while True:
    msg = consumer.poll(1.0)

    if msg is None:
        continue
    if msg.error():
        if msg.error().code() == KafkaError._PARTITION_EOF:
            print('End of partition reached {0}/{1}'
                  .format(msg.topic(), msg.partition()))
        else:
            print('Error while consuming message: {0}'.format(msg.error()))
    else:
        # Decode frame from bytes and process it
        frame_bytes = msg.value()
        frame = cv2.imdecode(frame_bytes, cv2.IMREAD_COLOR)
        processed_frame = process_frame(frame)

        # Display the processed frame
        cv2.imshow('frame', processed_frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Release the resources
consumer.close()
cv2.destroyAllWindows()
