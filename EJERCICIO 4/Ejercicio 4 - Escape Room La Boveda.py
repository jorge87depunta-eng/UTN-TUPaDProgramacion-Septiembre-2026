#TRABAJO PRACTICO DE REPETITIVAS, CONDICIONALES Y SECUENCIALES
#ALUMNO: JORGE MONJE PACHECO
print("EJERCICIO 2")
## EJERCICIO 4
#4)"Escape Room: La Bóveda"

                                         # --- Variables iniciales ---
energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
racha_forzar = 0  # Contador para la regla anti-spam

                                                        # --- Ingreso del agente ---
agente = input("Nombre del agente: ")
while not agente.isalpha():                                 #verifico que el texto sea solo letras
    print("Error: El nombre debe contener solo letras.")
    agente = input("Nombre del agente: ")

print(f"\nBienvenido Agente {agente}. La bóveda te espera.")

                                                              # bucle Principal del Juego ---
while cerraduras_abiertas < 3 and energia > 0 and tiempo > 0:
                                                                    # Verificación de bloqueo por alarma
    if alarma and tiempo <= 3:
        print("\n¡SISTEMA BLOQUEADO! La alarma y el poco tiempo sellaron la bóveda.")
        break

    print("-" * 30)
    print(f"ESTADO: Energía: {energia} | Tiempo: {tiempo} | Cerraduras: {cerraduras_abiertas}/3")
    print(f"Alarma: {'ENCENDIDA' if alarma else 'Apagada'}")
    print("-" * 30)                                     #imprime 30 guin bajos para separar secciones
    
    print("1. Forzar cerradura (-20 energía, -2 tiempo)")
    print("2. Descifrar código (-10 energía, -3 tiempo)")
    print("3. Descansar (+15 energía, -1 tiempo)")
    
    opcion = input("Elija una acción: ")
    while not opcion.isdigit() or opcion not in ["1", "2", "3"]:            #verifico que la opcion sea numero
        opcion = input("Opción inválida. Elija 1, 2 o 3: ")

                                                               
    if opcion == "1":
                                            # Aplicamos costos
        energia -= 20
        tiempo -= 2
        racha_forzar += 1
        
                                                                # Regla Anti-Spam
        if racha_forzar >= 3:
            alarma = True
            print("¡CRÍTICO! La cerradura se trabó y sonó la ALARMA.")
        else:
            cerraduras_abiertas += 1
            print("¡Éxito! Forzaste la cerradura.")

    elif opcion == "2":
        racha_forzar = 0  # Corta la racha
        energia -= 10
        tiempo -= 3
        cerraduras_abiertas += 1
        print("Código descifrado. Una cerradura más abierta.")

    elif opcion == "3":
        racha_forzar = 0  # Corta la racha
        tiempo -= 1
        recuperacion = 15
        
        if alarma:
            print("Descansar con la alarma sonando es difícil... (-10 energía extra)")
            recuperacion -= 10
            
        energia += recuperacion
        if energia > 100:
            energia = 100
        print(f"Descansaste. Energía actual: {energia}")

                                                             # --- Condiciones de Fin de Juego ---
print("\n" + "="*30)
if cerraduras_abiertas == 3:
    print(f"¡VICTORIA! El agente {agente} abrió la bóveda.")
elif energia <= 0:
    print("DERROTA: Te quedaste sin energía.")
elif tiempo <= 0:
    print("DERROTA: Se terminó el tiempo.")
else:
    print("fin del juego.")