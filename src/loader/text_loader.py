from abc import ABC, abstractmethod
from entities.text_dataset import TextDataSet

class TextDataSetLoader(ABC):
    @abstractmethod
    def load(self) -> TextDataSet:
        """Load and return a TextDataSet object."""
        pass