import requests
import pandas as pd

#retrieving data from server
response2 = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=TSCO.LON&outputsize=full&apikey=demo")
response3 = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=GPV.TRV&outputsize=full&apikey=demo")
response4 = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=DAI.DEX&outputsize=full&apikey=demo")
response5 = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=600104.SHH&outputsize=full&apikey=demo")

# The service sends JSON data, we parse that into a Python datastructure
raw_data2 = response2.json()
raw_data3 = response3.json()
raw_data4 = response4.json()
raw_data5 = response5.json()

## CREATING a Dataframe
data2 = raw_data2['Time Series (Daily)']
data3 = raw_data3['Time Series (Daily)']
data4 = raw_data4['Time Series (Daily)']
data5 = raw_data5['Time Series (Daily)']

df2 = pd.DataFrame(data2).T.apply(pd.to_numeric)
df3 = pd.DataFrame(data3).T.apply(pd.to_numeric)
df4 = pd.DataFrame(data4).T.apply(pd.to_numeric)
df5 = pd.DataFrame(data5).T.apply(pd.to_numeric)

print(df2.head())

dataframe = pd.DataFrame()
dataframe['TSCO_stock'] = df2['4. close']
dataframe['GPV.TRV'] = df3['4. close']
dataframe['DAI.DEX'] = df4['4. close']
dataframe['SHH'] = df5['4. close']

print(dataframe.info)


#df2 = pd.DataFrame(data2).T.apply(pd.to_numeric)
#df3 = pd.DataFrame(data3).T.apply(pd.to_numeric)
#df4 = pd.DataFrame(data4).T.apply(pd.to_numeric)
#df5 = pd.DataFrame(data5).T.apply(pd.to_numeric)
