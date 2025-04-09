class Jugador:
    def __init__(self, numero):
        self.numero = numero
    
    def elegir_pozo(self, tablero):
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