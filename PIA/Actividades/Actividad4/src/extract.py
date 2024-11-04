from abc import ABC, abstractmethod

class Extractor(ABC):
    @abstractmethod
    def extract(self, data):
        pass


class ExtractorCSV(Extractor):
    def extract(self, data):
        return data.split(',')

class ExtractorExcel(Extractor):
    def extract(self, data):
        return data.split(',')

class ExtractorSQLite(Extractor):
    def extract(self, data):
        return data.split(',')