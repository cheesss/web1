import requests

url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=bitcoin"

response = requests.get(url)
data = response.json()

market_cap = data[0]['market_cap']
print("Bitcoin market cap: ${:,.2f}".format(market_cap))