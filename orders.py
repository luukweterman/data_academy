import numpy as np

class Buy_stock:
    def __init__(self):
        self.select_stock = ""

    def select_stock(self, select_stock):
        self.select_stock = input("Please select a stock to invest in. Fill in one of the options: TSCO_stock, GPV.TRV, DAI.DEX, SHH")
        if self.select_stock not in ("TSCO_stock", "GPV.TRV", "DAI.DEX", "SHH"):
            print("Wrong option, please select TSCO_stock, GPV.TRV, DAI.DEX or SHH")
            self.select_stock = input("Please select a stock to invest in. Fill in one of the options: TSCO_stock, GPV.TRV, DAI.DEX, SHH")
    pass

    def select_date(self, date):
        self.date = input("Please choose a DAY after 2020-01-01, in the given format")
        if self.date == np.nan:
            print("You selected a day where the stock price is not available")
            self.date = input("Please choose a DAY after 2020-01-01, in the given format")
    pass

print(Buy_stock.select_stock("", "TSCO_stock"))



#def select_quantity(self, quantity):
 #   self.quantity_stock = input("How many stocks do you want to buy? Select an integer."
  #  return f"You ordered {self.quantity_stock} from {self.select_stock}"



class User:
    def __init__(self, name):
        self.name = name
        self.sharequantity = 10
        pass

class Stock:
    def __init__(self, name):
        self.Stock = 0
        self.name = name
        self.quantity = 0
        self.price = self.value
        pass