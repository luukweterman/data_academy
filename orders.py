import numpy as np

#### order class

class Order:
    def __init__(self, stock, date, quantity):
        self.stock = stock
        self.date = date
        self.quantity = quantity

    def __str__(self):
        return f"Player bought {self.quantity} stocks {self.stock} on {self.date}."

##### User input

cash_balance = int(input("What is you cash_balance?: "))
continue_game = "Y"

while continue_game == "Y":
    stock_name = input("Please select a stock to invest in. Fill in one of the options: TSCO_stock, GPV.TRV, DAI.DEX, SHH: ").strip().upper()
    if stock_name not in ("TSCO_stock", "GPV.TRV", "DAI.DEX", "SHH"):
        print("Wrong option, please select TSCO_stock, GPV.TRV, DAI.DEX or SHH")
        ### use stock_name as input for Luuk's retrieving of stock_price
    else:
        stock_date = input("Please choose a DAY after 2020-01-01, in the given format: ").strip().upper()
        if stock_date == np.nan:
            print("You selected a day where the stock price is not available")
            ### use stock_name as input for Luuk's retrieving of stock_price
        else:
            stock_quantity = int(input("Please choose the amount of stocks you want to buy. Select an integer: ").strip())
            #stock_price = from Luuks function
            if stock_quantity > cash_balance: #need to multiply with stock_price here
                print("You selected more stocks than you have money")
            else:
                cash_balance = cash_balance #- stock_price
                print(f"You have {cash_balance} left")
                continue_game = input("Do you like to buy more stocks? (Y/N): ")
                if continue_game == "N":
                    print("Game Finished")
                    break


player1 = Order(stock_name, stock_date, stock_quantity)
player2 = Order(stock_name, stock_date, stock_quantity)
player1.__str__()
player2.__str__()
