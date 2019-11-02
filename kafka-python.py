from kafka import KafkaProducer
from kafka.errors import KafkaError
import sys

print (sys.argv[1])
producer = KafkaProducer(bootstrap_servers=['149.62.156.214:3000'])


for _ in range(1):
    producer.send('pythontopic', str.encode(sys.argv[1]))
    producer.flush()