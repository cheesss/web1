import ccxt

binance = ccxt.binance({
'options': {
'adjustForTimeDifference': True
},
'enableRateLimit': True
})

a = binance.fetch_tickers()
print(a.keys())