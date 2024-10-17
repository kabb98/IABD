

import tensorflow as tf
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from keras.api.datasets import cifar10
import matplotlib.pyplot as plt
from sklearn.metrics import ConfusionMatrixDisplay


from keras.api.models import Sequential
from keras.api.layers import Dense

from keras.api.layers import Conv2D, MaxPooling2D, Flatten, Dense
from keras.api.utils import to_categorical, image_dataset_from_directory


def clasificar_random_forest():
    # Cargar el conjunto de datos CIFAR-10
    (x_train, y_train), (x_test, y_test) = cifar10.load_data()
    # Tomar solo una fracción del conjunto de datos para reducir la memoria
    frac = 0.2
    x_train, _, y_train, _ = train_test_split(x_train, y_train, 
    test_size=1-frac, random_state=42)
    # Aplanar las imágenes y normalizar los valores de píxeles a un rango de 0 a 1
    x_train = x_train.reshape((x_train.shape[0], -1)) / 255.0
    x_test = x_test.reshape((x_test.shape[0], -1)) / 255.0
    # Convertir las etiquetas a un formato unidimensional
    y_train = np.ravel(y_train)
    y_test = np.ravel(y_test)
    # Dividir el conjunto de entrenamiento en entrenamiento y validación
    x_train, x_val, y_train, y_val = train_test_split(x_train, y_train, 
    test_size=0.2, random_state=42)
    # Crear y entrenar un clasificador de bosques aleatorios
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(x_train, y_train)
    # Realizar predicciones en el conjunto de prueba
    y_pred_test = clf.predict(x_test.reshape((x_test.shape[0], -1)))


    # Evaluar la precisión en el conjunto de prueba
    accuracy_test = accuracy_score(y_test, y_pred_test)
    # Mostrar métricas adicionales
    print("\nInforme de clasificación en el conjunto de prueba:")
    print(classification_report(y_test, y_pred_test))
    # Crear la matriz de confusión
    cm = confusion_matrix(y_test, y_pred_test)
    # Mostrar la matriz de confusión
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, 
    display_labels=np.unique(y_test))
    disp.plot(cmap=plt.cm.Blues, values_format='d')
    plt.title('Matriz de Confusión en Conjunto de Prueba')
    plt.show()

def clasificar_nn():
    # Cargar el conjunto de datos CIFAR-10
    (x_train, y_train), (x_test, y_test) = cifar10.load_data()
    # Tomar solo una fracción del conjunto de datos para reducir la memoria
    frac = 0.2
    x_train, _, y_train, _ = train_test_split(x_train, y_train, 
    test_size=1-frac, random_state=42)
    # Aplanar las imágenes y normalizar los valores de píxeles a un rango de 0 a 1
    x_train = x_train.reshape((x_train.shape[0], -1)) / 255.0
    x_test = x_test.reshape((x_test.shape[0], -1)) / 255.0
    # Convertir las etiquetas a un formato unidimensional
    y_train = np.ravel(y_train)
    y_test = np.ravel(y_test)
    # Dividir el conjunto de entrenamiento en entrenamiento y validación
    x_train, x_val, y_train, y_val = train_test_split(x_train,
                                                      y_train, test_size=0.2, random_state=42)
    
    # Construir una red neuronal simple
    model = Sequential()
    model.add(Dense(128, input_dim=x_train.shape[1], activation='relu'))
    model.add(Dense(10, activation='softmax'))  
    model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', 
    metrics=['accuracy'])
    history = model.fit(x_train, y_train, epochs=50, batch_size=32, 
    validation_data=(x_val, y_val), verbose=1)
    y_pred_test_probs = model.predict(x_test)
    y_pred_test = np.argmax(y_pred_test_probs, axis=1)
    accuracy_test = accuracy_score(y_test, y_pred_test)
    # Mostrar métricas adicionales
    print("\nInforme de clasificación en el conjunto de prueba:")
    print(classification_report(y_test, y_pred_test))
    # Crear la matriz de confusión
    cm = confusion_matrix(y_test, y_pred_test)
    # Mostrar la matriz de confusión
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, 
    display_labels=np.unique(y_test))
    disp.plot(cmap=plt.cm.Blues, values_format='d')
    plt.title('Matriz de Confusión en Conjunto de Prueba')
    plt.show()
    # Mostrar la curva de aprendizaje
    plt.plot(history.history['accuracy'], label='Training Accuracy')
    plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
    plt.xlabel('Epoch')
    plt.ylabel('Accuracy')
    plt.legend()
    plt.title('Curva de Aprendizaje')
    plt.show()




