from time import sleep
from json import dumps
from kafka import KafkaProducer
producer = KafkaProducer(
    bootstrap_servers=['kafka-docker_kafka_1', 'kafka-docker_kafka_2'],
    value_serializer=lambda x: dumps(x).encode('utf-8')
)
for j in range(9999):
    print("Iteration", j)
    data = {'counter': j}
    producer.send('topic_test', value=data)
    sleep(0.5)
