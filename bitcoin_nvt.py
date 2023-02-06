import requests
import matplotlib.pyplot as plt
import pandas as pd
import datetime


#거래총량
url = "https://api.blockchain.info/charts/n-transactions?format=json&timespan=30days"

response = requests.get(url)
data = response.json()

dates = []
volumes = []	#날짜와 거래량 데이터를 넣을 빈 리스트를 준비합니다.
for point in data['values']:
    dates.append(datetime.datetime.fromtimestamp(point['x']).strftime('%Y-%m-%d'))
    volumes.append(point['y'])
    #가져온 데이터 안의 날짜 정보를 %Y-%m-%d형태로 가공하여, 그래프 x축에 사용할 날짜 리스트에 넣습니다

df = pd.DataFrame({'date': dates, 'volume': volumes})
df['volume'] = df['volume'].astype(int)
print(df)
#데이터프레임을 만들어 각 x축과 y축에 데이터를 넣은 후, 거래량 데이터를 int 형식으로 바꿔줍니다.

# df.set_index('date', inplace=True)
# df.plot(kind='line', figsize=(12, 6), color='blue')
# plt.xlabel("Date")
# plt.ylabel("Transaction Volume (BTC)")
# plt.title("Bitcoin On-Chain Transaction Volume")
# plt.show()			#그래프를 그려줍니다.


