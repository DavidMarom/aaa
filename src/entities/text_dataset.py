import pandas as pd

class TextDataSet:
    def __init__(self, data: pd.DataFrame):
        self.data = data

    def get_dataframe(self) -> pd.DataFrame:
        return self.data.copy()