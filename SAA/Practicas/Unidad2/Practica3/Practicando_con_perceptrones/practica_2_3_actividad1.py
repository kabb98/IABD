import numpy as np
import matplotlib.pyplot as plt

class Perceptron:
    def __init__(self, input_size, learning_rate=0.1, epochs=100):
        self.weights = np.zeros(input_size + 1)
        self.learning_rate = learning_rate
        self.epochs = epochs

    def predict(self, inputs):
        summation = np.dot(inputs, self.weights[1:]) + self.weights[0]
        return 1 if summation > 0 else 0

    def train(self, training_inputs, labels):
        errors = []  # Lista para almacenar el error en cada época
        for _ in range(self.epochs):
            total_error = 0
            for inputs, label in zip(training_inputs, labels):
                prediction = self.predict(inputs)
                error = label - prediction
                self.weights[1:] += self.learning_rate * error * inputs
                self.weights[0] += self.learning_rate * error
                total_error += error ** 2  # Error cuadrado para esta muestra
            errors.append(total_error)  # Agregamos el error total de la época
        return errors


def puerta_and():
    # Datos de entrenamiento (puerta lógica AND)
    training_inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    labels = np.array([0, 0, 0, 1])

    # Inicializamos y entrenamos el perceptrón
    perceptron = Perceptron(input_size=2, epochs=5)
    errors = perceptron.train(training_inputs, labels)

    # Graficamos el error en función de las épocas
    plt.plot(range(1, perceptron.epochs + 1), errors)
    plt.xlabel('Épocas')
    plt.ylabel('Error')
    plt.title('Error en función de las épocas')
    plt.show()

    # Prueba con entradas
    test_inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    for inputs in test_inputs:
        print(f"Entrada: {inputs}, Predicción: {perceptron.predict(inputs)}")

    print("Pesos finales: ", perceptron.weights)

def puerta_or():
    # Datos de entrenamiento (puerta lógica OR)
    training_inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    labels = np.array([0, 1, 1, 1])

    # Inicializamos y entrenamos el perceptrón
    perceptron = Perceptron(input_size=2, epochs=4)
    errors = perceptron.train(training_inputs, labels)

    # Graficamos el error en función de las épocas
    plt.plot(range(1, perceptron.epochs + 1), errors)
    plt.xlabel('Épocas')
    plt.ylabel('Error')
    plt.title('Error en función de las épocas')
    plt.show()

    # Prueba con entradas
    test_inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    for inputs in test_inputs:
        print(f"Entrada: {inputs}, Predicción: {perceptron.predict(inputs)}")

    print("Pesos finales: ", perceptron.weights)


def puerta_xor():
    # Datos de entrenamiento (puerta lógica XOR)
    training_inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    labels = np.array([0, 1, 1, 0])

    # Inicializamos y entrenamos el perceptrón
    perceptron = Perceptron(input_size=2, epochs=15)
    errors = perceptron.train(training_inputs, labels)

    # Graficamos el error en función de las épocas
    plt.plot(range(1, perceptron.epochs + 1), errors)
    plt.xlabel('Épocas')
    plt.ylabel('Error')
    plt.title('Error en función de las épocas')
    plt.show()

    # Prueba con entradas
    test_inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    for inputs in test_inputs:
        print(f"Entrada: {inputs}, Predicción: {perceptron.predict(inputs)}")

    print("Pesos finales: ", perceptron.weights)


def puerta_not():
    # Datos de entrenamiento (puerta lógica NOT)
    training_inputs = np.array([[0], [1]])
    labels = np.array([1, 0])

    # Inicializamos y entrenamos el perceptrón
    perceptron = Perceptron(input_size=1, epochs=5)
    errors = perceptron.train(training_inputs, labels)

    # Graficamos el error en función de las épocas
    plt.plot(range(1, perceptron.epochs + 1), errors)
    plt.xlabel('Épocas')
    plt.ylabel('Error')
    plt.title('Error en función de las épocas')
    plt.show()

    # Prueba con entradas
    test_inputs = np.array([[0], [1]])
    for inputs in test_inputs:
        print(f"Entrada: {inputs}, Predicción: {perceptron.predict(inputs)}")

    print("Pesos finales: ", perceptron.weights)


def puerta_nand():
    # Datos de entrenamiento (puerta lógica NAND)
    training_inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    labels = np.array([1, 1, 1, 0])

    # Inicializamos y entrenamos el perceptrón
    perceptron = Perceptron(input_size=2, epochs=5)
    errors = perceptron.train(training_inputs, labels)

    # Graficamos el error en función de las épocas
    plt.plot(range(1, perceptron.epochs + 1), errors)
    plt.xlabel('Épocas')
    plt.ylabel('Error')
    plt.title('Error en función de las épocas')
    plt.show()

    # Prueba con entradas
    test_inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    for inputs in test_inputs:
        print(f"Entrada: {inputs}, Predicción: {perceptron.predict(inputs)}")

    print("Pesos finales: ", perceptron.weights)

def puerta_nor():
    # Datos de entrenamiento (puerta lógica NOR)
    training_inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    labels = np.array([1, 0, 0, 0])

    # Inicializamos y entrenamos el perceptrón
    perceptron = Perceptron(input_size=2, epochs=5)
    errors = perceptron.train(training_inputs, labels)

    # Graficamos el error en función de las épocas
    plt.plot(range(1, perceptron.epochs + 1), errors)
    plt.xlabel('Épocas')
    plt.ylabel('Error')
    plt.title('Error en función de las épocas')
    plt.show()

    # Prueba con entradas
    test_inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    for inputs in test_inputs:
        print(f"Entrada: {inputs}, Predicción: {perceptron.predict(inputs)}")

    print("Pesos finales: ", perceptron.weights)


if __name__ == '__main__':
    # puerta_and()
    # puerta_or()
    # puerta_xor()
    # puerta_not()
    # puerta_nand()
    puerta_nor()