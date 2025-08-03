import pandas as pd

from cleaner import clean_tweet_data
from loader.csv_text_loader import CSVTextDataSetLoader
from analysis.composite_analyzer import CompositeAnalyzer
from analysis.named_analyzer import NamedAnalyzer
from analysis.analyzers.records_count_analyzer import RecordsCountAnalyzer
from analysis.analyzers.average_words_length_analyzer import AverageWordsLengthAnalyzer
from analysis.analyzers.most_common_word_analyzer import MostCommonWordsAnalyzer
from analysis.analyzers.top_longest_text_records_analyzer import TopLongestTextRecordsAnalyzer
from analysis.analyzers.uppercase_word_count_analyzer import UppercaseWordCountAnalyzer
from results_transformer import ResultsTransformer
from report_builder import ReportBuilder,JsonReportBuilder

TARGET_CATEGORY_FEATURE = "Biased"
TARGET_TEXT_FEATURE = "Text"
NUM_COMMON_WORDS = 10
NUM_LONGEST_TWEETS = 3
DEFAULT_CATEGORY_NAME = 'total'


# Load dataset
loader = CSVTextDataSetLoader(filepath='data/tweets_dataset.csv',
                              chosen_features=[TARGET_TEXT_FEATURE,TARGET_CATEGORY_FEATURE])
dataset = loader.load()


# Question 1 - Data Analysis
analyzers = [
    NamedAnalyzer(
        "total_tweets", 
        RecordsCountAnalyzer(dataset, 
                             category_feature=TARGET_CATEGORY_FEATURE, 
                             default_category=DEFAULT_CATEGORY_NAME)
        ),
    NamedAnalyzer(
        "average_length", 
        AverageWordsLengthAnalyzer(dataset, 
                                   text_feature=TARGET_TEXT_FEATURE, 
                                   category_feature=TARGET_CATEGORY_FEATURE,
                                   default_category=DEFAULT_CATEGORY_NAME)
        ),
    NamedAnalyzer(
        "common_words", 
        MostCommonWordsAnalyzer(dataset, 
                                text_feature=TARGET_TEXT_FEATURE, 
                                top_n=NUM_COMMON_WORDS,
                                default_category=DEFAULT_CATEGORY_NAME)
        ),
    NamedAnalyzer(
        f"longest_{NUM_LONGEST_TWEETS}_tweets", 
        TopLongestTextRecordsAnalyzer(dataset, 
                                      text_feature=TARGET_TEXT_FEATURE, 
                                      top_n=NUM_LONGEST_TWEETS, 
                                      category_feature=TARGET_CATEGORY_FEATURE,
                                      default_category=DEFAULT_CATEGORY_NAME)
        ),
    NamedAnalyzer(
        "uppercase_words", 
        UppercaseWordCountAnalyzer(dataset, 
                                   text_feature=TARGET_TEXT_FEATURE, 
                                   category_feature=TARGET_CATEGORY_FEATURE,
                                   default_category=DEFAULT_CATEGORY_NAME)
        )
]

composite_analyzer = CompositeAnalyzer(analyzers)
results = composite_analyzer.run_all()

# Question 2 - Clean Data
clean_df = clean_tweet_data(dataset.get_dataframe())
clean_df.to_csv('results/tweets_dataset_cleaned.csv', index=False)


# Question 3

report_builder = ResultsTransformer(
    category_mapping={0: 'non_antisemitic', 1: 'antisemitic'},
    tuple_extract_keys=['common_words'],
    tuple_extract_index = 0,
    exclude_keys={f"longest_{NUM_LONGEST_TWEETS}_tweets": [DEFAULT_CATEGORY_NAME]}
)
final_results = report_builder.transform(results)

report_builder:ReportBuilder = JsonReportBuilder(filepath="results/results", report=final_results)

report_builder.save()