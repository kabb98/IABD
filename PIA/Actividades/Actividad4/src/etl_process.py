# Instancio la clase Energy -> Lee datos, hacemos los transforms

import pandas as pd
import sys
from pathlib import Path
import sqlite3
import parsers, extract, transform

# Añadir el directorio raíz del proyecto al sys.path
sys.path.append(str(Path(__file__).resolve().parent.parent))

def main():
    # Paths
    paths = parsers.Parser.parse(Path('./config.yml'))

    # Comprobar que exista la salida
    Path('./output').mkdir(parents=True, exist_ok=True)

    data_files_paths = paths['files']
    data_root_path = paths['paths']['data_dir']
    database_file = paths['paths']['database_file']

    energy_path = Path(data_root_path) / data_files_paths['energy']
    pib_path = Path(data_root_path) / data_files_paths['pib']
    emissions_path = Path(data_root_path) / data_files_paths['emissions']

    # Extract data
    energy_df = extract.ExtractorCSV.extract(energy_path, rows=4)
    pib_df = extract.ExtractorExcel.extract(pib_path, sheet_name='Full data')
    emissions_df = extract.ExtractorCSV.extract(emissions_path)

    # Transform data
    energy_df = transform.TransformEnergy.transform(energy_df)
    pib_df = transform.TransformPib.transform(pib_df)
    emissions_df = transform.TransformEmissions.transform(emissions_df)

    # Merge data
    merged_df = pd.merge(energy_df, pib_df, on='Country', how='inner')

    # Merge data
    merged_df = pd.merge(merged_df, emissions_df, on='Country', how='inner')

    # Guardar en SQLite
    with sqlite3.connect(Path(database_file)) as dbcon:
        merged_df.to_sql(name='etl', con=dbcon, if_exists='replace', index=False)

if __name__ == '__main__':
    main()