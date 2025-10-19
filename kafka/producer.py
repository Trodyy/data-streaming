from confluent_kafka import Producer
from api.crypto_api import CryptoAPI


api = CryptoAPI()

configs = {
    'bootstrap.servers': 'kafka:9092'
}


producer = Producer(configs)

real_data = api.get_data()

