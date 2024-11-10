from sklearn.datasets import fetch_lfw_people
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split



lfw_people = fetch_lfw_people(min_faces_per_person=70, resize=0.4)
X = lfw_people.data
y = lfw_people.target

_, X_test, _, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

lda = LDA(n_components=None) 
X_lda = lda.fit_transform(X, y)

lda_classifier = LDA()
lda_classifier.fit(X_lda, y)

X_test_lda = lda.transform(X_test)
y_pred = lda_classifier.predict(X_test_lda)

accuracy = np.mean(y_pred == y_test)

random_indices = np.random.choice(len(X_test), 5, replace=False)
X_samples = X_test[random_indices]
y_samples = y_test[random_indices]

X_samples_lda = lda.transform(X_samples)
y_pred_samples = lda_classifier.predict(X_samples_lda)

plt.figure(figsize=(15, 3))
for i in range(5):
    plt.subplot(1, 5, i + 1)
    plt.imshow(X_samples[i].reshape(50, 37), cmap='gray')
    plt.title(f"Real: {lfw_people.target_names[y_samples[i]]}\nPredicción: {lfw_people.target_names[y_pred_samples[i]]}")
plt.axis('off')
plt.show()
