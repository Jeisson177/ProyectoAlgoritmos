class Tablero:
    def __init__(self):
        self.jugadores = {
            "jugador1": [4, 4, 4, 4, 4, 4, 0],
            "jugador2": [4, 4, 4, 4, 4, 4, 0]
        }
    
    def mostrar(self):
        print("\n  Jugador 2")
        print("   ", self.jugadores["jugador2"][:6][::-1])
        print(" ", self.jugadores["jugador2"][6], "               ", self.jugadores["jugador1"][6])
        print("   ", self.jugadores["jugador1"][:6])  
        print("  Jugador 1\n")
    
    def obtener_semillas(self, jugador, pozo):
        return self.jugadores[f"jugador{jugador}"][pozo]
    
    def vaciar_pozo(self, jugador, pozo):
        semillas = self.jugadores[f"jugador{jugador}"][pozo]
        self.jugadores[f"jugador{jugador}"][pozo] = 0
        return semillas
    
    def agregar_semilla(self, jugador, posicion):
        if posicion == 6:  # Almacén
            self.jugadores[f"jugador{jugador}"][6] += 1
        else:
            self.jugadores[f"jugador{jugador}"][posicion] += 1
    
    def verificar_fila_vacia(self, jugador):
        return sum(self.jugadores[f"jugador{jugador}"][:6]) == 0
    
    def finalizar_juego(self):
        for jugador in ["jugador1", "jugador2"]:
            self.jugadores[jugador][6] += sum(self.jugadores[jugador][:6])
            self.jugadores[jugador][:6] = [0, 0, 0, 0, 0, 0]
    
    def obtener_almacen(self, jugador):
        return self.jugadores[f"jugador{jugador}"][6]