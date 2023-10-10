cantidad = float(input("Precio:"))
iva = float(input("Cuanto es el impuesto a aplicar: "))


def factura(precio, iva = 19 ):
    return ((precio / 100) * iva) + precio

print (factura(cantidad, iva))
print(factura(cantidad))








def descuento(valArticulo):
     if valArticulo > 150000:
         d = valArticulo * 0.05
     else:
         d = 0
     return d
    
    
valor = int(input("Ingrese el valor del articulo : "))
d = descuento(valor)
print(f"El valor del descuento es de: {d:,}")
