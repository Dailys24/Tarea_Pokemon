#Poder_total.py

import pandas as pd

def calcular_poder_total():
    try:
        #Agregar los datos
        df = pd.read_csv('pokemon_primera_gen.csv')

        #Crear la columna "Poder Total"
        df['Poder Total'] = df['Ataque'] + df['Defensa'] + df['Velocidad'] + df['PS']

        #Ordenar el DataFrame por "Poder Total" de mayor a menor
        df_ordenado = df.sort_values(by='Poder Total', ascending=False)
        
        #Mostrar el resultado (los primeros 10 Pokémon)
        print("\n--- Pokémon ordenados por Poder Total (Top 10) ---")
        print(df_ordenado[['Nombre', 'Poder Total', 'Ataque', 'Defensa', 'Velocidad', 'PS']].head(10))
        print("-----------------------------------------------------")
        
        return df_ordenado

    except FileNotFoundError:
        print("Error: El archivo 'pokemon_primera_gen.csv' no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

if __name__ == '__main__':
    calcular_poder_total()