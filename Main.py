#Main.py

#Tarea Pokemon

import pandas as pd
import os

#Importar funciones
from Filtrado_y_Seleccion import filtrar_pokemons_fuego
from Estadistica_descriptiva import estadisticas
from Visualizacion_de_Datos import visualizar_datos
from Poder_total import calcular_poder_total
from Agrupamiento_y_Analisis import estadisticas_alaisis
from Analisis_exploratorio import analisis_eda
from Interpretacion import interpretacion

#Función principal que contiene el menú
def main():
    while True:
        #Limpiar la pantalla de la consola
        os.system('cls' if os.name == 'nt' else 'clear')
        
        #Menú del programa
        print("****************************************************************************************")
        print("\n-----Tarea Pokemon Fundamentos de Data Science-----\n")
        print("------------- MENU -------------")
        print("\n\u27a4 [1] Filtrado y selección")
        print("\n\u27a4 [2] Estadística descriptiva básica")
        print("\n\u27a4 [3] Vizualización de datos")
        print("\n\u27a4 [4] Manipulacion de datos")
        print("\n\u27a4 [5] Agrupamiento y análisis por grupo")
        print("\n\u27a4 [6] Análisis exploratorio de datos (EDA)")
        print("\n\u27a4 [7] Ejercicios de interpretación de resultados")
        print("\n\u27a4 [8] Salir\n")
        print("****************************************************************************************")

        try:
            op = int(input("\u27a4 Digite la operación a realizar: "))
            
            if op == 1:
                print("------------------------------------------------------------------------------------")
                filtrar_pokemons_fuego() #Llamamos a la función del problema 1
                print("------------------------------------------------------------------------------------")
            
            elif op == 2:
                print("------------------------------------------------------------------------------------")
                estadisticas() #Llamamos a la función de estadísticas descriptivas del problema 2
                print("------------------------------------------------------------------------------------")
            
            elif op == 3:
                print("------------------------------------------------------------------------------------")
                visualizar_datos() #Llamamos a la función de visualización del problema 3
                print("------------------------------------------------------------------------------------")
            
            elif op == 4:
                print("------------------------------------------------------------------------------------")
                calcular_poder_total() #Llamamos a la función de manipular datos del problema 4
                print("------------------------------------------------------------------------------------")
            
            elif op == 5:
                print("------------------------------------------------------------------------------------")
                estadisticas_alaisis() #Llamamos a la función del problema 5
                print("------------------------------------------------------------------------------------")
            
            elif op == 6:
                print("------------------------------------------------------------------------------------")
                analisis_eda() #Llamamos a la función análisis eda del problema 6
                print("------------------------------------------------------------------------------------")

            elif op == 7:
                print("------------------------------------------------------------------------------------")
                interpretacion() #Llamamos a la función interpretacion del problema 7
                print("------------------------------------------------------------------------------------")
            
            elif op == 8:
                print("\n****Gracias por utilizar****")
                break
            while True:
                opcion = input("\n\u27a4¿Desea Realizar otra operacion? (Y=si/N=no): ").upper()
                if opcion == 'N':
                    print("\n****Gracias por utilizar****")
                    return 
                elif opcion == 'Y':
                    break
                else:
                    print("Operacion invalida.")

        except ValueError:
            print("\n*** Opcion invalida. Porfavor digite un numero ***\n")
            input("Presione Enter para continuar...")

#Ejecutamos la función principal
if __name__ == "__main__":
    main()