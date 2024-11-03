
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Perceptron
from sklearn.metrics import accuracy_score

def solo_entrenamiento():

    #Cargar el dataset Iris
    iris = datasets.load_iris()
    x = iris.data
    y = iris.target
    # Dividir el dataset en conjuntos de entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

    # Escalar las características para un mejor rendimiento
    sc = StandardScaler()
    sc.fit(X_train)

    X_train_std = sc.transform(X_train)
    X_test_std= sc.transform(X_test)
    # Crear un perceptrón y entrenarlo
    ppn = Perceptron (max_iter=100, eta0= 0.1, random_state=42)
    ppn.fit(X_train_std, y_train)

    # Predecir con el conjunto de prueba
    y_pred = ppn.predict(X_test_std)

    # Calcular la precisión del perceptrón
    accuracy = accuracy_score (y_test, y_pred)
    print (f'Precisión: {accuracy}')

    # Pesos finales
    print (f'Pesos finales: {ppn.coef_}')

def prueba_con_datos_nuestros():

    from sklearn.preprocessing import StandardScaler
    from sklearn.linear_model import Perceptron
    from sklearn.datasets import load_iris
    import numpy as np
    #Función para ingresar los valores de las características de la flor
    def ingresar_valores():
        sepal_length =  float(input("Introduce la longitud del sépalo (cm): "))
        sepal_width = float(input("Introduce el ancho del sépalo (cm): "))
        petal_length = float(input("Introduce la longitud del pétalo (cm): "))
        petal_width = float(input("Introduce el ancho del pétalo (cm): "))
    
        return [sepal_length, sepal_width, petal_length, petal_width]
    
    #Cargar el dataset Iris
    iris = load_iris()
    x = iris.data
    y = iris.target
    
    # Dividir el dataset en conjuntos de entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)
    # Escalar las características para un mejor rendimiento
    sc = StandardScaler()
    sc.fit(X_train)
    X_train_std = sc.transform(X_train)
    X_test_std = sc.transform(X_test)
    
    #Crear un perceptrón y entrenar lo
    ppn = Perceptron (max_iter=100, eta0=0.1, random_state=42)
    ppn.fit(X_train_std, y_train)
    
    #Obtener los valores del usuario
    nuevos_valores = ingresar_valores()
    #Escalar los valores ingresados
    nuevos_valores_std=sc.transform([nuevos_valores])
    # Predecir el tipo de flor con los valores ingresados
    prediccion = ppn.predict(nuevos_valores_std)
    especies = iris.target_names
    print(f"El tipo de flor predicho es: {especies [prediccion[0]]}")


if __name__ == '__main__':
    solo_entrenamiento()
    prueba_con_datos_nuestros()