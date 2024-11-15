import pandas as pd
from pathlib import Path

from src.extract import ExtractorCSV, ExtractorExcel, ExtractorSQLite
from src.transform import TransformEnergy, TransformPib

pib_data = ExtractorExcel.extract(Path('data/pib.xlsx'), sheet_name='Full data')

# print(pib_data.head())

pib_data = TransformPib.transform(pib_data)

print(pib_data.head(n=50))