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


#Unción principal que contiene el menú
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
        print("\n\u27a4 [6] ")
        print("\n\u27a4 [7] ")
        print("\n\u27a4 [8] Terminar")
        print("\n****************************************************************************************")

        try:
            op = int(input("\nIngrese una opcion: "))
            
            if op < 1 or op > 8:
                print("\n*** Opcion invalida. Porfavor digite nuevamente ***\n")
                input("Presione Enter para continuar...")
                continue #Vuelve al inicio del bucle
            
            #Switch-case en Python (usamos un diccionario o if/elif/else)
            if op == 1:
                print("------------------------------------------------------------------------------------")
                filtrar_pokemons_fuego() #Llamamos a la función filtrar pokemons fuego del problema 1
                print("------------------------------------------------------------------------------------")
            
            elif op == 2:
                print("------------------------------------------------------------------------------------")
                estadisticas() #Llamamos a la función estadisticas del problema 2
                print("------------------------------------------------------------------------------------")
            elif op == 3:
                print("------------------------------------------------------------------------------------")
                visualizar_datos() #Llamamos a la función visualizar datos del problema 3
                print("------------------------------------------------------------------------------------")
            elif op == 4:
                print("------------------------------------------------------------------------------------")
                calcular_poder_total() #Llamamos a la función calcular poder total del problema 4
                print("------------------------------------------------------------------------------------")
            
            elif op == 5:
                print("------------------------------------------------------------------------------------")
                estadisticas_alaisis() #Llamamos a la función estadisticas por tipo del problema 5
                print("------------------------------------------------------------------------------------")
            
            elif op == 6:
                print("------------------------------------------------------------------------------------")
                 #Llamamos a la función del problema 6
                print("------------------------------------------------------------------------------------")

            elif op == 7:
                print("------------------------------------------------------------------------------------")
                 #Llamamos a la función del problema 7
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