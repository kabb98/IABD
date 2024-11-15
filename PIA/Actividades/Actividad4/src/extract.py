from abc import ABC, abstractmethod
from pathlib import Path
import pandas as pd


class Extractor(ABC):
    @abstractmethod
    def extract(self, data):
        pass


class ExtractorCSV(Extractor):
    @staticmethod
    def extract(path: Path, rows = 0):
        """
        Returns a pandas DataFrame from a CSV file
        """
        return pd.read_csv(path, skiprows=rows)

class ExtractorExcel(Extractor):
    @staticmethod
    def extract(path: Path, sheet_name: str):
        """
        Returns a pandas DataFrame from a Excel file
        """
        return pd.read_excel(path, sheet_name=sheet_name)

class ExtractorSQLite(Extractor):
    @staticmethod
    def extract(path: Path):
        """
        Returns a pandas DataFrame from a SQLite file
        """
        import sqlite3
        from pandas import read_sql_query, read_sql_table

        with sqlite3.connect(path) as dbcon:
            tables = list(read_sql_query("SELECT name FROM sqlite_master WHERE type='table';", dbcon)['name'])
            out = {tbl : read_sql_query(f"SELECT * from {tbl}", dbcon) for tbl in tables}

        return out

# Depnde del formato a guardar o leer -> ESTO ES LEER