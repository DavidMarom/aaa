from abc import ABC, abstractmethod
import json

class ReportBuilder(ABC):
    @abstractmethod
    def save(self):
        """Saves Report object into a file"""
        pass

class JsonReportBuilder(ReportBuilder):
    def __init__(self, filepath:str, report:dict):
        self.filepath = filepath
        self.file_format = 'json'
        self.report = report
        
    def save(self):
        with open(f'{self.filepath}.{self.file_format}', 'w') as f:
            json.dump(self.report, f, indent=4)