#TRABAJO PRACTICO DE REPETITIVAS, CONDICIONALES Y SECUENCIALES
#ALUMNO: JORGE MONJE PACHECO
print("EJERCICIO 2")
## EJERCICIO 2
#2)Acceso al Campus y Menú Seguro

USUARIO = "alumno"                                       
CLAVE = "python123"
intentos_max = 3
acceso = False


for i in range(1, intentos_max + 1):                                      #Ingreso de usuario y clave
    print(f"Intento {i}/{intentos_max}")
    usuario_input = input("Usuario: ")
    clave_input = input("Clave: ")

    if usuario_input == USUARIO and clave_input == CLAVE:
        print("Acceso permitido.")
        acceso = True
        break
    else:
        print("Error: credenciales inválidas.")


if not acceso:
    print("Cuenta bloqueada")
else:
    opcion = ""
    while opcion != "4":
        print("\n--- MENÚ CAMPUS TECNICATURA EN PROGRAMACION ---")                                 #parte del menu
        print("1) Ver estado de inscripción")
        print("2) Cambiar clave")
        print("3) Mensaje motivacional")
        print("4) Salir")
        
        opcion = input("Opción: ")

                                                                   # Validación de que sea un numero
        if not opcion.isdigit():
            print("Error: ingrese un número válido.")
            continue
    
                                                                    # Validación: ¿Está entre 1 y 4?
        if int(opcion) < 1 or int(opcion) > 4:
            print("Error: opción fuera de rango.")
            continue

                                                                     # Acciones al ingresar 1, 2, 3 o 4
        if opcion == "1":
            print("Estado: Inscripto")
            
        elif opcion == "2":                                           #cambio de clave
            nueva_clave = input("Nueva clave: ")
            # Validación de longitud
            if len(nueva_clave) < 6:
                print("Error: mínimo 6 caracteres.")
            else:
                confirmacion = input("Confirme nueva clave: ")
                if nueva_clave == confirmacion:
                    CLAVE = nueva_clave
                    print("Clave cambiada con éxito.")
                else:
                    print("Error: las claves no coinciden.")
                    
        elif opcion == "3":
            print("Mensaje: 'Dale que mañana sale el sol!'")
            
        elif opcion == "4":
            print("Saliendo del sistema...")