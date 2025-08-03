from analysis.analyzer import Analyzer
from entities.text_dataset import TextDataSet
from analysis.analyzers.constants import DEFAULT_CATEGORY

class AverageWordsLengthAnalyzer(Analyzer):
    def __init__(self, dataset: TextDataSet, text_feature: str, 
                 category_feature: str = None, default_category=DEFAULT_CATEGORY,
                 dropna:bool=False):
        self.dataset = dataset
        self.category_feature = category_feature
        self.text_feature = text_feature
        self.default_category = default_category
        self.dropna=dropna

    def analyze(self) -> dict:
        df = self.dataset.get_dataframe()
        df['word_count'] = df[self.text_feature].str.split().str.len()
        result = {}
        if self.category_feature:
            result = df.groupby(self.category_feature, dropna=self.dropna)['word_count'].mean().to_dict()
        result[self.default_category] = float(df['word_count'].mean())
        return result