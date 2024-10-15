import numpy as np 
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# -------------------- CONFIGURACIÓN INICIAL -------------------- #

# Generar datos aleatorios para regresión (función original)
np.random.seed(0)
X_regression = np.random.uniform(0, 10, 100)
X_regression = X_regression.reshape(-1, 1)

# Crear modelo de regresión
regression_model = LinearRegression()

# Crear puntos para graficar las predicciones de la regresión
x_values = np.linspace(0, 10, 100).reshape(-1, 1)

# -------------------- FUNCIONES A PROBAR -------------------- #
functions = [
    (2 * X_regression + 3 + np.random.normal(0, 2, 100).reshape(-1, 1), 'Función original: 2X + 3'),
    (3 * X_regression + 3 + np.random.normal(0, 2, 100).reshape(-1, 1), '3X + 3'),
    (-2 * X_regression + 3 + np.random.normal(0, 2, 100).reshape(-1, 1), '-2X + 3'),
    (2 * X_regression - 2 + np.random.normal(0, 2, 100).reshape(-1, 1), '2X - 2'),
    (2 * np.sin(0.5 * X_regression + (np.pi / 4)) + 3, '2sin(0.5X + π/4) + 3')
]

# -------------------- GRAFICAR LAS FUNCIONES -------------------- #
plt.figure(figsize=(15, 10))

for i, (y_regression, title) in enumerate(functions, 1):
    # Entrenar el modelo de regresión para cada función
    regression_model.fit(X_regression, y_regression)

    # Predecir valores de Y
    y_values_regression = regression_model.predict(x_values)

    # Subfigura correspondiente
    plt.subplot(3, 2, i)
    plt.scatter(X_regression, y_regression, label='Datos de regresión', color='blue')
    plt.plot(x_values, y_values_regression, color='red', label='Regresión lineal')
    plt.title(title)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()

plt.tight_layout()
plt.show()
