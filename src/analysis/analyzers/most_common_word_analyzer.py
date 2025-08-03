from collections import Counter
from analysis.analyzer import Analyzer
from entities.text_dataset import TextDataSet
from typing import Dict,Tuple
from analysis.analyzers.constants import DEFAULT_CATEGORY

class MostCommonWordsAnalyzer(Analyzer):
    def __init__(self, dataset: TextDataSet, text_feature:str, 
                 top_n: int, default_category=DEFAULT_CATEGORY):
        self.dataset = dataset
        self.text_feature = text_feature
        self.top_n = top_n
        self.default_category = default_category

    def analyze(self) -> Dict[str,Tuple[str,int]]:
        df = self.dataset.get_dataframe()
        results = {}
        words = df[self.text_feature].str.lower().str.split().explode()
        results[self.default_category] = Counter(words).most_common(self.top_n)
        return results
