from analysis.analyzer import Analyzer

class NamedAnalyzer:
    def __init__(self, name: str, analyzer: Analyzer):
        self.name = name
        self.analyzer = analyzer

    def analyze(self) -> dict:
        return self.analyzer.analyze()