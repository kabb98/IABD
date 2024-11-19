import matplotlib.pyplot as plt
import pandas as pd
from sklearn import datasets
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

# Cargar el conjunto de datos de iris
iris = datasets.load_iris()
X = iris.data
y = iris.target
target_names = iris.target_names

# Aplicar LDA para reducción de dimensionalidad
lda = LinearDiscriminantAnalysis(n_components=2)
X_r = lda.fit(X, y).transform(X)

# Crear un DataFrame para mostrar los datos antes y después de LDA
data_before_lda = pd.DataFrame(X, columns=iris.feature_names)
data_after_lda = pd.DataFrame(X_r, columns=['LDA Component 1', 'LDA Component 2'])

# Mostrar la tabla con los datos antes y después de LDA
print("Datos antes de LDA:")
print(data_before_lda.head(4))  # Muestra las primeras 4 filas

print("\nDatos después de LDA:")
print(data_after_lda.head(4))  # Muestra las primeras 4 filas
