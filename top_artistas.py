import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos
df = pd.read_csv(r'C:\Users\DELL\OneDrive\Escritorio\Github\analisisDatos\spotify-2023.csv')

# Contar el número de apariciones de cada artista en la lista de reproducción
artist_counts = df['artist(s)_name'].value_counts().head(10)  # Obtener los 10 artistas más populares

# Graficar el recuento de artistas
plt.figure(figsize=(10, 6))
artist_counts.plot(kind='bar', color='skyblue')
plt.title('Top 10 Artistas Más Populares en la Lista de Reproducción')
plt.xlabel('Artista')
plt.ylabel('Número de Apariciones')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
