import os
from itertools import product

# Ruta del archivo
archivo_ruta = "iteracion.txt"

# Eliminar el archivo si existe
if os.path.exists(archivo_ruta):
    os.remove(archivo_ruta)

# Dígitos posibles (del 1 al 10)
digitos = "0123456789"

# Iteración sobre todas las combinaciones de 1 a 4 dígitos
for longitud in range(1, 5):
    for combinacion in product(digitos, repeat=longitud):
        # Convertir la combinación en una cadena de texto
        num_str = "".join(combinacion)
        
        # Concatenar la palabra "hola" con la combinación
        palabra = "laterrazadetegueste" + num_str
        
        # Abrir el archivo en modo de escritura
        with open(archivo_ruta, "a") as archivo:
            # Escribir la palabra en el archivo
            archivo.write(palabra + "\n")
