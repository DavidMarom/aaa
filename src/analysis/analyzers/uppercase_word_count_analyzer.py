from analysis.analyzer import Analyzer
from entities.text_dataset import TextDataSet
from analysis.analyzers.constants import DEFAULT_CATEGORY

class UppercaseWordCountAnalyzer(Analyzer):
    def __init__(self, dataset: TextDataSet, text_feature:str, 
                 category_feature:str=None, default_category:str=DEFAULT_CATEGORY):
        self.dataset = dataset
        self.text_feature = text_feature
        self.category_feature = category_feature
        self.default_category = default_category

    def analyze(self) -> dict:
        def count_upper(text):
            return sum(1 for w in text.split() if w.isupper())
        df = self.dataset.get_dataframe()
        df['upper_count'] = df[self.text_feature].apply(count_upper)
        results = {}
        if self.category_feature:
            results = df.groupby(self.category_feature, dropna=False)['upper_count'].sum().to_dict()
        results[self.default_category] = int(df['upper_count'].sum())
        return results