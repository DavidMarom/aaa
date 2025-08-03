import pandas as pd
from cleaner import clean_tweet_data
from dataAnalyzer import dataAnalysis
from collections import defaultdict as DefaultDict
import json


class Reporter:
    def __init__(self, output_path):
        self.df = dataAnalysis()
        self.report = DefaultDict()


    def generate_report(self):
        for cat in self.df['category'].unique(): # either antisemetic or non-antisemitic, neutral/unspecified or total
            cat_df = self.df[self.df['category'] == cat]
            for param in cat_df['parameter'].unique(): # parameters like 'total_tweets', 3 longest tweets, total tweet count.
                value = cat_df[cat_df['parameter'] == param]['value'].values[0]
                self.report[cat][param] = value

    def save_report(self, filename='results'):
        with open(f'./{filename}.json', 'w') as f:
            json.dump(self.report, f, indent=4)

        print(f"Custom JSON data has been stored in '{filename}.json'")