#TRABAJO PRACTICO DE REPETITIVAS, CONDICIONALES Y SECUENCIALES
#ALUMNO: JORGE MONJE PACHECO
print("EJERCICIO 2")
## EJERCICIO 3
#3)Agenda de Turnos con Nombres (sin listas)

# variables
lunes1 = ""; lunes2 = ""; lunes3 = ""; lunes4 = ""                      #lunes 4 turnos martes 3 turnos
martes1 = ""; martes2 = ""; martes3 = ""

                                                                          # --- 2. Ingreso del Operador ---                                    
operador = input("Nombre del operador: ")
while not operador.isalpha():                                                 #.isalpha verifica caracteres alfabeticos
    print("Error: El nombre debe contener solo letras.")
    operador = input("Nombre del operador: ")

                                                # ---. Menú Principal ---
opcion = ""
while opcion != "5":
    print(f"\n--- SISTEMA DE TURNOS (Op: {operador}) ---")
    print("1. Reservar turno")
    print("2. Cancelar turno")
    print("3. Ver agenda del día")
    print("4. Ver resumen general")
    print("5. Cerrar sistema")
    
    opcion = input("Seleccione una opción: ")
    
    if not opcion.isdigit():                                      #solo digitos del 0 al 9
        print("Error: Ingrese un número.")
        continue

                                        # --- OPCIÓN 1: RESERVAR ---
    if opcion == "1":
        dia = input("Elija día (1=Lunes, 2=Martes): ")
        if dia == "1":
            nombre = input("Nombre del paciente: ")
            while not nombre.isalpha():                                   #verifico que el texto sea solo letras
                nombre = input("Error (solo letras). Nombre: ")
            
                                                # Verificar si ya existe el nombre en el listado el dia Lunes
            if nombre == lunes1 or nombre == lunes2 or nombre == lunes3 or nombre == lunes4:
                print("Error: El paciente ya tiene un turno este día.")
                                                                                  # Buscar lugar libre
            elif lunes1 == "": lunes1 = nombre; print("Turno asignado en Lunes 1")
            elif lunes2 == "": lunes2 = nombre; print("Turno asignado en Lunes 2")
            elif lunes3 == "": lunes3 = nombre; print("Turno asignado en Lunes 3")
            elif lunes4 == "": lunes4 = nombre; print("Turno asignado en Lunes 4")
            else: print("Sin cupos para el Lunes.")
            
        elif dia == "2":
            nombre = input("Nombre del paciente: ")
            while not nombre.isalpha():                                       #verifico que el texto sea solo letras
                nombre = input("Error (solo letras). Nombre: ")
                
            if nombre == martes1 or nombre == martes2 or nombre == martes3:
                print("Error: El paciente ya tiene un turno este día.")
            elif martes1 == "": martes1 = nombre; print("Turno asignado en Martes 1")
            elif martes2 == "": martes2 = nombre; print("Turno asignado en Martes 2")
            elif martes3 == "": martes3 = nombre; print("Turno asignado en Martes 3")
            else: print("Sin cupos para el Martes.")
        else:
            print("Día inválido.")

                                                                # --- OPCIÓN 2: CANCELAR ---
    elif opcion == "2":
        dia = input("Elija día para cancelar (1 o 2): ")
        nombre = input("Nombre del paciente a cancelar: ")
        
        encontrado = False
        if dia == "1":
            if lunes1 == nombre: lunes1 = ""; encontrado = True
            elif lunes2 == nombre: lunes2 = ""; encontrado = True
            elif lunes3 == nombre: lunes3 = ""; encontrado = True
            elif lunes4 == nombre: lunes4 = ""; encontrado = True
        elif dia == "2":
            if martes1 == nombre: martes1 = ""; encontrado = True
            elif martes2 == nombre: martes2 = ""; encontrado = True
            elif martes3 == nombre: martes3 = ""; encontrado = True
            
        if encontrado: print("Turno cancelado con éxito.")
        else: print("No se encontró al paciente.")

                                               # --- OPCIÓN 3: VER AGENDA ---
    elif opcion == "3":
        dia = input("Ver agenda de (1=Lunes, 2=Martes): ")
        if dia == "1":
            print(f"L1: {lunes1 if lunes1 != '' else '(libre)'}")
            print(f"L2: {lunes2 if lunes2 != '' else '(libre)'}")
            print(f"L3: {lunes3 if lunes3 != '' else '(libre)'}")
            print(f"L4: {lunes4 if lunes4 != '' else '(libre)'}")
        elif dia == "2":
            print(f"M1: {martes1 if martes1 != '' else '(libre)'}")
            print(f"M2: {martes2 if martes2 != '' else '(libre)'}")
            print(f"M3: {martes3 if martes3 != '' else '(libre)'}")

                                       # --- OPCIÓN 4: RESUMEN GENERAL ---
    elif opcion == "4":
                                        # Contar el dia lunes ocupados
        occ_l = 0
        if lunes1 != "": occ_l += 1
        if lunes2 != "": occ_l += 1
        if lunes3 != "": occ_l += 1
        if lunes4 != "": occ_l += 1
        
                                        # Contar el dia martes ocupados
        occ_m = 0
        if martes1 != "": occ_m += 1
        if martes2 != "": occ_m += 1
        if martes3 != "": occ_m += 1
        
        print(f"Lunes: {occ_l} ocupados, {4 - occ_l} libres.")
        print(f"Martes: {occ_m} ocupados, {3 - occ_m} libres.")
        
        if occ_l > occ_m: print("Día con más turnos: Lunes")
        elif occ_m > occ_l: print("Día con más turnos: Martes")
        else: print("Empate en cantidad de turnos.")

print("Sistema cerrado. ¡Hasta Luego!")