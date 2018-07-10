import pandas as pd

df = pd.read_excel('twitter_followers.xlsx')


for i, row in df['Player'].iteritems():
    index = row.find("\\")
    newrow = row[: index]

    df.at[i,'Player'] = newrow

df.to_csv("twitter_followers.csv")
