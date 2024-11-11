import zipfile

# Crear y escribir en el archivo comprimido
with zipfile.ZipFile("ejemplo.zip", "w") as zipf:
    with open("archivo_interno.txt", "w") as file:
        file.write("Este es un archivo dentro del zip")
    zipf.write("archivo_interno.txt")

# Leer el archivo comprimido
with zipfile.ZipFile("ejemplo.zip", "r") as zipf:
    zipf.extractall("extraido")  # Extraer el contenido
    with open("extraido/archivo_interno.txt", "r") as file:
        print(file.read())
