def leerInt(msj):
    while True:
        try:
            n = int(input(msj))
            if n < 1:
                print("Valor invalido. Debe ser mayo a 0")
                continue
            return n
        except ValueError:
            print("error al ingresar el numero")
def leerTexto(msj):
    while True:
        try:
            texto = input(msj)
            if len(texto) < 1:
                print("Recuerde que el texto no pude ir vacio")
                continue
            return texto
        except ValueError:
            print("error.")
def leerFloat(msj):
    while True:
        try:
            n = float(input(msj))
            if n < 0:
                print("nota invalida. Debe ser mayor o igual a 0")
                continue
            return n
        except ValueError:
            print("error al ingresar el numero")

def leerNombre(msj):
    while True:
        try:
            nom = input(msj)
            nom = nom.strip()
            if len(nom) == 0 or not nom.isalnum():
                 print("Nombre inválido")
                 continue
            return nom
        except Exception as e:
             print("Error al ingresar el nombre.", e)    