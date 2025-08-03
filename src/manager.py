import pandas as pd

from cleaner import clean_tweet_data
from loader.csv_text_loader import CSVTextDataSetLoader

TARGET_CATEGORY_FEATURE = "Biased"
TARGET_TEXT_FEATURE = "Text"
NUM_COMMON_WORDS = 10
NUM_LONGEST_TWEETS = 3
DEFAULT_CATEGORY_NAME = 'total'
# Load dataset
loader = CSVTextDataSetLoader(filepath='data/tweets_dataset.csv',
                              chosen_features=[TARGET_TEXT_FEATURE,TARGET_CATEGORY_FEATURE])
dataset = loader.load()

# Question 2
clean_df = clean_tweet_data(dataset.get_dataframe())
clean_df.to_csv('results/tweets_dataset_cleaned.csv', index=False)


