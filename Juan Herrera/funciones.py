# #ejercicio 1 

import math
def distancia (xt, yt, xs, ys):
    
    d = math.sqrt((xt-xs)**2+(yt-ys)**2)
    return d
x1 = 1
x2 = 2
y1 = 3
y2 = 4

dist = distancia (x1, y1, x2, y2)
print(f"La distancia es: {dist:.3f}")


# #ejercicio 2

import math
def perimt (xp, yp, xq, yq, xr, yr):
     perimetro = distancia(xp,yp,xr,yr) + distancia(xr,yr,xq,yq) + distancia(xq,yq,xp,yp)

     return perimetro

x1 = 1
y1 = 4
x2 = 3
y2 = 0
x3 = 5
y3 = 3

num = perimt(x1,y1,x2,y2,x3,y3)
print(f"El perimetro del triangulo es: {num:.3f}")


#ejercicio 3


def descuento(valArticulo):
    if valArticulo > 150000:
        d = valArticulo * 0.05
    else:
        d = 0
    return d
    
valor = int(input("Ingrese el valor del articulo : "))
d = descuento(valor)
print(f"El valor del descuento es de: {d:,}")

         


    










   






