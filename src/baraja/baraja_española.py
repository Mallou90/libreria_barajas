# Empezamos por importar la clase Baraja desde el módulo barajas
from .barajas import Baraja
import random

class BarajaEspañola(Baraja):
    def __init__(self):
        '''Inicializa una baraja española con 40 cartas.'''
        super().__init__()
        palos = ["oros", "copas", "espadas", "bastos"]
        numeros = list(range(1, 8)) + ['sota', 'caballo', 'rey']  # 1-7 y 10-12 (Sota, Caballo, Rey)
        self.cartas = [f"{numero} de {palo}" for palo in palos for numero in numeros]

    def tipo_baraja(self):
        '''Devuelve el tipo de baraja.'''
        return "Baraja Española"
    
    def __str__(self):
        '''Devuelve una representación en cadena de la baraja española.'''
        return f"Baraja Española con {self.cantidad_cartas} cartas: {', '.join(self.cartas)}"

    @property
    def cantidad_cartas(self) -> int:
        '''Devuelve la cantidad de cartas en la baraja española.'''
        return len(self.cartas)  # Siempre será 40

# Vamos a añadir algún método, como barajar las cartas, sacar una carta o reiniciar la baraja

    def barajar(self):
        '''Baraja las cartas de la baraja.'''
        random.shuffle(self.cartas)

    def sacar_carta(self):
        '''Saca una carta de la baraja y la elimina de la lista.'''
        if self.cartas:
            carta = self.cartas.pop()
            print(f"Carta sacada: {carta}")                
            return carta
        print("No quedan cartas en la baraja.")
        return None

    def reiniciar(self):
        '''Reinicia la baraja con las cartas originales ordenadas.'''
        palos = ["oros", "copas", "espadas", "bastos"]
        numeros = list(range(1, 8)) + list(range(10, 13))
        self.cartas = [f"{numero} de {palo}" for palo in palos for numero in numeros]

    def sacar_varias_cartas(self, cantidad=5):
        '''Saca varias cartas de la baraja, las muestra y las elimina de la lista.'''
        if len(self.cartas) < cantidad:
            print("No hay suficientes cartas en la baraja.")
            return []
        cartas_sacadas = []
        for i in range(cantidad):
            carta = self.cartas.pop()
            cartas_sacadas.append(carta)
            print(f"Carta sacada: {carta}")
        return cartas_sacadas