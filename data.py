import requests
import pandas as pd
import numpy as np

#retrieving data from server
client = requests.Session() #added this to make it faster (RJ recommended)
response2 = client.get("https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=TSCO.LON&outputsize=full&apikey=demo")
# response3 = client.get("https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=GPV.TRV&outputsize=full&apikey=demo")
# response4 = client.get("https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=000002.SHZ&outputsize=full&apikey=demo")
# #response4 = client.get("https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=DAI.DEX&outputsize=full&apikey=demo")
# #changed the stock to 000002.SHZ since the DAI.DEX did not have values
# response5 = client.get("https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=600104.SHH&outputsize=full&apikey=demo")

# The service sends JSON data, we parse that into a Python datastructure
raw_data2 = response2.json()
# raw_data3 = response3.json()
# raw_data4 = response4.json()
# raw_data5 = response5.json()

## CREATING a Dataframe
data2 = raw_data2['Time Series (Daily)']
# data3 = raw_data3['Time Series (Daily)']
# data4 = raw_data4['Time Series (Daily)']
# data5 = raw_data5['Time Series (Daily)']

df2 = pd.DataFrame(data2).T.apply(pd.to_numeric)
# df3 = pd.DataFrame(data3).T.apply(pd.to_numeric)
# df4 = pd.DataFrame(data4).T.apply(pd.to_numeric)
# df5 = pd.DataFrame(data5).T.apply(pd.to_numeric)

print(df2.head())

dataframe = pd.DataFrame()
dataframe['TSCO_stock'] = df2['4. close']
# dataframe['GPV.TRV'] = df3['4. close']
# dataframe['000002.SHZ'] = df4['4. close']
# dataframe['SHH'] = df5['4. close']

dataframe.info() #changed the code here
print(dataframe.head()) #added to show overall stock closing prices

#df2 = pd.DataFrame(data2).T.apply(pd.to_numeric)
#df3 = pd.DataFrame(data3).T.apply(pd.to_numeric)
#df4 = pd.DataFrame(data4).T.apply(pd.to_numeric)
#df5 = pd.DataFrame(data5).T.apply(pd.to_numeric)
df = dataframe


#retrieve the latest price for the TSCO stock
def stockprice(price_series):
    price = price_series.TSCO_stock[0]
    return price

print(stockprice(df))
def order_buy(dataframe):
    #inputs
    cash = int(input("Enter your cash balance: "))
    quantity = int(input("Enter the amount of stocks you want to buy: "))


    #transaction and balance settlement
    stock_price = stockprice(dataframe)
    buy_price = stock_price * quantity
    cash_balance = cash - buy_price

    #condition statement for sale and cas
    if cash_balance < 0:
        print("Transaction failed.")
        return f"This is your cash balance: {cash_balance}."
    else:
        print("Transaction not failed.")
        return f"This is your cash balance: {cash_balance}."

order_buy(df)

