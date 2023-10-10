ventas_totales = 0
comisionestotales = 0


while True: 
    cedula = int(input("Ingrese su cedula: \nSi quiere salir del programa digita (-1):\n"))
    if cedula == -1:
        break
    nombre = input("Ingrese su nombre: ")
    tvendedor = int(input("Ingrese que tipo de vendedor es: \n1. Puerta a Puerta \n2. Telemercadeo \n3. Ejecutivo de venta \n- Opcion: "))
    nventas = int(input("Ingrese el numero de ventas: "))

    if tvendedor == 1:
      ventas_totales += nventas 
      comision = nventas * 0.2
      comisionestotales += comision
      print(f"El valor a pagar por comision es: {comision:,.2f}\n el precio mas la comision {nventas + comision}")
    elif tvendedor == 2:
      ventas_totales += nventas 
      comision = nventas * 0.15
      comisionestotales += comision
      print(f"El valor a pagar por comision es: {comision:,.2f}\n el precio mas la comision {nventas + comision}")
    else:
      
      ventas_totales += nventas 
      comision = nventas * 0.25
      comisionestotales += comision
      print(f"El valor a pagar por comision es: {comision:,.2f}\n el precio mas la comision {nventas + comision}")    


print(f"El valor total de las ventas es: ${ventas_totales:,.2f} \ny el valor a pagar de comisiones es: ${comisionestotales:,.2f}")
    
    
