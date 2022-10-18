import pandas as pd
import json

df = pd.read_csv("top-users.csv")


users = {}

for col in df.columns:
    for user in df[col]:
        users[user] = col

with open("users.json", "w") as outfile:
    json.dump(users, outfile)
