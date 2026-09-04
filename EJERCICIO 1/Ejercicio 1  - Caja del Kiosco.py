#TRABAJO PRACTICO DE REPETITIVAS, CONDICIONALES Y SECUENCIALES
#ALUMNO: JORGE MONJE PACHECO

print("EJERCICIO 1")
## EJERCICIO 1
#1) "Caja del Kiosco"

nombre = input("Ingrese el nombre del cliente: ")                          #en este paso ingreso nombre
while not nombre.isalpha():                                                #valido solo letras y que no este vacio
    print("Error: El nombre debe contener solo letras y no estar vacío.")
    nombre = input("Ingrese el nombre del cliente: ")

cantidad_str = input("Cantidad de productos a comprar: ")                  #en este paso ingreso cantidad de productos a comprar
while not cantidad_str.isdigit() or int(cantidad_str) <= 0:                #valido numero entero positivo
    print("Error: Ingrese un número entero positivo mayor a 0.")
    cantidad_str = input("Cantidad de productos a comprar: ")

cantidad = int(cantidad_str)

total_sin_descuento = 0
total_con_descuento = 0


for i in range(1, cantidad + 1):                                            #cargo el producto, 
    # Pedir precio
    precio_str = input(f"Producto {i} - Precio: ")                           #ingresa precio
    while not precio_str.isdigit():                                          #valido numero positivo
        print("Error: El precio debe ser un número entero.")
        precio_str = input(f"Producto {i} - Precio: ")
    precio = int(precio_str)

    total_sin_descuento += precio
    tiene_descuento = input("¿Tiene descuento? (S/N): ").lower()              #descuento si o no #convierte a mayuscula
    while tiene_descuento not in ['s', 'n']:
        print("Error: Ingrese 'S' para sí o 'N' para no.")
        tiene_descuento = input("¿Tiene descuento? (S/N): ").lower()
    
    if tiene_descuento == 's':                                                 #en caso de que tenga descuento
        precio_final = precio * 0.90                                           # Aplica el 10% de descuento
    else:
        precio_final = precio
        
    total_con_descuento += precio_final


ahorro = total_sin_descuento - total_con_descuento                             #punto 4 mostrar
promedio = total_con_descuento / cantidad

print("-" * 30)                                                                #hace 30 guion Bajo
print(f"Cliente: {nombre}")
print(f"Cantidad de productos: {cantidad}")
print(f"Total sin descuentos: ${total_sin_descuento}")
print(f"Total con descuentos: ${total_con_descuento:.2f}")
print(f"Ahorro: ${ahorro:.2f}")
print(f"Promedio por producto: ${promedio:.2f}")


