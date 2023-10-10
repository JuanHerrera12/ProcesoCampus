def menu():
    while True:
        try:
            print("***MENU NOMINA***")
            print("1. Agregar empleado ")
            print("2. Modificar empleado")
            print("3. Buscar empleado")
            print("4. Eliminar empleado")
            print("5. Listar empleados")
            print("6. Listar nómina de un empleado")
            print("7. Listar nómina de todos los empleados")
            print("8. Salir")
        
            op = int(input("Opcion (1-8): "))
            if op <1 or op > 8:
                print("Opcion invalida. Escoja de 1 a 8")
                input("Presione cualquier tecla para continuar...")
                continue
            return op 
        except ValueError:
            print("Opcion invalida. Escoja de 1 a 8")
            input("Presione cualquier tecla para continuar... ")

def leerInt(msj):
    while True:
        try:
            n = int(input(msj))
            if n < 1:
                print("Valor invalido. Debe ser mayor a 0")
                continue
            return n
        except ValueError:
            print("Error al ingresar el numero")



def leerEmpleado(msj):
    while True:
        try:
            texto = input(msj)
            if len(texto):
                print("Recuerde que el texto no puede ir vacio")
                continue
            return texto
        except:
            print("Error.")

def leerInt2(msj):
    while True:
        try:
            n = int(input(msj))
            if n < 1 or n > 160:
                print("Valor invalido. Debe ser mayor a 0")
                continue
            return n
        except ValueError:
            print("error al ingresar el numero")     

def leerInt3(msj):
    while True:
        try:
            n = int(input(msj))
            if n < 8000 or n > 150000:
                print("Valor invalido. Debe ser mayor a 0")
                continue
            return n
        except ValueError:
            print("Error al ingresar el numero")  

        



### MENU PRINCIPAL
while True:
   opcion = menu()
   id = leerInt("Ingrese su id: ") 
   nombre = leerEmpleado("Ingrese su nombre: ")
   horas_t = leerInt2("Ingrese las horas trabajadas: ")
   valor_hora = leerInt3("Ingrese  el valor de la hora: ")
   if opcion == 1:
       print("\n\n 1. Agregar empleado")                                        