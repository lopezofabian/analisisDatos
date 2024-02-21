import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt

# Cargar los datos
df = pd.read_csv(r'C:\Users\DELL\OneDrive\Escritorio\Github\analisisDatos\spotify-2023.csv')

# Extraer los títulos de las canciones
titles = df['track_name']

# Convertir todos los títulos a minúsculas para un análisis más consistente
titles_lower = titles.str.lower()

# Crear una lista de palabras clave
keywords = ['love', 'heartbreak', 'party', 'dance', 'summer', 'sad', 'happy', 'life', 'dream', 'night']

# Contar la frecuencia de cada palabra clave en los títulos
keyword_counts = {keyword: sum(titles_lower.str.contains(keyword)) for keyword in keywords}

# Convertir el diccionario en un DataFrame para facilitar la visualización
keyword_df = pd.DataFrame.from_dict(keyword_counts, orient='index', columns=['count'])

# Ordenar el DataFrame por frecuencia descendente
keyword_df = keyword_df.sort_values(by='count', ascending=False)

# Graficar los resultados
plt.figure(figsize=(10, 6))
keyword_df.plot(kind='bar', color='skyblue')
plt.title('Frecuencia de palabras clave en títulos de canciones')
plt.xlabel('Palabra clave')
plt.ylabel('Frecuencia')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
