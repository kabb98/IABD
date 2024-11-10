from sklearn.datasets import fetch_lfw_people
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
import matplotlib.pyplot as plt

# Cargar el conjunto de datos LFW (Labeled Faces in the Wild)
lfw_people = fetch_lfw_people(min_faces_per_person=70, resize=0.4)

# Obtener características e etiquetas
X = lfw_people.data
y = lfw_people.target

# Aplicar LDA para reducir la dimensionalidad a 3 componentes
lda = LDA(n_components=2)
X_r = lda.fit(X, y).transform(X)

# Visualizar los resultados en 3D
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Crear un scatter plot en 3D para cada clase
for i in range(len(lfw_people.target_names)):
    ax.scatter(X_r[y == i, 0], X_r[y == i, 1], X_r[y == i, 2], alpha=0.8, label=lfw_people.target_names[i])

# Añadir leyenda y etiquetas
ax.legend(loc='best', shadow=False, scatterpoints=1)
ax.set_title('LDA for LFW Dataset')
ax.set_xlabel('LD1')
ax.set_ylabel('LD2')
ax.set_zlabel('LD3')

# Mostrar la gráfica
plt.show()
