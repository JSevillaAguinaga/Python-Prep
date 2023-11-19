import sys
import os
import csv

from diccionario10_ej3_hw import montañas

list_keys = list(montañas.keys())
linea_cab = (
    list_keys[0]
    + ","
    + list_keys[1]
    + ","
    + list_keys[2]
    + ","
    + list_keys[3]
    + ","
    + list_keys[4]
)

def verificar_csv_vacio(nombre_csv):
    try:
        with open(nombre_csv, "r") as archivo_csv:
            lector_csv = csv.reader(archivo_csv)
            # Comprobar si el archivo está vacío
            if not any(lector_csv):
                return True
            else:
                return False
    except FileNotFoundError:
        print(f"El archivo {nombre_csv} no existe.")

arch_csv_mont = r"C:/Users/jose_/Escritorio/Python-Prep/M10_manejodearchivos/Archivos Homework M10/clase10_ej3_hw.csv"

if verificar_csv_vacio(arch_csv_mont) == True:
    logs_montaña = open(arch_csv_mont, "a", newline="", encoding="utf-8")
    logs_montaña.write(linea_cab + "\n")
    logs_montaña.close()

    logs_montaña = open(arch_csv_mont, "a", newline="", encoding="utf-8")
    for i in range(0, len(montañas["nombre"])):
        linea_data = (
            str(montañas["nombre"][i])
            + ","
            + str(montañas["orden"][i])
            + ","
            + str(montañas["pais"][i])
            + ","
            + str(montañas["cordillera"][i])
            + ","
            + str(montañas["altura"][i])
        )
        logs_montaña.write(linea_data + "\n")
    logs_montaña.close()

else:
    logs_montaña = open(arch_csv_mont, "a", newline="", encoding="utf-8")
    for i in range(0, len(montañas["nombre"])):
        linea_data = (
            str(montañas["nombre"][i])
            + ","
            + str(montañas["orden"][i])
            + ","
            + str(montañas["pais"][i])
            + ","
            + str(montañas["cordillera"][i])
            + ","
            + str(montañas["altura"][i])
        )
        logs_montaña.write(linea_data + "\n")
    logs_montaña.close()
    