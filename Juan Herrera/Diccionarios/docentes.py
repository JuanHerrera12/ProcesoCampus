n = int(input("Cantidad de docentes:"))
dicCategoria = {1:25000, 2:30000, 3:40000, 4:45000, 5:60000}

dicDocentes = {}
totalHonorarios =  0

for i in range(1, n+1):
    print("\nDatos del docente#", i)
    datDocentes = {}
    ced = input("Cedula: ")
    datDocentes["nombre"] = input("Nombre: ")
    datDocentes["categoria"] = int(input("Categoria (1-5): "))
    datDocentes["horas_hab"] = int(input("Horas Laboradas"))
    datDocentes["honorarios"] = dicCategoria.get(datDocentes["categoria"], 0) 
    datDocentes["horas_hab"]

    totalHonorarios += datDocentes["honorarios"]

    dicDocentes[ced] + datDocentes



print("\n\n", "=" * 30)
print("INFORME") 
print("\n\n" "=" * 30)
print("NOMBRE\t\tHONORARIOS")
print("=" * 30) 

for k, v in dicDocentes.items():
    print(f'{v["nombre"]}\t\t{v["honorarios"]:,}')

print("\n", "-" * 30)

