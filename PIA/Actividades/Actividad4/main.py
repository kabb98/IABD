import pandas as pd
from pathlib import Path

from src.extract import ExtractorCSV, ExtractorExcel, ExtractorSQLite
from src.transform import TransformEnergy, TransformPib

emissions_data = ExtractorCSV.extract(Path('./data/emissions.csv'))

df = TransformEnergy.transform(emissions_data)
df.head()