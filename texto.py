# Escritura inicial en el archivo
with open("texto_ejemplo.txt", "w") as archivo:
    archivo.write("Primera línea de texto.\n")
    archivo.write("Segunda línea de texto.\n")

# Lectura del archivo
with open("texto_ejemplo.txt", "r") as archivo:
    contenido = archivo.read()
    print("Contenido después de la primera escritura:\n", contenido)

# Agregar más texto
with open("texto_ejemplo.txt", "a") as archivo:
    archivo.write("Línea adicional de texto.\n")

# Lectura del archivo después de agregar texto
with open("texto_ejemplo.txt", "r") as archivo:
    contenido = archivo.read()
    print("Contenido después de agregar texto:\n", contenido)
