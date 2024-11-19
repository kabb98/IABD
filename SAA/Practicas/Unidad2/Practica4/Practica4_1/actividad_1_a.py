
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
#Cargar el conjunto de datos de iris
iris = datasets.load_iris()
X = iris.data
y= iris.target
target_names = iris.target_names

# Aplicar LDA para reducción de dimensionalidad
lda = LinearDiscriminantAnalysis (n_components=3)
X_r = lda.fit(X, y).transform(X)

# Visualizar los resultados
plt.figure()
colors = ['navy', 'turquoise', 'darkorange']
lw = 2

for color, i, target_name in zip (colors, [0, 1, 2], target_names):
    plt.scatter (X_r[y==i, 0], X_r[y == i, 1], color=color, alpha=.8, lw= lw,
                 label= target_name)

plt.legend (loc='best', shadow=False, scatterpoints=1)
plt.title('LDA of IRIS dataset')
plt.show()