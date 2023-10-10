
def resultadoEstudiante(n1, n2, n3, n4, n5):
    promedio = (n1 + n2 + n3 + n4 + n5) / 5
    if promedio > 3.5:
       return True
    else:
       return False

n1 = float(input("Ingrese la nota: "))
n2 = float(input("Ingrese la nota: "))
n3 = float(input("Ingrese la nota: "))
n4 = float(input("Ingrese la nota: "))
n5 = float(input("Ingrese la nota: "))

if resultadoEstudiante(n1, n2, n3, n4, n5):
   print("Gano el año")
else: 
   print("Perdio el año")   

    

    
    
