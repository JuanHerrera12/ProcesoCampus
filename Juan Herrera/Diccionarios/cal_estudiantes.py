bandera = 0
dicEscuela = {}
while True:
    if bandera == 0: 
        datEstudiantes = {}
        codigo = int(input("Codigo: "))
        if codigo == 999:
            break
        else: 
            datEstudiantes["nombre"] = input("Nombre: ")
            datEstudiantes["Nota #1"] = float(input("Nota 1 (0-5.0): "))
            datEstudiantes["Nota #2"] = float(input("Nota 2 (0-5.0): "))
            datEstudiantes["Nota #3"] = float(input("Nota 3 (0-5.0): "))
    
        dicEscuela[codigo] = datEstudiantes    



def calPromedio(Nota1 , Nota2, Nota3):
    promedio = (Nota1 * 0.3) + (Nota2 * 0.3) + (Nota3 * 0.4) 
    return promedio
    

for c, D in dicEscuela.items():
    nota_1 = D["Nota #1"]
    nota_2 = D["Nota #2"]
    nota_3 = D["Nota #3"]
    notaFinal = calPromedio(nota_1, nota_2, nota_3)
    
    if notaFinal >= 3.0: 
        print(f'{D["nombre"]} Aprobo la materia con una nota de: {notaFinal:.1f}')

    else: 
        print(f'{D["nombre"]} su nota fue: {notaFinal:.1f} No aprobo, siga intentado')


  


 