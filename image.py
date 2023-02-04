import ccxt
import pandas as pd
import matplotlib.pyplot as plt

# # Initialize the exchange object
exchange = ccxt.binance()

# # Fetch the historical data for Bitcoin
symbol = "BTC/USDT"
timeframe = "1d"
ohlcv = exchange.fetch_ohlcv(symbol, timeframe)

# # Create a data frame from the data
# df = pd.DataFrame(ohlcv, columns=["timestamp", "open", "high", "low", "close", "volume"])

# # Convert the timestamp to a datetime object
# df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")



import requests

url = "https://api.blockchain.info/charts/transactions-per-second?timespan=5days&rollingAverage=8hours&format=json"

response = requests.get(url)

if response.status_code == 200:
    try:
        data = response.json()
        transactions_per_second = data["values"][-1]["y"]
        transactions_per_day = transactions_per_second * 86_400
        print("Bitcoin on-chain transaction volume: {:,.0f} transactions per day".format(transactions_per_day))

        # convert to dollars
        conversion_rate = 63000  # current rate: 1 BTC = 63000 USD
        transaction_volume_usd = transactions_per_day * conversion_rate
        print("Bitcoin on-chain transaction volume: ${:,.2f}".format(transaction_volume_usd))
    except ValueError:
        print("Could not parse response as JSON.")
else:
    print("Request failed with status code", response.status_code)
