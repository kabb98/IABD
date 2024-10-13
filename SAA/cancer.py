from sklearn.datasets import load_breast_cancer
import pandas as pd
import matplotlib.pyplot as plt

# Cargar el conjunto de datos de cáncer de mama
data = load_breast_cancer()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = data.target

# Análisis exploratorio de datos
# Por ejemplo, podrías calcular estadísticas descriptivas de las características
# Esto te dará una idea de la distribución y variación de los datos
descriptive_statistics = X.describe()
print(descriptive_statistics)

# También podrías visualizar la distribución de algunas características para las dos clases
# Aquí hay un ejemplo con dos características
plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.hist(X.loc[y == 0, 'mean radius'], bins=20, alpha=0.5, label='Clase 0', color='blue')
plt.hist(X.loc[y == 1, 'mean radius'], bins=20, alpha=0.5, label='Clase 1', color='red')
plt.xlabel('Mean Radius')
plt.ylabel('Frecuencia')
plt.legend()

plt.subplot(1, 2, 2)
plt.scatter(X.loc[y == 0, 'mean texture'], X.loc[y == 0, 'mean compactness'], label='Clase 0', color='blue')
plt.scatter(X.loc[y == 1, 'mean texture'], X.loc[y == 1, 'mean compactness'], label='Clase 1', color='red')
plt.xlabel('Mean Texture')
plt.ylabel('Mean Compactness')
plt.legend()

plt.tight_layout()
plt.show()
