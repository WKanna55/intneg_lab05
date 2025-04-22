import pandas as pd
from sklearn.experimental import enable_iterative_imputer  # Habilitar el uso de IterativeImputer
from sklearn.impute import IterativeImputer

# Cargar el dataset
file_path = "housing-with-missing-1.csv"
df = pd.read_csv(file_path, delimiter=";")

# Verificar si hay valores nulos
print("Valores nulos antes de la imputación:")
print(df.isnull().sum())

# Imputar los valores faltantes utilizando IterativeImputer (Imputación multivariante)
imputer = IterativeImputer(max_iter=10, random_state=42)
df_imputed = pd.DataFrame(imputer.fit_transform(df), columns=df.columns)

# Verificar si los valores nulos han sido imputados
print("\nValores nulos después de la imputación:")
print(df_imputed.isnull().sum())

# Mostrar las primeras filas de los datos imputados
print("\nDatos imputados:")
print(df_imputed.head())
