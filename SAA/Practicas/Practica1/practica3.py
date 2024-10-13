import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVC
# Generar datos aleatorios para regresión
np.random.seed(0)
X_regression = np.random.uniform(0, 10, 1000)
#y_regression = 2 * X_regression + 3 + np.random.normal(0, 2, 1000)
#y_regression = 3 * X_regression + 3 + np.random.normal(0, 2, 1000)
y_regression = -2 * X_regression + 3 + np.random.normal(0, 2, 1000)
#y_regression = 2 * X_regression - 2 + np.random.normal(0, 2, 1000)
#y_regression = 2 * np.sin(0.5 * X_regression + (np.pi/4) + 3)


# Generar datos aleatorios para clasificación
np.random.seed(1)
X_classification_1 = np.random.normal(3, 1, 100)
y_classification_1 = np.random.normal(3, 1, 100)
X_classification_2 = np.random.normal(7, 1, 100)
y_classification_2 = np.random.normal(7, 1, 100)
# Crear modelos
regression_model = LinearRegression()
classification_model = SVC(kernel='linear')
# Entrenar modelos
X_regression = X_regression.reshape(-1, 1)
regression_model.fit(X_regression, y_regression)



X_classification = np.concatenate((np.stack((X_classification_1, y_classification_1), axis=1),
np.stack((X_classification_2, y_classification_2), axis=1)))
y_classification = np.concatenate([np.zeros(100), np.ones(100)])
classification_model.fit(X_classification, y_classification)
# Crear puntos para graficar las predicciones
x_values = np.linspace(0, 10, 100).reshape(-1, 1)
y_values_regression = regression_model.predict(x_values)
xx, yy = np.meshgrid(np.linspace(0, 10, 100), np.linspace(0, 10, 100))
xy = np.column_stack([xx.ravel(), yy.ravel()])
y_values_classification = classification_model.predict(xy).reshape(xx.shape)
# Graficar resultados de regresión y clasificación
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.scatter(X_regression, y_regression, label='Datos de regresión', color='blue')
plt.plot(x_values, y_values_regression, color='red', label='Regresión lineal')
plt.title('Ejemplo de Regresión')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()


plt.subplot(1, 2, 2)
plt.contourf(xx, yy, y_values_classification,
alpha=0.2, cmap='bwr')
plt.scatter(X_classification_1,
y_classification_1, label='Clase 1',
color='blue')
plt.scatter(X_classification_2,
y_classification_2, label='Clase 2',
color='orange')
plt.title('Ejemplo de Clasificación')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.tight_layout()
plt.show()