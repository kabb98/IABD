from sklearn.datasets import fetch_openml
from sklearn.linear_model import Perceptron
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import numpy as np

# Cargar el dataset MNIST
mnist = fetch_openml('mnist_784', version=1, parser='auto', as_frame=False)

# Obtener características (X) y etiquetas (y)
X = mnist.data
y = mnist.target.astype(int)

# Dividir el dataset en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Escalar las características para un mejor rendimiento
sc = StandardScaler()
sc.fit(X_train)
X_train_std = sc.transform(X_train)
X_test_std = sc.transform(X_test)

# Crear un perceptrón y preparar variables para almacenar la precisión por época
ppn = Perceptron(max_iter=1, eta0=0.1, random_state=42, warm_start=True)  # max_iter=1 y warm_start=True para entrenar en cada época
epochs = 50  # Número de épocas para ver la evolución de aprendizaje
accuracy_train = []
accuracy_test = []

# Entrenar el perceptrón y registrar la precisión en cada época
for epoch in range(epochs):
    ppn.fit(X_train_std, y_train)
    y_train_pred = ppn.predict(X_train_std)
    y_test_pred = ppn.predict(X_test_std)
    train_accuracy = accuracy_score(y_train, y_train_pred)
    test_accuracy = accuracy_score(y_test, y_test_pred)
    accuracy_train.append(train_accuracy)
    accuracy_test.append(test_accuracy)
    print(f"Época {epoch+1}, Precisión en entrenamiento: {train_accuracy}, Precisión en prueba: {test_accuracy}")

# Graficar la precisión en función de las épocas
plt.plot(range(1, epochs + 1), accuracy_train, label='Precisión en entrenamiento')
plt.plot(range(1, epochs + 1), accuracy_test, label='Precisión en prueba')
plt.xlabel('Épocas')
plt.ylabel('Precisión')
plt.title('Evolución de la Precisión en Función de las Épocas')
plt.legend()
plt.show()

# Mostrar precisión final en el conjunto de prueba
print(f'Precisión final en prueba: {accuracy_test[-1]}')


# Obtener los pesos y el sesgo del perceptrón
weights = ppn.coef_
bias = ppn.intercept_
# Mostrar los pesos de las características
print("Pesos de las características:")
for i, weight in enumerate (weights[0]):
    print (f" Feature {i}: {weight}")
# Mostrar el peso del sesgo print
(f"Sesgo (Bias): {bias[0]}")


# Mostrar 10 imágenes con sus etiquetas y predicciones
num_images = 10
indices = np.random.choice(X_test.shape[0], num_images, replace=False)
for idx in indices:
    plt.imshow(X_test[idx].reshape(28, 28), cmap='gray')
    plt.title(f"Valor real: {y_test[idx]}, Predicción: {y_test_pred[idx]}")
    plt.axis('off')
    plt.show()