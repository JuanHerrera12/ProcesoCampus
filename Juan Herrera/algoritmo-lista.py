def findElementslistPos(lst, elem):
    #Funcion que busca un elemento en la lista
    #si lo encuentra devuelva
    #Si no lo encuentra devuelve -1
    for p in range(len(lst)):
        if elem == lst[p]:
            return p
        return -1
    
def exitElemList(lst, elem):
    # Funcion que busca un elemento en la lista
    # Si lo enceuntra devuelve True
    # Sino lo encuentra devuelve False

    for e in lst:
        if e == elem:
            return True
        return False   
        