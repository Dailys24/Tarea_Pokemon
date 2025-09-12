#Interpretacion.py

import pandas as pd
from Analisis_exploratorio import analisis_eda

def interpretacion():
    #Ejecutar el EDA sin mostrar gráficos
    df, stats_by_type, correlation, ps_std_by_type = analisis_eda(mostrar_graficos=False)

    print("\nConclusiones:")
    print(f"- Tipos con mayor ataque: {stats_by_type.index[0]} y {stats_by_type.index[1]}")
    print(f"- Tipos con mayor defensa: {stats_by_type.sort_values(by='Defensa', ascending=False).index[0]}")
    print(f"- Correlación Ataque-Velocidad: {correlation:.1f} (relación {'fuerte' if abs(correlation) > 0.7 else 'moderada' if abs(correlation) > 0.4 else 'débil'})\n")
    print(f"- Tipo con PS más dispersos: {ps_std_by_type.index[0]}")

    #Pokémon más balanceado
    df["Desviacion"] = df[["Ataque", "Defensa", "Velocidad", "PS"]].std(axis=1)
    balanceado = df.loc[df["Desviacion"].idxmin()]

    print("\nPokémon más balanceado:")
    #Muestra las columnas de texto y luego las numéricas
    print(f"Nombre: {balanceado['Nombre']}, Tipo 1: {balanceado['Tipo 1']}")
    print(f"Ataque: {balanceado['Ataque']:.1f}, Defensa: {balanceado['Defensa']:.1f}, Velocidad: {balanceado['Velocidad']:.1f}, PS: {balanceado['PS']:.1f}\n")

    #Pokémon más especializado
    especializado = df.loc[df["Desviacion"].idxmax()]
    
    print("\nPokémon más especializado:")
    #Muestra las columnas de texto y luego las numéricas
    print(f"Nombre: {especializado['Nombre']}, Tipo 1: {especializado['Tipo 1']}")
    print(f"Ataque: {especializado['Ataque']:.1f}, Defensa: {especializado['Defensa']:.1f}, Velocidad: {especializado['Velocidad']:.1f}, PS: {especializado['PS']:.1f}")
    
if __name__ == '__main__':
    interpretacion()