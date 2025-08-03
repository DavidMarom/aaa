import pandas as pd
from cleaner import clean_tweet_data

df = pd.read_csv('./tweets_dataset.csv')
clean_df = clean_tweet_data(df)

# print(clean_df.head())

# clean_df.to_csv('../results/clean_tweets.csv', index=False)