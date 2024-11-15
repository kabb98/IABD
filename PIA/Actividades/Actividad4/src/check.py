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

    database_file = paths['paths']['database_file']
    merged_file = paths['paths']['merged_file']

    # Leer el fichero SQLite
    
    try:
        with sqlite3.connect(Path(database_file)) as dbcon:
            df = pd.read_sql_query("SELECT * from etl", dbcon)
    except:
        print("Error al leer el fichero SQLite")
        sys.exit(1)

    # Guardar el fichero en formato CSV
    df.to_csv(Path(merged_file), index=False)

if __name__ == '__main__':
    main()
