from typing import List,Dict
from analysis.named_analyzer import NamedAnalyzer

class CompositeAnalyzer:
    def __init__(self, analyzers: List[NamedAnalyzer]):
        self.analyzers = analyzers

    def run_all(self) -> Dict[str, dict]:
        return {a.name: a.analyze() for a in self.analyzers}