import requests
import pandas as pd
import numpy as np

#retrieving data from server
client = requests.Session() #added this to make it faster (RJ recommended)
response2 = client.get("https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=TSCO.LON&outputsize=full&apikey=demo")
response3 = client.get("https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=GPV.TRV&outputsize=full&apikey=demo")
response4 = client.get("https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=000002.SHZ&outputsize=full&apikey=demo")
#response4 = client.get("https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=DAI.DEX&outputsize=full&apikey=demo")
# #changed the stock to 000002.SHZ since the DAI.DEX did not have values
# response5 = client.get("https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=600104.SHH&outputsize=full&apikey=demo")

# The service sends JSON data, we parse that into a Python datastructure
raw_data2 = response2.json()
raw_data3 = response3.json()
raw_data4 = response4.json()
# raw_data5 = response5.json()

## CREATING a Dataframe
data2 = raw_data2['Time Series (Daily)']
data3 = raw_data3['Time Series (Daily)']
data4 = raw_data4['Time Series (Daily)']
# data5 = raw_data5['Time Series (Daily)']

df2 = pd.DataFrame(data2).T.apply(pd.to_numeric)
df3 = pd.DataFrame(data3).T.apply(pd.to_numeric)
df4 = pd.DataFrame(data4).T.apply(pd.to_numeric)
# df5 = pd.DataFrame(data5).T.apply(pd.to_numeric)

dataframe = pd.DataFrame()
dataframe['TSCO_stock'] = df2['4. close']
dataframe['GPV.TRV'] = df3['4. close']
dataframe['000002.SHZ'] = df4['4. close']
# dataframe['SHH'] = df5['4. close']

stock_list = list(dataframe.columns)
print(stock_list)

dataframe.info() #changed the code here

#df2 = pd.DataFrame(data2).T.apply(pd.to_numeric)
#df3 = pd.DataFrame(data3).T.apply(pd.to_numeric)
#df4 = pd.DataFrame(data4).T.apply(pd.to_numeric)
#df5 = pd.DataFrame(data5).T.apply(pd.to_numeric)
df = dataframe


#retrieve the latest price for the TSCO stock
def stockprice(price_series, stock_name):
    price = price_series[stock_name]
    last_price = price[0]
    return last_price

print(stockprice(df, stock_list[0]))

def order(dataframe, stock_name):
    #inputs

    cash = int(input("Enter your cash balance: "))
    buy_or_sell = input("Enter your whether you want to buy [B] or sell [S]: ")
    quantity = int(input("Enter the amount of stocks: "))
    stock_price = stockprice(dataframe, stock_name)

    #transaction and balance settlement

    price = stock_price * quantity
    if buy_or_sell == 'B':
        cash_balance = cash - price
        print(cash_balance)
    elif buy_or_sell == 'S':
        cash_balance = cash + price
        print(cash_balance)
    else:
        print("Please select the option buy [B] or sell [S]")


    #condition statement
    if cash_balance < 0:
        print("Transaction failed due to insufficient cash balance.")
        return f"This is your cash balance: {cash_balance}."
    else:
        print("Transaction not failed.")
        return f"This is your cash balance: {cash_balance}."

order(df, stock_list[0])




# create a user
# class User:
#     def __init__(self):
#         self.cash_balance = int(input("Insert you current cash balance: "))
#
#     #stockprice
#     def stockprice(self, price_series):
#         price = price_series.TSCO_stock[0]
#         return price
#     #buy function
#     def buy(self, price_series):
#
#         self.cash_balance -= stockprice(price_series)
#         print(f"Cash: {self.cash_balance}")
#
#     def __str__(self):
#         return f"This user has {self.cash_balance} units of cash."
#
#
# #run the class
# if __name__ == "__main__":
#     user = User()
#     user.buy(df)
#     print(user)






