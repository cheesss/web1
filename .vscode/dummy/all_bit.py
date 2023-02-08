import requests
import matplotlib.pyplot as plt
import pandas as pd
import datetime

# make a GET request to CoinGecko API to get market cap data
url = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=usd&days=30"
response = requests.get(url)
data = response.json()

# extract the required data from the API response
market_cap_data = [
    (datetime.datetime.fromtimestamp(item[0] / 1000).strftime("%Y-%m-%d"), item[1])
    for item in data["prices"]
]

# convert the extracted data into a Pandas data frame
df = pd.DataFrame(market_cap_data, columns=["Date", "Market Cap"])

# average the data by day
df = df.groupby("Date").mean().reset_index()

# get the current date
# current_date = datetime.datetime.now().strftime("%Y-%m-%d")
# # check if the current date is already in the data frame
# if current_date not in df['Date'].tolist():
#     # add the data for the current date to the last row of the data frame
#     df = df.append({'Date': current_date, 'Market Cap': df['Market Cap'][-1]}, ignore_index=True)
# 날짜 검사 후 오늘 데이터가 없으면 추가해주는 코드

print(df)
# plot the data using Matplotlib
plt.plot(df["Date"], df["Market Cap"])
plt.xlabel("Date")
plt.ylabel("Market Cap (in USD)")
plt.title("Bitcoin Market Cap for the Last 30 Days (averaged by day)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 시총 구하는 코드
