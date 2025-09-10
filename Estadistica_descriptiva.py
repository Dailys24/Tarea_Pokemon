#Estadisticas_y_Consultas.py

import pandas as pd

def estadisticas():
    try:
        #Cargar los datos
        df = pd.read_csv('pokemon_primera_gen.csv')

        #Cálculos de Ataque
        print("\n--- Estadísticas de Ataque ---")
        promedio_ataque = df['Ataque'].mean()
        mediana_ataque = df['Ataque'].median()
        moda_ataque = df['Ataque'].mode()
        print(f"Promedio de Ataque: {promedio_ataque:.2f}")
        print(f"Mediana de Ataque: {mediana_ataque}")
        print(f"Moda de Ataque: {moda_ataque.tolist()}")

        #Consultas específicas de Pokémon
        print("\n--- Consultas de Pokémon ---")
        pokemon_mayor_defensa = df.loc[df['Defensa'].idxmax()]
        pokemon_menor_velocidad = df.loc[df['Velocidad'].idxmin()]
        print(f"Pokémon con mayor defensa: {pokemon_mayor_defensa['Nombre']} (Defensa: {pokemon_mayor_defensa['Defensa']})")
        print(f"Pokémon con menor velocidad: {pokemon_menor_velocidad['Nombre']} (Velocidad: {pokemon_menor_velocidad['Velocidad']})")

        #Conteo de Pokémon con dos tipos
        print("\n--- Conteo de Tipos ---")
        pokemon_dos_tipos = df['Tipo 2'].count()
        print(f"Número de Pokémon con dos tipos: {pokemon_dos_tipos}")

        #Estadísticas de Puntos de Salud (PS)
        print("\n--- Estadísticas de PS ---")
        rango_ps = df['PS'].max() - df['PS'].min()
        desviacion_estandar_ps = df['PS'].std()
        print(f"Rango de PS: {rango_ps}")
        print(f"Desviación estándar de PS: {desviacion_estandar_ps:.2f}")

    except FileNotFoundError:
        print("Error: El archivo 'pokemon_primera_gen.csv' no fue encontrado. Asegúrate de que esté en el mismo directorio.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")