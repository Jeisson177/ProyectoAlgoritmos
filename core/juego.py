from core.tablero import Tablero
from core.jugador import Jugador

class JuegoMancala:
    def __init__(self):
        self.tablero = Tablero()
        self.jugador_actual = 1
        self.jugadores = {
            1: Jugador(1),
            2: Jugador(2)
        }
    
    def mover_semillas(self, jugador, pozo):
        semillas = self.tablero.vaciar_pozo(jugador, pozo)
        posicion_actual = pozo
        turno_extra = False
        
        while semillas > 0:
            posicion_actual += 1
            
            if jugador == 1:
                if posicion_actual == 6:
                    self.tablero.agregar_semilla(1, 6)
                    semillas -= 1
                    if semillas == 0:
                        turno_extra = True
                        break
                    else:
                        posicion_actual = -1
                        continue
                
                if posicion_actual == -1:
                    posicion_actual = 0
                    jugador = 2
                    continue
                
                self.tablero.agregar_semilla(1, posicion_actual)
            
            elif jugador == 2:
                if posicion_actual == 6:
                    self.tablero.agregar_semilla(2, 6)
                    semillas -= 1
                    if semillas == 0:
                        turno_extra = True
                        break
                    else:
                        posicion_actual = -1
                        continue
                
                if posicion_actual == -1:
                    posicion_actual = 0
                    jugador = 1
                    continue
                
                self.tablero.agregar_semilla(2, posicion_actual)
            
            semillas -= 1
        
        return turno_extra
    
    def verificar_ganador(self):
        if self.tablero.verificar_fila_vacia(1) or self.tablero.verificar_fila_vacia(2):
            self.tablero.finalizar_juego()
            self.tablero.mostrar()
            
            print("\n Juego terminado.")
            print(f"Jugador 1 almacén: {self.tablero.obtener_almacen(1)}")
            print(f"Jugador 2 almacén: {self.tablero.obtener_almacen(2)}")
            
            if self.tablero.obtener_almacen(1) > self.tablero.obtener_almacen(2):
                print("¡Jugador 1 gana!")
            elif self.tablero.obtener_almacen(1) < self.tablero.obtener_almacen(2):
                print("¡Jugador 2 gana!")
            else:
                print("¡Es un empate!")
            
            return True
        return False
    
    def cambiar_turno(self):
        self.jugador_actual = 2 if self.jugador_actual == 1 else 1
    
    def jugar(self):
        while True:
            self.tablero.mostrar()
            
            jugador = self.jugadores[self.jugador_actual]
            pozo_elegido = jugador.elegir_pozo(self.tablero)
            turno_extra = self.mover_semillas(self.jugador_actual, pozo_elegido)
            
            if self.verificar_ganador():
                break
            
            if not turno_extra:
                self.cambiar_turno()
