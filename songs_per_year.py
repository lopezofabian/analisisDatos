import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Paso 1: Cargar los datos
df = pd.read_csv(r'C:\Users\DELL\OneDrive\Escritorio\Github\analisisDatos\spotify-2023.csv')
songs_per_year = df['released_year'].value_counts().sort_index()

# Crear el gráfico de barras
plt.figure(figsize=(10, 6))
songs_per_year.plot(kind='bar', color='skyblue')
plt.title('Recuento de canciones por año de lanzamiento')
plt.xlabel('Año de lanzamiento')
plt.ylabel('Número de canciones')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()