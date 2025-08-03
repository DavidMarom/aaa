from analysis.analyzer import Analyzer
from entities.text_dataset import TextDataSet
from analysis.analyzers.constants import DEFAULT_CATEGORY

class RecordsCountAnalyzer(Analyzer):
    def __init__(self, dataset: TextDataSet, 
                 category_feature:str=None, default_category=DEFAULT_CATEGORY,
                 dropna:bool=None):
        self.dataset = dataset
        self.category_feature = category_feature
        self.default_category = default_category
        self.dropna=dropna

    def analyze(self) -> dict:
        df = self.dataset.get_dataframe()
        result = {}
        if self.category_feature:
            result = df[self.category_feature].value_counts(dropna=self.dropna).to_dict()
        result[self.default_category] = int(df.value_counts().sum())
        return result