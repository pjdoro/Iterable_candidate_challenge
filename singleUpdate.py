import pandas as pd
import requests
# indicate the row number in the csv to post update
rec = 0
# Specify target API and valid key
api_key = '123' #This is a placeholder
# Read csv into dataframe
data = 'Tomato_data.csv'
df = pd.read_csv(data)
# Create payload for POST request
payload =[(x,df.iloc[rec][x]) for x in list(df.columns.values)]
#Submit POST request to API
r = requests.post("https://api.iterable.com/api/users/update", data=payload) #pass valid API_key into this function

