import requests
print("Hello")
url = 'https://api.freecryptoapi.com/v1/getCryptoList'
header = {
    "accept": "*/*",
    "Authorization": "Bearer e6oxzv3qp6robho81kia"
}

response = requests.get(url , headers=header)
if response.status_code == 200 :
    value = response.json()
    print(value)
else :
    print(f"Error: {response.status_code}")
    print(response.text)


#### the follwing code is for api ######
#https://freecryptoapi.com/