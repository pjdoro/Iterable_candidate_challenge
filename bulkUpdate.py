import pandas as pd
import requests
# indicate the user row numbers in the csv as a list of comma seperated integers to post updates
users = [0,2]
# Specify a valid API valid key
api_key = '123' #Here is where you would define a valid API_key
# read csv into dataframe
data = 'Tomato_data.csv'
df = pd.read_csv(data)
# Break if number of users exceeds 50
if len(users) > 50:
    raise Exception('You can only Include up to 50 users in a single bulk call. Reduce the number of users selected')
# Create payload for POST request
payload = {}
for x in users:
    row =df.iloc[x]
    payload[str(df.loc[x,'email'])] = [str(x)+ ' : ' +str(row[x]) for x in list(df.columns.values)]
#Submit POST request to API
r = requests.post("https://api.iterable.com/api/users_bulkUpdateUser", data=payload) #pass valid API_key into this function

