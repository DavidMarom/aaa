from ..entities.text_dataset import TextDataSet
from .loader import TextDataSetLoader
from typing import List
import pandas as pd

class CSVTextDataSetLoader(TextDataSetLoader):
    """
    This implementation uses pandas for efficient CSV parsing
    
    Parameters:
        filepath: Path to the CSV file
        chosen_features (Optional): List of chosen features names
    """
    def __init__(self, filepath: str, chosen_features: List[str] = None):
        self.filepath = filepath
        self.chosen_features = chosen_features

    def load(self, encoding='utf-8') -> TextDataSet:
        try:
            df = pd.read_csv(self.filepath, encoding=encoding)
        except UnicodeDecodeError as e:
            msg = f"Could not decode CSV file '{self.filepath}' with encoding {encoding}: {e.reason}"
            raise UnicodeDecodeError(
                encoding=e.encoding,
                object=e.object,
                start=e.start,
                end=e.end,
                reason=msg
            ) from e
        
        if self.chosen_features:
            df = df[self.chosen_features].copy()
        return TextDataSet(df)