#Analisis_exploratorio.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def analisis_eda(mostrar_graficos=True):
    #Cargar datos
    df = pd.read_csv("pokemon_primera_gen.csv")

    #Forzar columnas numéricas por seguridad
    cols_numericas = ["Ataque", "Defensa", "Velocidad", "PS"]
    df[cols_numericas] = df[cols_numericas].apply(pd.to_numeric, errors="coerce")

    #Tipos con mayor ataque o defensa (redondeado a 1 decimal)
    stats_by_type = (
        df.groupby("Tipo 1")[["Ataque", "Defensa"]]
        .mean()
        .round(1)
        .sort_values(by="Ataque", ascending=False)
    )
    print("Promedio de Ataque y Defensa por Tipo:")
    print(stats_by_type)

    #Correlación entre ataque y velocidad (1 decimal)
    correlation = round(df["Ataque"].corr(df["Velocidad"]), 1)
    print(f"\nCoeficiente de correlación entre Ataque y Velocidad: {correlation:.1f}")

    #Dispersión de PS por tipo (1 decimal)
    ps_std_by_type = (
        df.groupby("Tipo 1")["PS"]
        .std()
        .round(1)
        .sort_values(ascending=False)
    )
    print("\nDesviación estándar de PS por Tipo:")
    print(ps_std_by_type)

    if mostrar_graficos:
        #Gráficos de visualización (ejemplo: histograma, scatter plot, etc.)
        plt.figure(figsize=(10, 6))
        sns.histplot(data=df, x='Ataque', kde=True)
        plt.title('Distribución de Ataque')
        plt.show()

        plt.figure(figsize=(10, 6))
        sns.scatterplot(data=df, x='Ataque', y='Velocidad')
        plt.title('Relación entre Ataque y Velocidad')
        plt.show()

    return df, stats_by_type, correlation, ps_std_by_type

if __name__ == '__main__':
    df, stats_by_type, correlation, ps_std_by_type = analisis_eda()