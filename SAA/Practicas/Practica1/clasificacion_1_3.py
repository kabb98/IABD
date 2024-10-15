import numpy as np 
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVC
from mpl_toolkits.mplot3d import Axes3D


def grafica_3_clases():
    # -------------------- CLASIFICACIÓN -------------------- #

    # Generar datos aleatorios para clasificación con tres clases
    np.random.seed(1)
    X_classification_1 = np.random.normal(3, 1, 100)
    y_classification_1 = np.random.normal(3, 1, 100)

    X_classification_2 = np.random.normal(7, 1, 100)
    y_classification_2 = np.random.normal(7, 1, 100)

    # Nueva clase (Clase 3)
    X_classification_3 = np.random.normal(5, 1, 100)
    y_classification_3 = np.random.normal(8, 1, 100)

    # Preparar los datos de clasificación
    X_classification = np.concatenate((
        np.stack((X_classification_1, y_classification_1), axis=1),
        np.stack((X_classification_2, y_classification_2), axis=1),
        np.stack((X_classification_3, y_classification_3), axis=1)  # Añadir la tercera clase
    ))
    y_classification = np.concatenate([np.zeros(100), np.ones(100), np.full(100, 2)])  # Añadir etiquetas para clase 3

    # Crear y entrenar el modelo de clasificación
    classification_model = SVC(kernel='linear', decision_function_shape='ovr')  # 'ovr' para One-vs-Rest
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
    plt.scatter(X_classification_3, y_classification_3, label='Clase 3', color='green')  # Graficar tercera clase

    plt.title('Ejemplo de Clasificación con 3 Clases')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.tight_layout()
    plt.show()

def grafica_3_clases_3d():
    # -------------------- CLASIFICACIÓN -------------------- #

    # Generar datos aleatorios para clasificación con tres clases
    np.random.seed(1)
    X_classification_1 = np.random.normal(3, 1, 100)
    y_classification_1 = np.random.normal(3, 1, 100)

    X_classification_2 = np.random.normal(7, 1, 100)
    y_classification_2 = np.random.normal(7, 1, 100)

    # Nueva clase (Clase 3)
    X_classification_3 = np.random.normal(5, 1, 100)
    y_classification_3 = np.random.normal(8, 1, 100)

    # Preparar los datos de clasificación
    X_classification = np.concatenate((
        np.stack((X_classification_1, y_classification_1), axis=1),
        np.stack((X_classification_2, y_classification_2), axis=1),
        np.stack((X_classification_3, y_classification_3), axis=1)  # Añadir la tercera clase
    ))
    y_classification = np.concatenate([np.zeros(100), np.ones(100), np.full(100, 2)])  # Añadir etiquetas para clase 3

    # Crear y entrenar el modelo de clasificación
    classification_model = SVC(kernel='linear', decision_function_shape='ovr')  # 'ovr' para One-vs-Rest
    classification_model.fit(X_classification, y_classification)

    # Crear puntos para graficar las predicciones de la clasificación
    xx, yy = np.meshgrid(np.linspace(0, 10, 100), np.linspace(0, 10, 100))
    xy = np.column_stack([xx.ravel(), yy.ravel()])
    y_values_classification = classification_model.predict(xy).reshape(xx.shape)

    # Graficar resultados de clasificación en una figura separada
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')

    # Graficar los puntos de las tres clases
    ax.scatter(X_classification_1, y_classification_1, np.zeros_like(X_classification_1), label='Clase 1', color='blue')
    ax.scatter(X_classification_2, y_classification_2, np.zeros_like(X_classification_2), label='Clase 2', color='orange')
    ax.scatter(X_classification_3, y_classification_3, np.zeros_like(X_classification_3), label='Clase 3', color='green')

    # Graficar el plano de decisión
    ax.plot_surface(xx, yy, y_values_classification, alpha=0.3, cmap='bwr', zorder=0)  # Suavizar el plano de decisión

    # Añadir títulos y etiquetas
    ax.set_title('Ejemplo de Clasificación en 3D con 3 Clases')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Clase (Z)')
    ax.legend()

    plt.tight_layout()
    plt.show()

