# Crear un script con el nombre "clase09_ej1.py" que reciba 3 parametros a elección,
# verificando que sean exactamente esa cantidad, y muestre como salida los parámetros recibidos

import sys

if len(sys.argv)>1:
    print(f"El primer elemento es {sys.argv[0]}")
else:
    print(f'La lista no tiene más de {len(sys.argv)} elementos.')
