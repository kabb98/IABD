# Asociadas a unos daots y su estructura

import pandas as pd
from pathlib import Path


class TransformEnergy:
    @staticmethod
    def transform(data: pd.DataFrame):
        # Transpose temporal data
        data = data.T

        
        return data
    

class TransformPib:
    @staticmethod
    def transform(data: pd.DataFrame):
        # Eliminar las columnas 'region' y 'pop'
        df = data.drop(columns=['region'])

        # Pillar años entre 1990 y 2014
        df = df[(df['year'] >= 1990) & (df['year'] <= 2014)].reset_index(drop=True)

        # Añadimos la columna 'pib_total'
        df['pib_total'] = df['gdppc'] * df['pop']

        # Media del pib
        df['mean_pib'] = df.groupby('country')['pib_total'].transform('mean')

        # Media del pib per capita
        df['mean_pib_per_capita'] = df.groupby('country')['gdppc'].transform('mean')

        df = df.drop(columns=['year', 'gdppc', 'pop', 'pib_total'])
        
        return df.groupby('country').first().reset_index()