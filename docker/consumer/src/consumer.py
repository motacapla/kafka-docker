from kafka import KafkaConsumer
from json import loads
from time import sleep
consumer = KafkaConsumer(
    'topic_test',
    bootstrap_servers=['kafka-docker_kafka_1', 'kafka-docker_kafka_2'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='my-group-id',
    value_deserializer=lambda x: loads(x.decode('utf-8'))
)
for event in consumer:
    event_data = event.value
    print(event_data)
