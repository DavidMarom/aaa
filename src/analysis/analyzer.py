from abc import ABC, abstractmethod

class Analyzer(ABC):
    @abstractmethod
    def analyze(self) -> dict:
        """analyze dataset given and return dict object"""
        pass