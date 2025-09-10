#Visualizacion_datos.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def visualizar_datos():
    try:
        #Cargar los datos
        df = pd.read_csv('pokemon_primera_gen.csv')

        # --- Histograma de Ataque ---
        plt.figure(figsize=(10, 6))
        plt.hist(df['Ataque'], bins=15, edgecolor='black', color='skyblue')
        plt.title('Distribución de los valores de Ataque')
        plt.xlabel('Puntos de Ataque')
        plt.ylabel('Frecuencia')
        plt.grid(axis='y', alpha=0.75)
        plt.show()

        # --- Gráfico de dispersión (Ataque vs. Velocidad) ---
        plt.figure(figsize=(10, 6))
        plt.scatter(df['Ataque'], df['Velocidad'], alpha=0.6, color='coral')
        plt.title('Relación entre Ataque y Velocidad')
        plt.xlabel('Ataque')
        plt.ylabel('Velocidad')
        plt.grid(True)
        plt.show()

        # --- Boxplot de PS por Tipo 1 ---
        plt.figure(figsize=(12, 8))
        df.boxplot(column='PS', by='Tipo 1', figsize=(12, 8), vert=True, patch_artist=True)
        plt.title('Distribución de Puntos de Salud (PS) por Tipo Principal')
        plt.suptitle('')  # Elimina el título automático
        plt.xlabel('Tipo Principal')
        plt.ylabel('Puntos de Salud (PS)')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.show()

        # --- Diagrama de violín para la Defensa ---
        plt.figure(figsize=(10, 6))
        sns.violinplot(x=df['Defensa'], color='lightgreen')
        plt.title('Distribución de la Defensa')
        plt.xlabel('Puntos de Defensa')
        plt.grid(True)
        plt.show()

    except FileNotFoundError:
        print("Error: El archivo 'pokemon_primera_gen.csv' no fue encontrado.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

#Para ejecutar la función directamente si es necesario
if __name__ == '__main__':
    visualizar_datos()