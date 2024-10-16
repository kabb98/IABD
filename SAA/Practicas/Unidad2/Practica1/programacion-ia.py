from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar el conjunto de datos de cáncer de mama
data = load_breast_cancer()
X = data.data
y = data.target

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Crear un modelo de clasificación utilizando Random Forest
model = RandomForestClassifier(n_estimators=100, random_state=42)

# Entrenar el modelo con los datos de entrenamiento
model.fit(X_train, y_train)

# Realizar predicciones con los datos de prueba
y_pred = model.predict(X_test)

# Calcular la matriz de confusión
conf_matrix = metrics.confusion_matrix(y_test, y_pred)

# Mostrar la matriz de confusión como un heatmap
plt.figure(figsize=(12, 4))

plt.subplot(1, 2, 1)
sns.heatmap(conf_matrix, annot=True, cmap='Blues', fmt='g')
plt.xlabel('Predicción')
plt.ylabel('Valor Real')
plt.title('Matriz de Confusión')

# Evaluar la precisión del modelo
accuracy = metrics.accuracy_score(y_test, y_pred)
print(f"Precisión del modelo: {accuracy}")

# Graficar la evolución de la precisión con respecto al número de árboles
plt.subplot(1, 2, 2)

# Definir el rango de árboles que se probarán
num_trees = [10, 50, 100, 200, 300]

# Lista para almacenar la precisión de cada modelo
accuracies = []

for trees in num_trees:
    # Crear un modelo de clasificación utilizando Random Forest
    model = RandomForestClassifier(n_estimators=trees, random_state=42)

    # Entrenar el modelo con los datos de entrenamiento
    model.fit(X_train, y_train)

    # Realizar predicciones con los datos de prueba
    y_pred = model.predict(X_test)

    # Evaluar la precisión del modelo y almacenarla
    accuracy = metrics.accuracy_score(y_test, y_pred)
    accuracies.append(accuracy)

    print(f"Precisión del modelo con {trees} árboles: {accuracy}")

# Graficar la evolución de la precisión con respecto al número de árboles
plt.plot(num_trees, accuracies, marker='o')
plt.xlabel('Número de Árboles')
plt.ylabel('Precisión del Modelo')
plt.title('Evolución de la Precisión del Modelo con Random Forest')
plt.grid(True)

plt.tight_layout()
plt.show()