from analysis.analyzer import Analyzer
from entities.text_dataset import TextDataSet
from analysis.analyzers.constants import DEFAULT_CATEGORY

class TopLongestTextRecordsAnalyzer(Analyzer):
    def __init__(self, dataset: TextDataSet, text_feature:str, top_n: int, 
                 category_feature:str=None, default_category:str=DEFAULT_CATEGORY):
        self.dataset = dataset
        self.text_feature = text_feature
        self.top_n = top_n
        self.category_feature = category_feature
        self.default_category = default_category

    def analyze(self) -> dict:
        df = self.dataset.get_dataframe()
        df['char_count'] = df[self.text_feature].str.len()
        result = {}
        result[self.default_category] = df.sort_values('char_count', ascending=False).head(self.top_n)[self.text_feature].tolist()
        if self.category_feature:
            for cat, group in df.groupby(self.category_feature, dropna=False):
                result[cat] = group.sort_values('char_count', ascending=False).head(self.top_n)[self.text_feature].tolist()
        return result