def clasificar_cnn():
    # Cargar el conjunto de datos CIFAR-10
    (x_train, y_train), (x_test, y_test) = cifar10.load_data()

    # Tomar solo una fracción del conjunto de datos para reducir la memoria
    frac = 0.2
    x_train, _, y_train, _ = train_test_split(x_train, y_train, test_size=1-frac, random_state=42)

    # Normalizar los valores de píxeles a un rango de 0 a 1
    x_train = x_train / 255.0
    x_test = x_test / 255.0

    # Convertir las etiquetas a un formato unidimensional
    y_train = np.ravel(y_train)
    y_test = np.ravel(y_test)

    # Convertir las etiquetas a un formato categórico (one-hot encoding)
    y_train = to_categorical(y_train, 10)
    y_test = to_categorical(y_test, 10)

    # Dividir el conjunto de entrenamiento en entrenamiento y validación
    x_train, x_val, y_train, y_val = train_test_split(x_train, y_train, test_size=0.2, random_state=42)

    # Crear datasets de TensorFlow para entrenamiento y validación
    train_ds = tf.data.Dataset.from_tensor_slices((x_train, y_train)).shuffle(10000).batch(32).prefetch(tf.data.AUTOTUNE)
    val_ds = tf.data.Dataset.from_tensor_slices((x_val, y_val)).batch(32).prefetch(tf.data.AUTOTUNE)

    # Definir el modelo
    model = Sequential([
        Conv2D(32, (3, 3), input_shape=(32, 32, 3), activation='relu'),
        MaxPooling2D((2, 2)),
        Conv2D(64, (3, 3), activation='relu'),
        MaxPooling2D((2, 2)),
        Flatten(),
        Dense(128, activation='relu'),
        Dense(10, activation='softmax')
    ])

    # Compilar el modelo
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

    # Entrenar la red neuronal convolucional con el dataset de entrenamiento
    history = model.fit(train_ds, epochs=10, validation_data=val_ds, verbose=1)

    # Realizar predicciones en el conjunto de prueba
    y_pred_test_probs = model.predict(x_test)
    y_pred_test = np.argmax(y_pred_test_probs, axis=1)

    # Evaluar la precisión en el conjunto de prueba
    accuracy_test = accuracy_score(np.argmax(y_test, axis=1), y_pred_test)
    print(f"\nPrecisión en el conjunto de prueba: {accuracy_test:.4f}")

    # Mostrar métricas adicionales
    print("\nInforme de clasificación en el conjunto de prueba:")
    print(classification_report(np.argmax(y_test, axis=1), y_pred_test))

    # Crear la matriz de confusión
    cm = confusion_matrix(np.argmax(y_test, axis=1), y_pred_test)

    # Mostrar la matriz de confusión
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=np.unique(np.argmax(y_test, axis=1)))
    disp.plot(cmap=plt.cm.Blues, values_format='d')
    plt.title('Matriz de Confusión en Conjunto de Prueba')
    plt.show()

    # Mostrar la curva de aprendizaje
    plt.plot(history.history['accuracy'], label='Training Accuracy')
    plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
    plt.xlabel('Epoch')
    plt.ylabel('Accuracy')
    plt.legend()
    plt.title('Curva de Aprendizaje')
    plt.show()




def main():
    clasificar_random_forest()
    clasificar_nn()
    clasificar_cnn()

if __name__ == "__main__":
    main()