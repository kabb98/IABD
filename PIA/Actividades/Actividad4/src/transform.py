# Asociadas a unos daots y su estructura

import pandas as pd
from pathlib import Path


class TransformEnergy:
    @staticmethod
    def transform(data: pd.DataFrame):
        # Borrar las columnas que no tienen datos importantes
        data.drop(columns=["Unnamed: 68", "Indicator Name", "Indicator Code", "Country Code"], inplace=True)
        
        df = data.rename(columns={"Country Name": "Country"})

        # Selecciona las columnas de los años 1990 a 2014
        df = df[[ "Country"] + [str(i) for i in range(1990, 2015)]]

        # Average energy
        years = [str(year) for year in range(1990, 2015)]

        df["average_electricity"] = df[years].mean(axis=1)

        # Eliminar las columnas de los años
        df = df.drop(columns=years)
        return df
    

class TransformPib:
    @staticmethod
    def transform(data: pd.DataFrame):
        # Eliminar las columnas 'region' y 'pop'
        df = data.drop(columns=['region', 'countrycode'])

        # Pillar años entre 1990 y 2014
        df = df[(df['year'] >= 1990) & (df['year'] <= 2014)].reset_index(drop=True)

        # Añadimos la columna 'pib_total'
        df['pib_total'] = df['gdppc'] * df['pop']

        # Media del pib
        df['mean_pib'] = df.groupby('country')['pib_total'].transform('mean')

        # Media del pib per capita
        df['mean_pib_per_capita'] = df.groupby('country')['gdppc'].transform('mean')

        # Eliminamos las columnas que no necesitamos
        df = df.drop(columns=['year', 'gdppc', 'pop', 'pib_total'])

        # Ponemos el nombre de los paises igual que en el los otros dataframes
        df.rename(columns={'country': 'Country'}, inplace=True)
        
        return df.groupby('Country').first().reset_index()

class TransformEmissions:
    @staticmethod
    def transform(data: pd.DataFrame):
        #  Quitamos los datos que no usamos
        df = data.drop(columns=["category"])

        # Renombramos el campo "country_or_area" a "country"
        df.rename(columns={"country_or_area": "Country"}, inplace=True)
        
        # Filtramos por los años al igual que en el primer caso
        df = df[(df["year"] >= 1990) & (df["year"] <= 2014)]

        # Calculamos el promedio por pais
        df = df.groupby("Country")["value"].mean().reset_index()

        # Renombrar la columna de emisiones promedio
        df.rename(columns={"value": "average_emissions"}, inplace=True)
        
        return df