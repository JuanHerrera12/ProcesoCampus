archivo = open("/home/spukN01-020/Desktop/ProcesoCampus-1/Archivos/nombres.txt", "r")

texto = archivo.read()

print(texto)

print()

archivo.seek(0)
texto2 = archivo.readline()
print(texto2)

texto3 = archivo.readlines()
print(texto3)

archivo.close