import sys

arch_csv_ej2 = r"C:/Users/jose_/Escritorio/Python-Prep/M10_manejodearchivos/Archivos Homework M10/clase10_ej2_hw.csv"

try:
    import datetime
    import os

    tiempo = datetime.datetime.now()
    tiempo = int(datetime.datetime.timestamp(tiempo))

    temper = input("¿Cuantos °C tenemos de temperatura?: ")
    humedad = input("¿Cual es el nivel de humedad (en %)?: ")
    # lluvia = sys.argv[0]
    lluvia = input("¿Está lloviendo? (Sí=True,No=False): ")
    # linea = 'timestamp' + "," + 'temperatura' + "," + 'humedad' + "," + 'lluvia'
    linea = str(tiempo) + "," + temper + "," + humedad + "," + lluvia

    logs_lluvia = open(arch_csv_ej2,"a",)
    logs_lluvia.write(linea + "\n")
    logs_lluvia.close()

except:
    print("ERROR: Introdujo una cantidad de argumentos distinta de tres (3)")
    print("Ejemplo: clase09_ej1.py <temperatura> <humedad> <True o False>")
