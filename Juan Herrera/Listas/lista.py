milista= [] #lista vacia
milista2 = list() # lista vacia  


nombreCampers = ["Juan",  "Yulieth", "Lorenzo", "Manuel", "David"]
print(nombreCampers)
print(nombreCampers[1])
nombreCampers[1] ="Julieth"



#slices
print(nombreCampers[2:4])
print(nombreCampers[::-1]) #orden de ultimo a primero

nombreCampers_juan = ["Daniela", "Maria", "Juliana", "Sandra", "Carolina"]
print(nombreCampers_juan)
# nombreCampers += nombreCampers_juan
# print(nombreCampers)

#metodos de listas
nombreCampers.append("Kevin")  #con append kevin se agrega al final de la lista
print(nombreCampers) 

nombreCampers.extend(nombreCampers_juan) #con extend se agrega elemento de una lista a otra 
print(nombreCampers)
print(nombreCampers[-1])

nombreCampers.insert(1, "Carlos") #El insert me permite insertar en cualquier posicion
print(nombreCampers)

nombreCampers.pop() #el pop sirve opara eliminar(si no se coloca nada se elimina el ultimo elemnto, si no se coloca la poscion el cual desea eliminar)
print(nombreCampers)

nombreCampers.pop(-3)
print(nombreCampers)

nombreCampers.remove("Sandra") #remove nos pide el elemento a eliminar
print(nombreCampers)


# list2 = [0,1,15,"115"]
# list2.sort()
# list

nombreCampers.sort(reverse= True) #ordenar de forma descendente 
print(nombreCampers)