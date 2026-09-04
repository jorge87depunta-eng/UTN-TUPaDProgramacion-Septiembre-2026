#TRABAJO PRACTICO DE REPETITIVAS, CONDICIONALES Y SECUENCIALES
#ALUMNO: JORGE MONJE PACHECO
print("EJERCICIO 2")
## EJERCICIO 5
#5)Escape Room"La Arena del Gladiador"

                                                                #Configuración del Personaje
nombre = input("Nombre del Gladiador: ")
while not nombre.isalpha():
    print("Error: Solo se permiten letras.")
    nombre = input("Nombre del Gladiador: ")

                                                                 # Inicialización de Estadísticas
vida_jugador = 100
vida_enemigo = 100
pociones = 3
ataque_pesado_base = 15
ataque_enemigo_base = 12
juego_activo = True                                               # Boolean para controlar el ciclo

print("\n=== INICIO DEL COMBATE ===")

                                                                  #Combate
while vida_jugador > 0 and vida_enemigo > 0:
    print(f"\n{nombre} (HP: {vida_jugador}) vs Enemigo (HP: {vida_enemigo}) | Pociones: {pociones}")
    print("Elige acción:")
    print("1. Ataque Pesado")
    print("2. Ráfaga Veloz")
    print("3. Curar")
    
    opcion = input("Opción: ")
    
                                                                            #Menú
    while not opcion.isdigit() or opcion not in ["1", "2", "3"]:
        print("Error: Ingrese un número válido (1, 2 o 3).")
        opcion = input("Opción: ")
    
                                                                       #Acciones del Jugador ---
    
    if opcion == "1":
        # Acción A: Ataque Pesado
        if vida_enemigo < 20:
            # Golpe Crítico (Uso de Float)
            danio_final = ataque_pesado_base * 1.5
            print(f"¡GOLPE CRÍTICO! Multiplicador 1.5x aplicado.")
        else:
            danio_final = float(ataque_pesado_base)
            
        vida_enemigo -= int(danio_final)
        print(f"¡Atacaste al enemigo por {danio_final} puntos de daño!")

    elif opcion == "2":
        # Acción B: Ráfaga Veloz (Uso de FOR)
        print(">> ¡Inicias una ráfaga de golpes!")
        for i in range(3):
            vida_enemigo -= 5
            print(" > Golpe conectado por 5 de daño")

    elif opcion == "3":                              # Acción C: Curar
                                                  
        if pociones > 0:
            vida_jugador += 30
            if vida_jugador > 100:                                 # Opcional: no pasar del máximo
                vida_jugador = 100
            pociones -= 1
            print(f"¡Usaste una poción! Recuperaste 30 HP. Vida actual: {vida_jugador}")
        else:
            print("¡No quedan pociones!")
                                                        # Pierde el turno

    # --- Turno del Enemigo ---
                                                         
    if vida_enemigo > 0:
        vida_jugador -= ataque_enemigo_base                  # Solo ataca si no ha muerto por el golpe del jugador
        print(f">> ¡El enemigo te atacó por {ataque_enemigo_base} puntos de daño!")

                                                     #Fin del Juego
print("\n" + "="*30)
if vida_jugador > 0:
    print(f"¡VICTORIA! {nombre} ha ganado la batalla.")
else:
    print("DERROTA. Has caido en combate.")