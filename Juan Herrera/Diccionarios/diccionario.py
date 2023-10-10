empleado = {"Nombre": "Sergio Medina", "cargo": "progamador", "salario":400000}
print(empleado["cargo"])
print(empleado.get("cargo"))
# print(empleado["apellido"])
print(empleado.get("apellido", "llave no existe"))


empleado["sexo"] = "M"
print(empleado)

#Modificar un valor 
empleado["salario"] = 4500000
print(empleado)

#borrar una llave y su valor
del empleado["sexo"]
print(empleado)

#borrar todo el diccionario
# empleado = {}
# empleado.clear()
# del empleado 

oficina = empleado.copy() #copy sirve para que no se modifique el diccionario empleado
print(oficina)
oficina["salario"] = 5000000
print(oficina)
print(empleado)

#fromkeys
x = ('key1', 'key2', 'key3')
y = 0
thisdict = dict.fromkeys(x, y)
print(thisdict)

#items
print(empleado.items())

#keys
print(empleado.keys()) #devuelve las llaves del diccionario

#values
print(empleado.values())

#por
print(empleado.pop("salario")) #elimina la llave especifica
print(empleado)

#popitem
print(empleado.popitem())
print(empleado)

#setdefault
print(empleado.setdefault("Nombre", "Carlos"))
print(empleado.setdefault("Ciudad", "Bucaramanga"))