import pandas as pd
from cleaner import clean_tweet_data

# Question 2
df = pd.read_csv('../data/tweets_dataset.csv', encoding='utf-8', low_memory=False)
clean_df = clean_tweet_data(df)
clean_df.to_csv('../results/tweets_dataset_cleaned.csv', index=False)
