import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

# Descargar el conjunto de datos de crédito alemán desde una URL
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/statlog/german/german.data'
column_names = [
    "Status_of_existing_checking_account", 
    "Duration_in_month", "Credit_history", "Purpose",
    "Credit_amount", "Savings_account", 
    "Present_employment_since", "Installment_rate",
    "Personal_status_and_sex", "Other_debtors", 
    "Present_residence_since", "Property",
    "Age", "Other_installment_plans", "Housing", 
    "Number_of_existing_credits", "Job",
    "Number_of_people_being_liable", "Telephone", 
    "Foreign_worker", "Credit_approval"
]

# Cargar el conjunto de datos en un DataFrame de Pandas
data = pd.read_csv(url, delimiter=' ', header=None, 
names=column_names)

# Convertir variables categóricas usando One-Hot Encoding
categorical_cols = [
"Status_of_existing_checking_account", "Credit_history", "Purpose", 
"Savings_account",
"Present_employment_since", "Personal_status_and_sex", "Other_debtors", 
"Property",
"Other_installment_plans", "Housing", "Job", "Telephone", 
"Foreign_worker"
]

numeric_cols = [col for col in data.columns if col not in categorical_cols and col != "Credit_approval"]

# Aplicar One-Hot Encoding a las variables categóricas
data = pd.get_dummies(data, columns=categorical_cols, drop_first=True)

# Separar características (X) y etiquetas (y)
X = data.drop('Credit_approval', axis=1)
y = data['Credit_approval']

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, 
random_state=42)

# Crear un clasificador de Bosques Aleatorios (Random Forest)
clf = RandomForestClassifier()

# Entrenar el clasificador con los datos de entrenamiento
clf.fit(X_train, y_train)

# Realizar predicciones en el conjunto de prueba
y_pred = clf.predict(X_test)

# Calcular la precisión del modelo
accuracy = accuracy_score(y_test, y_pred)
print(f"Precisión del modelo de Bosques Aleatorios: {accuracy:.2f}")

# Matriz de confusión para evaluar el rendimiento del modelo
conf_matrix = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(6, 4))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', 
cbar=False)
plt.xlabel('Predicción')
plt.ylabel('Valor Real')
plt.title('Matriz de Confusión')
plt.show()