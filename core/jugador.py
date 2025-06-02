class Jugador:
    def __init__(self, numero, tipo='humano'):
        self.numero = numero
        self.tipo = tipo  # 'humano' o 'automático'
    
    def elegir_pozo(self, tablero):
        if self.tipo == 'humano':
            return self._elegir_pozo_humano(tablero)
        else:
            return self._elegir_pozo_automatico(tablero)
    
    def _elegir_pozo_humano(self, tablero):
        while True:
            try:
                eleccion = int(input(f"Jugador {self.numero}, elige un pozo (1-6): ")) - 1
                if 0 <= eleccion < 6:
                    if tablero.obtener_semillas(self.numero, eleccion) > 0:
                        return eleccion
                    else:
                        print("⚠️ Error: El pozo está vacío. Elige otro pozo.")
                else:
                    print("⚠️ Error: Debes elegir un número del 1 al 6.")
            except ValueError:
                print("⚠️ Error: Por favor, ingresa un número válido (1-6).")
    
    def _elegir_pozo_automatico(self, tablero):
        # Estrategia simple: elige el pozo con más semillas
        max_semillas = -1
        mejor_pozo = 0
        for pozo in range(6):
            semillas = tablero.obtener_semillas(self.numero, pozo)
            if semillas > max_semillas:
                max_semillas = semillas
                mejor_pozo = pozo
        return mejor_pozo