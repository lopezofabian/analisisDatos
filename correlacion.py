import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Paso 1: Cargar los datos
df = pd.read_csv(r'C:\Users\DELL\OneDrive\Escritorio\Github\analisisDatos\spotify-2023.csv')

# Paso 2: Eliminar las columnas no numéricas
df_numeric = df.select_dtypes(include=['int64', 'float64'])

# Paso 3: Calcular la matriz de correlación
correlation_matrix = df_numeric.corr()

# Paso 4: Visualizar el mapa de correlación
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title('Mapa de Correlación de Características Musicales')
plt.show()