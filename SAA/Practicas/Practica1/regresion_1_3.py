import numpy as np 
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from mpl_toolkits.mplot3d import Axes3D

def grafica_5_funciones(): 
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



def grafica_5_funciones_3d():
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

    # -------------------- GRAFICAR LAS FUNCIONES EN 3D -------------------- #
    fig = plt.figure(figsize=(18, 12))

    for i, (y_regression, title) in enumerate(functions, 1):
        # Entrenar el modelo de regresión para cada función
        regression_model.fit(X_regression, y_regression)

        # Predecir valores de Y
        y_values_regression = regression_model.predict(x_values)

        # Subfigura en 3D correspondiente
        ax = fig.add_subplot(3, 2, i, projection='3d')
        
        # Graficar los puntos de datos y la línea de regresión
        ax.scatter(X_regression, y_regression, np.zeros_like(X_regression), label='Datos de regresión', color='blue')
        ax.plot(x_values, y_values_regression, np.zeros_like(x_values), color='red', label='Regresión lineal')

        # Añadir títulos y etiquetas
        ax.set_title(title)
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z (0)')
        ax.legend()

    plt.tight_layout()
    plt.show()


def main():
    grafica_5_funciones()
    grafica_5_funciones_3d()
    
if __name__ == '__main__':
    main()