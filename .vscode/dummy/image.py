import ccxt
import pandas as pd
import matplotlib.pyplot as plt
import time


exchange = ccxt.binance()
symbol = "BTC/USDT"


import requests

url = "https://api.blockchain.info/charts/transactions-per-second?timespan=5days&rollingAverage=8hours&format=json"

response = requests.get(url)

if response.status_code == 200:
    try:
        datas = response.json()
        transactions_per_second = datas["values"][-1]["y"]
        transactions_per_day = transactions_per_second * 86_400
        print(
            "Bitcoin on-chain transaction volume: {:,.0f} transactions per day".format(
                transactions_per_day
            )
        )

        # convert to dollars
        ticker = exchange.fetch_ticker(symbol)
        price = ticker["last"]
        transaction_volume_usd = transactions_per_day * price
        print(
            "Bitcoin on-chain transaction volume: ${:,.2f}".format(
                transaction_volume_usd
            )
        )
    except ValueError:
        print("Could not parse response as JSON.")
else:
    print("Request failed with status code", response.status_code)
