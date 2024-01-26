import requests

url = "https://api.upbit.com/v1/ticker"

headers = {
    "accept": "application/json"
}
params = {
    "markets": "KRW-XRP"
}

response = requests.get(url, headers=headers, params=params)
resJson = response.json()

print("{0} : {1}".format(resJson[0]["market"], resJson[0]["trade_price"]))

