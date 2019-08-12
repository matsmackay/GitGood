import requests
import pandas as pd


response = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=MSFT&interval=5min&outputsize=full&apikey=demo")

# Since we are retrieving stuff from a web service, it's a good idea to check for the return status code
# See: https://en.wikipedia.org/wiki/List_of_HTTP_status_codes
if response.status_code != 200:
    raise ValueError("Could not retrieve data, code:", response.status_code)

# The service sends JSON data, we parse that into a Python datastructure
raw_data = response.json()

# Let's look at the raw data (it's a lot so let's limit it)
raw_data.keys()

# This we probably don't need
raw_data['Meta Data']

# The actual time series is huge, let's just look at the first few items
# Let's use itertools to do this in a lazy way
import itertools
list(itertools.islice(raw_data['Time Series (5min)'].items(), 0,5))

# # Let's be smart and retrieve the name of the column with our actual data
# colname = list(raw_data.keys())[-1]
# # We want to extract the corresponding column only
# data = raw_data[colname]
#
# df = pd.DataFrame(data).T.apply(pd.to_numeric)
# df.info()
# df.head()
#
# # Next we parse the index to create a datetimeindex
# df.index = pd.DatetimeIndex(df.index)
#
# # Let's fix the column names
# df.rename(columns=lambda s: s[3:], inplace=True)
#
# df.info()