def grafica_4_clases():
    # Generar datos aleatorios para clasificación con cuatro clases
    np.random.seed(1)
    X_classification_1 = np.random.normal(2, 1, 100)
    y_classification_1 = np.random.normal(2, 1, 100)

    X_classification_2 = np.random.normal(6, 1, 100)
    y_classification_2 = np.random.normal(6, 1, 100)

    X_classification_3 = np.random.normal(4, 1, 100)
    y_classification_3 = np.random.normal(8, 1, 100)

    # Nueva clase (Clase 4)
    X_classification_4 = np.random.normal(8, 1, 100)
    y_classification_4 = np.random.normal(2, 1, 100)

    # Preparar los datos de clasificación
    X_classification = np.concatenate((
        np.stack((X_classification_1, y_classification_1), axis=1),
        np.stack((X_classification_2, y_classification_2), axis=1),
        np.stack((X_classification_3, y_classification_3), axis=1),
        np.stack((X_classification_4, y_classification_4), axis=1)  # Añadir la cuarta clase
    ))
    y_classification = np.concatenate([
        np.zeros(100), 
        np.ones(100), 
        np.full(100, 2), 
        np.full(100, 3)  # Añadir etiquetas para clase 4
    ])

    # Crear y entrenar el modelo de clasificación
    classification_model = SVC(kernel='linear', decision_function_shape='ovr')
    classification_model.fit(X_classification, y_classification)

    # Crear puntos para graficar las predicciones de la clasificación
    xx, yy = np.meshgrid(np.linspace(0, 10, 100), np.linspace(0, 10, 100))
    xy = np.column_stack([xx.ravel(), yy.ravel()])
    y_values_classification = classification_model.predict(xy).reshape(xx.shape)

    # Graficar resultados de clasificación en 2D
    plt.figure(figsize=(8, 6))
    plt.contourf(xx, yy, y_values_classification, alpha=0.2, cmap='bwr')
    plt.scatter(X_classification_1, y_classification_1, label='Clase 1', color='blue')
    plt.scatter(X_classification_2, y_classification_2, label='Clase 2', color='orange')
    plt.scatter(X_classification_3, y_classification_3, label='Clase 3', color='green')
    plt.scatter(X_classification_4, y_classification_4, label='Clase 4', color='purple')  # Graficar cuarta clase
    plt.title('Ejemplo de Clasificación en 2D con 4 Clases')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.tight_layout()
    plt.show()

def grafica_4_clases_3d():
    # Generar datos aleatorios para clasificación con cuatro clases
    np.random.seed(1)
    X_classification_1 = np.random.normal(2, 1, 100)
    y_classification_1 = np.random.normal(2, 1, 100)

    X_classification_2 = np.random.normal(6, 1, 100)
    y_classification_2 = np.random.normal(6, 1, 100)

    X_classification_3 = np.random.normal(4, 1, 100)
    y_classification_3 = np.random.normal(8, 1, 100)

    # Nueva clase (Clase 4)
    X_classification_4 = np.random.normal(8, 1, 100)
    y_classification_4 = np.random.normal(2, 1, 100)

    # Preparar los datos de clasificación
    X_classification = np.concatenate((
        np.stack((X_classification_1, y_classification_1), axis=1),
        np.stack((X_classification_2, y_classification_2), axis=1),
        np.stack((X_classification_3, y_classification_3), axis=1),
        np.stack((X_classification_4, y_classification_4), axis=1)  # Añadir la cuarta clase
    ))
    y_classification = np.concatenate([
        np.zeros(100), 
        np.ones(100), 
        np.full(100, 2), 
        np.full(100, 3)  # Añadir etiquetas para clase 4
    ])

    # Crear y entrenar el modelo de clasificación
    classification_model = SVC(kernel='linear', decision_function_shape='ovr')
    classification_model.fit(X_classification, y_classification)

    # Crear puntos para graficar las predicciones de la clasificación
    xx, yy = np.meshgrid(np.linspace(0, 10, 100), np.linspace(0, 10, 100))
    xy = np.column_stack([xx.ravel(), yy.ravel()])
    y_values_classification = classification_model.predict(xy).reshape(xx.shape)

    # Graficar resultados de clasificación en 3D
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')

    # Graficar los puntos de las cuatro clases
    ax.scatter(X_classification_1, y_classification_1, np.zeros_like(X_classification_1), label='Clase 1', color='blue')
    ax.scatter(X_classification_2, y_classification_2, np.zeros_like(X_classification_2), label='Clase 2', color='orange')
    ax.scatter(X_classification_3, y_classification_3, np.zeros_like(X_classification_3), label='Clase 3', color='green')
    ax.scatter(X_classification_4, y_classification_4, np.zeros_like(X_classification_4), label='Clase 4', color='purple')  # Graficar cuarta clase

    # Graficar el plano de decisión
    ax.plot_surface(xx, yy, y_values_classification, alpha=0.3, cmap='bwr', zorder=0)

    # Añadir títulos y etiquetas
    ax.set_title('Ejemplo de Clasificación en 3D con 4 Clases')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Clase (Z)')
    ax.legend()

    plt.tight_layout()
    plt.show()


def main():
    grafica_3_clases()
    grafica_3_clases_3d()
    grafica_4_clases()
    grafica_4_clases_3d()

if __name__ == '__main__':
    main()