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
            if 0 <= eleccion < 6 and tablero[f"jugador{jugador}"][eleccion] > 0:
                return eleccion
            else:
                print("Elección no válida. Inténtalo de nuevo.")
        except ValueError:
            print("Por favor, ingresa un número válido.")

def siguiente_pozo(posicion, jugador):
    if jugador == 1:
        if posicion == 5:
            return "almacen1"
        else:
            return posicion + 1
    else:
        if posicion == 0:
            return "almacen2"
        else:
            return posicion - 1

def mover_semillas(jugador, pozo, tablero):
    semillas = tablero[f"jugador{jugador}"][pozo]
    tablero[f"jugador{jugador}"][pozo] = 0
    posicion_actual = pozo
    while semillas > 0:
        posicion_actual = siguiente_pozo(posicion_actual, jugador)
        # Manejo de almacenes
        if posicion_actual == "almacen1":
            if jugador == 1:
                tablero["jugador1"][6] += 1
                semillas -= 1
                if semillas == 0:
                    return True  # Turno extra
            else:
                posicion_actual = 0  # Saltar el almacén del oponente
        elif posicion_actual == "almacen2":
            if jugador == 2:
                tablero["jugador2"][6] += 1
                semillas -= 1
                if semillas == 0:
                    return True  # Turno extra
            else:
                posicion_actual = 5  # Saltar el almacén del oponente
        # Repartir en los pozos
        else:
            if jugador == 1:
                tablero["jugador1"][posicion_actual] += 1
            else:
                tablero["jugador2"][posicion_actual] += 1
            semillas -= 1
    return False  # No hay turno extra

def verificar_ganador(tablero):
    if sum(tablero["jugador1"][:6]) == 0 or sum(tablero["jugador2"][:6]) == 0:
        tablero["jugador1"][6] += sum(tablero["jugador1"][:6])
        tablero["jugador2"][6] += sum(tablero["jugador2"][:6])
        print("\nJuego terminado.")
        print(f"Jugador 1 almacén: {tablero['jugador1'][6]}")
        print(f"Jugador 2 almacén: {tablero['jugador2'][6]}")
        if tablero["jugador1"][6] > tablero["jugador2"][6]:
            print("¡Jugador 1 gana!")
        elif tablero["jugador1"][6] < tablero["jugador2"][6]:
            print("¡Jugador 2 gana!")
        else:
            print("¡Es un empate!")
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
