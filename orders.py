import numpy as np
import requests
import pandas as pd

#### Data retrieval class

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
##### Functions
def stockprice(price_series, stock_name):
    price = price_series[stock_name]
    last_price = price[0]
    return last_price

def order(dataframe):
    #inputs

    cash = int(input("Enter your cash balance: "))
    buy_or_sell = input("Enter your whether you want to buy [B] or sell [S]: ")
    quantity = int(input("Enter the amount of stocks: "))
    stock_price = stockprice(dataframe)

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
#TESTING

stockprice(dataframe, 'TSCO_stock')
##### User input


continue_game = "Y"
while continue_game == "Y":
    stock_name = input("Please select a stock to invest in. Fill in one of the options: TSCO_stock, GPV.TRV, 000002.SHZ: ").strip().upper()
    if stock_name not in stock_list:
        print("Wrong option, please select TSCO_stock, GPV.TRV or 000002.SHZ")

        ### use stock_name as input for Luuk's retrieving of stock_price
    else:
        last_price = stockprice(dataframe, stock_name)
        stock_date = input("Please choose a DAY after 2020-01-01, in the given format: ").strip().upper()
        if stock_date == np.nan:
            print("You selected a day where the stock price is not available")
            ### use stock_name as input for Luuk's retrieving of stock_price
        else:
            order(dataframe)
            stock_quantity = int(input("Please choose the amount of stocks you want to buy. Select an integer: ").strip())
            #stock_price = from Luuks function
            continue_game = input("Do you like to buy more stocks? (Y/N): ")
            if continue_game == "N":
                    print("Game Finished")
                    break


# player1 = Order(stock_name, stock_date, stock_quantity)
# player2 = Order(stock_name, stock_date, stock_quantity)
# player1.__str__()
# player2.__str__()