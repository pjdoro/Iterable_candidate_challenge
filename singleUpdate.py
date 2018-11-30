import pandas as pd
import requests
# Specify target API and valid key
url = "https://api.iterable.com/api/users_bulkUpdateUser"
api_key = '123' #Here is where you would define a valid API_key
# Read csv into dataframe
data = 'Tomato_data.csv'
df = pd.read_csv(data)
# indicate the row number in the csv to post update
rec = 0
# Create payload for POST request
payload =[(x,df.iloc[rec][x]) for x in list(df.columns.values)]
#Submit POST request to API
r = requests.post(url, data=payload) #pass valid API_key into this function

