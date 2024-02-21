import pandas as pd
import matplotlib.pyplot as plt

# Leer el archivo CSV
df = pd.read_csv(r'C:\Users\DELL\OneDrive\Escritorio\Github\analisisDatos\spotify-2023.csv')

# Dividir la columna 'artist(s)_name' en casos de múltiples artistas y expandirlos en filas
artists = df['artist(s)_name'].str.split(', ', expand=True).stack()

# Convertir el índice de nivel 1 a columna
artists = artists.reset_index(level=1, drop=True)

# Dar un nombre adecuado a la serie resultante
artists.name = 'artist'

# Concatenar la serie con el DataFrame original
df = df.join(artists)

# Contar el número de veces que aparece cada artista
collaborations = df['artist'].value_counts()

# Ordenar los resultados
collaborations = collaborations.sort_values(ascending=False)

# Seleccionar los 10 artistas con más colaboraciones para visualizar
top_collaborations = collaborations.head(10)

# Crear el gráfico de barras
plt.figure(figsize=(10, 6))
top_collaborations.plot(kind='bar', color='skyblue')
plt.title('Top 10 Artistas con Más Colaboraciones')
plt.xlabel('Artista')
plt.ylabel('Número de Colaboraciones')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
