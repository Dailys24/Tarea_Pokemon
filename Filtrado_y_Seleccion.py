#Filtrado_y_Seleccion.py

import pandas as pd

def filtrar_pokemons_fuego():
    #Cargar los datos del archivo CSV
    df = pd.read_csv('pokemon_primera_gen.csv')

    #Filtrar los Pokémon de tipo "Fuego"
    pokemons_fuego = df[df['Tipo 1'] == 'Fuego']

    #Seleccionar solo las columnas Nombre, Tipo 1, Ataque y Velocidad
    resultado = pokemons_fuego[['Nombre', 'Tipo 1', 'Ataque', 'Velocidad']]

    #Mostrar el resultado
    print("------------------------------------------------------------------------------------")
    print("Resultados del filtrado y selección:")
    print(resultado)
    print("------------------------------------------------------------------------------------")
    return resultado