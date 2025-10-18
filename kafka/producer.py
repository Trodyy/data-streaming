from confluent_kafka import Producer
from api.crypto_api import CryptoAPI

test = CryptoAPI()
test.get_data()