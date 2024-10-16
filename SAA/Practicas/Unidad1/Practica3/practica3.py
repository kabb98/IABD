import numpy as np 
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVC

# -------------------- REGRESIÓN -------------------- #

# Generar datos aleatorios para regresión
np.random.seed(0)
X_regression = np.random.uniform(0, 10, 100)
y_regression = 2 * X_regression + 3 + np.random.normal(0, 2, 100)

# Crear y entrenar el modelo de regresión
regression_model = LinearRegression()
X_regression = X_regression.reshape(-1, 1)
regression_model.fit(X_regression, y_regression)

# Crear puntos para graficar las predicciones de la regresión
x_values = np.linspace(0, 10, 100).reshape(-1, 1)
y_values_regression = regression_model.predict(x_values)

# Graficar resultados de regresión en una figura separada
plt.figure(figsize=(6, 5))
plt.scatter(X_regression, y_regression, label='Datos de regresión', color='blue')
plt.plot(x_values, y_values_regression, color='red', label='Regresión lineal')
plt.title('Ejemplo de Regresión')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.tight_layout()
plt.show()

# -------------------- CLASIFICACIÓN -------------------- #

# Generar datos aleatorios para clasificación
np.random.seed(1)
X_classification_1 = np.random.normal(3, 1, 100)
y_classification_1 = np.random.normal(3, 1, 100)
X_classification_2 = np.random.normal(7, 1, 100)
y_classification_2 = np.random.normal(7, 1, 100)

# Preparar los datos de clasificación
X_classification = np.concatenate((
    np.stack((X_classification_1, y_classification_1), axis=1),
    np.stack((X_classification_2, y_classification_2), axis=1)
))
y_classification = np.concatenate([np.zeros(100), np.ones(100)])

# Crear y entrenar el modelo de clasificación
classification_model = SVC(kernel='linear')
classification_model.fit(X_classification, y_classification)

# Crear puntos para graficar las predicciones de la clasificación
xx, yy = np.meshgrid(np.linspace(0, 10, 100), np.linspace(0, 10, 100))
xy = np.column_stack([xx.ravel(), yy.ravel()])
y_values_classification = classification_model.predict(xy).reshape(xx.shape)

# Graficar resultados de clasificación en una figura separada
plt.figure(figsize=(6, 5))
plt.contourf(xx, yy, y_values_classification, alpha=0.2, cmap='bwr')
plt.scatter(X_classification_1, y_classification_1, label='Clase 1', color='blue')
plt.scatter(X_classification_2, y_classification_2, label='Clase 2', color='orange')
plt.title('Ejemplo de Clasificación')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.tight_layout()
plt.show()
