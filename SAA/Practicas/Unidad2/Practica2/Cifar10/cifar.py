import numpy as np
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from keras.api.datasets import cifar10

def clustering_cifar():
    # Cargar el conjunto de datos CIFAR-10
    (train_images, train_labels), (_, _) = cifar10.load_data()
    # Filtrar las imágenes de las categorías de "coches" (label 1) y "aviones" (label 0)
    car_indices = np.where((train_labels == 1).squeeze())[0][:5000]
    airplane_indices = np.where((train_labels == 0).squeeze())[0][:5000]
    selected_indices = np.concatenate((car_indices, airplane_indices))
    selected_images = train_images[selected_indices]
    # Redimensionar y normalizar las imágenes para el clustering
    selected_images = selected_images.reshape(selected_images.shape[0], -1)
    selected_images = selected_images / 255.0
    # Reducir la dimensionalidad a 2 componentes con PCA
    pca = PCA(n_components=2)
    selected_images_pca = pca.fit_transform(selected_images)
    # Realizar el clustering con K-Means
    kmeans = KMeans(n_clusters=2, n_init=10)
    kmeans.fit(selected_images_pca)
    clusters = kmeans.predict(selected_images_pca)
    # Visualización en 2D
    plt.scatter(selected_images_pca[:, 0], selected_images_pca[:, 1], 
    c=clusters, cmap='viridis')
    plt.title('Clustering de las categorías "coches" y "aviones" de CIFAR-10')
    plt.xlabel('Componente Principal 1')
    plt.ylabel('Componente Principal 2')
    plt.show()

def clustering_no_supervisado():
    # Cargar el conjunto de datos CIFAR-10
    (train_images, train_labels), (_, _) = cifar10.load_data()
    # Filtrar 100 imágenes de cada categoría
    category_indices = [np.where(train_labels == i)[0][:100] for i in 
    range(10)]
    selected_indices = np.concatenate(category_indices)
    selected_images = train_images[selected_indices]
    # Redimensionar y normalizar las imágenes para el clustering
    selected_images = selected_images.reshape(selected_images.shape[0], -1)
    selected_images = selected_images / 255.0
    # Reducir la dimensionalidad a 2 componentes con PCA
    pca = PCA(n_components=2)
    selected_images_pca = pca.fit_transform(selected_images)
    # Realizar el clustering con K-Means (10 clusters)
    kmeans = KMeans(n_clusters=10, n_init=10)
    kmeans.fit(selected_images_pca)
    clusters = kmeans.predict(selected_images_pca)
    # Visualización en 2D
    plt.scatter(selected_images_pca[:, 0], selected_images_pca[:, 1], 
    c=clusters, cmap='viridis')
    plt.title('Clustering no supervisado de CIFAR-10 (10 clusters)')
    plt.xlabel('Componente Principal 1')
    plt.ylabel('Componente Principal 2')
    plt.show()

def main():
    clustering_cifar()
    clustering_no_supervisado()

if __name__ == '__main__':
    main()