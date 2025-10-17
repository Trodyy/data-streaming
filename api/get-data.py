import requests
import os

url = "https://api.freecryptoapi.com/v1/getData?symbol=BTC"

headers = {
    'accept': '*/*',
    'Authorization': 'Bearer e6oxzv3qp6robho81kia'
}

response = requests.get(url, headers=headers)
print(response.json())



#### the follwing code is for api ######
#https://freecryptoapi.com/