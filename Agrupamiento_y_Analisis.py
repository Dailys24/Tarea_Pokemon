#Agrupamiento y analisis por grupo

import pandas as pd

def estadisticas_alaisis():
    try:
        #Cargar los datos
        df = pd.read_csv('pokemon_primera_gen.csv')

        #Agrupar por 'Tipo 1' y calcular estadísticas de Ataque
        print("\n--- Estadísticas de Ataque por Tipo Principal ---")
        estadisticas_ataque = df.groupby('Tipo 1')['Ataque'].agg(['mean', 'median', 'std']).round(1)
        print(estadisticas_ataque)

        #Encontrar el tipo con mayor promedio de Velocidad
        print("\n--- Tipo con Mayor Promedio de Velocidad ---")
        promedio_velocidad = df.groupby('Tipo 1')['Velocidad'].mean().round(1)
        tipo_mayor_velocidad = promedio_velocidad.idxmax()
        valor_mayor_velocidad = promedio_velocidad.max()
        print(f"El tipo con el mayor promedio de velocidad es: {tipo_mayor_velocidad} con un promedio de {valor_mayor_velocidad:.1f}")

        #Encontrar el Pokémon con mayor y menor PS para cada tipo
        print("\n--- Pokémon con Mayor y Menor PS por Tipo Principal ---")
        idx_max_ps = df.groupby('Tipo 1')['PS'].idxmax()
        idx_min_ps = df.groupby('Tipo 1')['PS'].idxmin()

        pokemon_max_ps = df.loc[idx_max_ps, ['Nombre', 'Tipo 1', 'PS']].reset_index(drop=True)
        pokemon_min_ps = df.loc[idx_min_ps, ['Nombre', 'Tipo 1', 'PS']].reset_index(drop=True)

        #Redondear PS a 1 decimal si fuera necesario (aunque normalmente son enteros)
        pokemon_max_ps['PS'] = pokemon_max_ps['PS'].round(1)
        pokemon_min_ps['PS'] = pokemon_min_ps['PS'].round(1)

        print("\nPokémon con MAYOR PS por tipo:")
        print(pokemon_max_ps)

        print("\nPokémon con MENOR PS por tipo:")
        print(pokemon_min_ps)

    except FileNotFoundError:
        print("Error: El archivo 'pokemon_primera_gen.csv' no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

if __name__ == '__main__':
    estadisticas_alaisis()