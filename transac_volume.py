import requests
import matplotlib.pyplot as plt
import pandas as pd
import datetime
import ccxt

url = "https://api.blockchain.info/charts/n-transactions?format=json&timespan=30days"

response = requests.get(url)
data = response.json()

dates = []
volumes = []
for point in data['values']:
    dates.append(datetime.datetime.fromtimestamp(point['x']).strftime('%Y-%m-%d'))
    volumes.append(point['y'])

df = pd.DataFrame({'date': dates, 'volume': volumes})
df['volume'] = df['volume'].astype(int)




exchange = ccxt.binance()
symbol = 'BTC/USDT'
dates = []
 = []
url = "https://api.blockchain.info/charts/transactions-per-second?timespan=5days&rollingAverage=8hours&format=json"
response = requests.get(url)
if response.status_code == 200:
    try:
        datas = response.json()
        for i in range(-30, 0):
            transactions_per_second = datas["values"][i]["y"]
            transactions_per_day = transactions_per_second * 86_400
            print("Bitcoin on-chain transaction volume: {:,.0f} transactions per day".format(transactions_per_day))

        # convert to dollars
        ticker = exchange.fetch_ticker(symbol)
        price = ticker['last']
        transaction_volume_usd = transactions_per_day * price
        print("Bitcoin on-chain transaction volume: ${:,.2f}".format(transaction_volume_usd))
    except ValueError:
        print("Could not parse response as JSON.")
else:
    print("Request failed with status code", response.status_code)

print(datas["values"]["y"])

# df.set_index('date', inplace=True)
# df.plot(kind='line', figsize=(12, 6), color='blue')
# plt.xlabel("Date")
# plt.ylabel("Transaction Volume (BTC)")
# plt.title("Bitcoin On-Chain Transaction Volume")
# plt.show()