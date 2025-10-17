import requests
import os
import time

class Test:
    def __init__(self):
        self.url = "https://api.freecryptoapi.com/v1/getData?symbol=BTC"
        self.headers = {
            'accept' : '*/*' ,
            'Authorization' : 'Bearer e6oxzv3qp6robho81kia'}  
        

    def get_data(self):
        while 1 :
            response = requests.get(self.url , headers=self.headers)
            print(response.json())
            time.sleep(5)



#### the follwing code is for api ######
#https://freecryptoapi.com/