import requests
import matplotlib.pyplot as plt
import pandas as pd
import datetime

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

total_volume = df['volume'].sum()
print("The total bitcoin on-chain transaction volume is:", total_volume)

df.set_index('date', inplace=True)
df.plot(kind='line', figsize=(12, 6), color='blue')
plt.xlabel("Date")
plt.ylabel("Transaction Volume (BTC)")
plt.title("Bitcoin On-Chain Transaction Volume")
plt.show()