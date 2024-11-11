import json

# Escribir en el archivo JSON
datos_json = {"nombre": "Lucía", "edad": 27, "ciudad": "Madrid"}
with open("ejemplo.json", "w") as file:
    json.dump(datos_json, file)

# Leer el archivo JSON
with open("ejemplo.json", "r") as file:
    contenido_json = json.load(file)
    print(contenido_json)

