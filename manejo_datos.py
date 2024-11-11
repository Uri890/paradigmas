import csv

# Escribir en el archivo CSV
with open("ejemplo.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Nombre", "Edad"])
    writer.writerow(["Carlos", 28])
    writer.writerow(["María", 22])

# Leer el archivo CSV
with open("ejemplo.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
