#Ejercicio
#Hacer un programa que lea N estudiantes (nombre y nota). y nos muestre el promedio de la clase, el estudiante con menor 

# def leerInt(msj):
#     while True:
#         try:
#             n = int(input(msj))
#             if n < 1:
#                 print("Valor invalido . Debe ser mayor a cero")
#                 continue
#             return n
#         except ValueError:
#             print("Error al ingresar el numero. ")

#  def leerNombre(msj):
#     while True:
#       try:
#              nom = input(msj)
#             nom = nom.strip()
#              if len(nom) == 0 or not nom.isalnum():
#                  print("Nombre inválido")
#                  continue
#              return nom
#          except Exception as e:
#              print("Error al ingresar el nombre.", e)    

# def leerNota(msj):
#     while True:
#         try:
#             n = float(input(msj))
#             if n < 0:  
#              print("Error. Mayor a cero")
#              input("Presione cualquier tecla para continuar")
#              print("\n", "=" * 30 "\n") 
#              continue
#             return n 
#         except ValueError:
#             print("Error ")
#             input("Presione cualquier tecla para continuar")
#             print("\n", "=" * 30 "\n") 


# n = leerInt("Cuantos estudiantes son? ")
# lstNombres = []
# lstNotas = []
# for i in range(1, n+1):
#     print("\nDatos del estudiante #", i)
#     lstNombres.append (leerNombre("Nombre? "))
#     lstNotas.append(leerNota("Nota? "))

# prom = sum(lstNotas) / n 
# print("\n", "=" * 30)
# print("El promedio del curso es:" prom)






