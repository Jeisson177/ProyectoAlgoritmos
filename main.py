def inicializar_tablero():
    # Cada jugador tiene 6 pozos con 4 semillas y un almacén
    return {
        "jugador1": [4, 4, 4, 4, 4, 4, 0],  # Los 6 pozos y el almacén (último índice)
        "jugador2": [4, 4, 4, 4, 4, 4, 0]   # Los 6 pozos y el almacén (último índice)
    }

def mostrar_tablero(tablero):
    print("\n  Jugador 2")
    print("   ", tablero["jugador2"][:6][::-1])  # Se muestra en orden inverso
    print(" ", tablero["jugador2"][6], "               ", tablero["jugador1"][6])  # Almacenes
    print("   ", tablero["jugador1"][:6])  
    print("  Jugador 1\n")

def elegir_pozo(jugador, tablero):
    while True:
        try:
            eleccion = int(input(f"Jugador {jugador}, elige un pozo (1-6): ")) - 1
            if 0 <= eleccion < 6:
                if tablero[f"jugador{jugador}"][eleccion] > 0:
                    return eleccion
                else:
                    print("⚠️ Error: El pozo está vacío. Elige otro pozo.")
            else:
                print("⚠️ Error: Debes elegir un número del 1 al 6.")
        except ValueError:
            print("⚠️ Error: Por favor, ingresa un número válido (1-6).")

def mover_semillas(jugador, pozo, tablero):
    semillas = tablero[f"jugador{jugador}"][pozo]
    tablero[f"jugador{jugador}"][pozo] = 0
    posicion_actual = pozo

    while semillas > 0:
        # Mover en el tablero del jugador actual
        if jugador == 1:
            posicion_actual += 1
            
            # Si llegamos al almacén del jugador 1
            if posicion_actual == 6:
                tablero["jugador1"][6] += 1
                semillas -= 1
                if semillas == 0:
                    return True  # Turno extra
                else:
                    posicion_actual = -1  # Cambiaremos a la fila superior

            # Si estamos en la fila superior (jugador 2)
            elif posicion_actual == -1:
                posicion_actual = 0
                jugador = 2

            else:
                tablero["jugador1"][posicion_actual] += 1
                semillas -= 1

        # Mover en el tablero del jugador 2
        elif jugador == 2:
            posicion_actual += 1

            # Si llegamos al almacén del jugador 2
            if posicion_actual == 6:
                tablero["jugador2"][6] += 1
                semillas -= 1
                if semillas == 0:
                    return True  # Turno extra
                else:
                    posicion_actual = -1  # Cambiaremos a la fila inferior
                
            # Si estamos en la fila inferior (jugador 1)
            elif posicion_actual == -1:
                posicion_actual = 0
                jugador = 1
            
            else:
                tablero["jugador2"][posicion_actual] += 1
                semillas -= 1
    
    return False  # No hay turno extra

def verificar_ganador(tablero):
    if sum(tablero["jugador1"][:6]) == 0 or sum(tablero["jugador2"][:6]) == 0:
        tablero["jugador1"][6] += sum(tablero["jugador1"][:6])
        tablero["jugador2"][6] += sum(tablero["jugador2"][:6])
        
        print("\n🎉 Juego terminado.")
        print(f"Jugador 1 almacén: {tablero['jugador1'][6]}")
        print(f"Jugador 2 almacén: {tablero['jugador2'][6]}")
        
        if tablero["jugador1"][6] > tablero["jugador2"][6]:
            print("🏆 ¡Jugador 1 gana!")
        elif tablero["jugador1"][6] < tablero["jugador2"][6]:
            print("🏆 ¡Jugador 2 gana!")
        else:
            print("🤝 ¡Es un empate!")
        
        return True
    return False

def jugar_mancala():
    tablero = inicializar_tablero()
    jugador_actual = 1
    
    while True:
        mostrar_tablero(tablero)
        
        pozo_elegido = elegir_pozo(jugador_actual, tablero)
        turno_extra = mover_semillas(jugador_actual, pozo_elegido, tablero)
        
        if verificar_ganador(tablero):
            break
        
        if not turno_extra:
            jugador_actual = 2 if jugador_actual == 1 else 1

if __name__ == "__main__":
    jugar_mancala()
