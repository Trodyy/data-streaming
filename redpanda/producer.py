<<<<<<< HEAD
from confluent_kafka import Producer
from api.crypto_api import CryptoAPI
import json


api = CryptoAPI()

configs = {
    'bootstrap.servers': 'kafka:9092'
}

def delivery_report(err, msg):
    if err:
        print(f"❌ Delivery failed: {err}")
    else:
        print(f"✅ Delivered {msg.value().decode('utf-8')}")  # Changed to single quotes
        print(f"✅ Delivered to {msg.topic()} : partition {msg.partition()} : at offset {msg.offset()}")

producer = Producer(configs)

real_data = api.get_data()


value = json.dumps(real_data).encode('utf-8')

producer.produce(
    topic='crypto_topic',
    value=value ,
    callback=delivery_report
)

producer.flush()
=======
#Hello world.
>>>>>>> main
