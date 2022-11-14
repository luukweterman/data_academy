
## 0. Libraries
import requests
import pandas as pd

## 1. Data

#retrieving data from server
client = requests.Session() #added this to make it faster (RJ recommended)
response2 = client.get("https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=TSCO.LON&outputsize=full&apikey=demo")
response3 = client.get("https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=GPV.TRV&outputsize=full&apikey=demo")
response4 = client.get("https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=000002.SHZ&outputsize=full&apikey=demo")

# The service sends JSON data, we parse that into a Python datastructure
raw_data2 = response2.json()
raw_data3 = response3.json()
raw_data4 = response4.json()

## CREATING a Dataframe
data2 = raw_data2['Time Series (Daily)']
data3 = raw_data3['Time Series (Daily)']
data4 = raw_data4['Time Series (Daily)']

df2 = pd.DataFrame(data2).T.apply(pd.to_numeric)
df3 = pd.DataFrame(data3).T.apply(pd.to_numeric)
df4 = pd.DataFrame(data4).T.apply(pd.to_numeric)

dataframe = pd.DataFrame()
dataframe['TSCO.stock'] = df2['4. close']
dataframe['GPV.TRV'] = df3['4. close']
dataframe['000002.SHZ'] = df4['4. close']

# stock_list = list(dataframe.columns)
# print(stock_list)

##### Functions
def stockprice(price_series, stock_name):
    price = price_series[stock_name]
    last_price = price[0]
    return last_price
def order(dataframe, stock_name):
    #inputs

    cash = int(input("Enter your cash balance: "))
    buy_or_sell = input("Enter you whether you want to buy [B] or sell [S]: ")
    quantity = int(input("Enter the amount of stocks: "))
    stock_price = stockprice(dataframe, stock_name)

    #transaction and balance settlement

    price = stock_price * quantity
    if buy_or_sell == 'B':
        cash_balance = cash - price
        #print(cash_balance)
        print(f"This is your cash balance: {cash_balance}.")
    elif buy_or_sell == 'S':
        cash_balance = cash + price
        print(f"This is your cash balance: {cash_balance}.")
    else:
        print("Please select the option buy [B] or sell [S]")

    #condition statement
    if cash_balance < 0:
        print("Transaction failed due to insufficient cash balance.")
        return f"This is your cash balance: {cash_balance}."
    else:
        print("Transaction succeeded.")
        return f"This is your cash balance: {cash_balance}."

##### User input

continue_game = "Y"
while continue_game == "Y":
    stock_name = input("Please select a stock to invest in. Fill in one of the options: TSCO.stock, GPV.TRV, 000002.SHZ: ").strip().upper()
    if stock_name not in stock_list:
        print("Wrong option, please select TSCO.stock, GPV.TRV or 000002.SHZ")

        ### use stock_name as input for Luuk's retrieving of stock_price
    else:
        order(dataframe, stock_name)
        continue_game = input("Do you like to buy/sell more stocks? (Y/N): ")
        if continue_game == "N":
                print("Game Finished")
                break


