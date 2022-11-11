import numpy as np

class Orders:
    def __init__(self, stock_name, choose_stock, investment_date):

    def buy_stock(self, stock_name, choose_stock, investment_date, quantity):
        self.choose_stock = input("Please select a stock to invest in. Fill in one of the options: TSCO_stock, GPV.TRV, DAI.DEX, SHH")
        if self.choose_stock not in ("TSCO_stock", "GPV.TRV", "DAI.DEX", "SHH"):
            print("Wrong option, please select TSCO_stock, GPV.TRV, DAI.DEX or SHH")
            self.choose_stock = input("Please select a stock to invest in. Fill in one of the options: TSCO_stock, GPV.TRV, DAI.DEX, SHH")
            print(self.stock_price)
        else:
            self.investment_date = input("Please choose a DAY after 2020-01-01, in the given format")
            if self.investment_date == np.nan:
                print("You selected a day where the stock is not available")
        self.quantity_stock = input("How many stocks do you want to buy? Select an integer."

        if self.quantity_stock not in ("TSCO_stock", "GPV.TRV", "DAI.DEX", "SHH"):
            print("Wrong option, please select TSCO_stock, GPV.TRV, DAI.DEX or SHH")

    def stock_price
        dataframe[]

class User:
    def __init__(self, name):
        self.name = name
        self.sharequantity = 10
        pass

class Stock:
    def __init__(self, name):
        self.Stock = 0
        self.name = name
        self.quantity =
        self.price = self.value
        pass