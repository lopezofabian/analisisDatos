import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Paso 1: Cargar los datos
df = pd.read_csv(r'C:\Users\DELL\OneDrive\Escritorio\Github\analisisDatos\spotify-2023.csv')

# Contar la cantidad de canciones en listas de reproducción de Spotify y Apple
spotify_counts = df['in_spotify_playlists'].sum()
apple_counts = df['in_apple_playlists'].sum()

# Crear un gráfico de barras
plt.figure(figsize=(8, 6))
plt.bar(['Spotify', 'Apple'], [spotify_counts, apple_counts], color=['green', 'blue'])
plt.xlabel('Plataforma de Streaming')
plt.ylabel('Número de Canciones')
plt.title('Número de Canciones en Listas de Reproducción de Spotify y Apple')
plt.show()