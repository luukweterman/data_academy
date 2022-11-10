import requests
import pandas as pd


class Import_StockPrices:
    #retrieving data from server
    response = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=MSFT&interval=5min&outputsize=full&apikey=demo")

    # Since we are retrieving stuff from a web service, it's a good idea to check for the return status code
    # See: https://en.wikipedia.org/wiki/List_of_HTTP_status_codes
    if response.status_code != 200:
        raise ValueError("Could not retrieve data, code:", response.status_code)

    # The service sends JSON data, we parse that into a Python datastructure
    raw_data = response.json()

    ## CREATING a Dataframe
    data = raw_data['Time Series (5min)']
    df = pd.DataFrame(data).T.apply(pd.to_numeric)

    # Next we parse the index to create a datetimeindex
    df.index = pd.DatetimeIndex(df.index)

    # Let's fix the column names by chopping off the first 3 characters
    df.rename(columns=lambda s: s[3:], inplace=True)
    print(df.head(20))

    print(df[['open', 'high', 'low', 'close']].plot())

    # Let's take last value of the close column for every business day
    close_per_day = df.close.resample('B').last()

    print(close_per_day.plot())

