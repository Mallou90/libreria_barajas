# Empezamos por importar la clase Baraja desde el módulo barajas
from .barajas import Baraja
import random

class BarajaFrancesa(Baraja):
    def __init__(self):
        '''Inicializa una baraja francesa con 52 cartas.'''
        super().__init__()
        palos = ["corazones", "diamantes", "tréboles", "picas"]
        numeros = list(range(1, 11)) + ["J", "Q", "K"]  # 1-13 (As, 2-10, J, Q, K)
        self.cartas = [f"{numero} de {palo}" for palo in palos for numero in numeros]

    def tipo_baraja(self):
        '''Devuelve el tipo de baraja.'''
        return "Baraja Francesa"
    
    def __str__(self):
        '''Devuelve una representación en cadena de la baraja francesa.'''
        return f"Baraja Francesa con {self.cantidad_cartas} cartas: {', '.join(self.cartas)}"

    @property
    def cantidad_cartas(self):
        '''Devuelve la cantidad de cartas en la baraja francesa.'''
        return len(self.cartas)  # Siempre será 52
    
    def barajar(self):
        '''Baraja las cartas de la baraja.'''
        random.shuffle(self.cartas)

    def sacar_carta(self):
        '''Saca una carta de la baraja, la muestra y la elimina de la lista.'''
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

    def sacar_varias_cartas(self, cantidad=2):
        '''Saca varias cartas de la baraja, las muestra y las elimina de la lista. Por defecto extrae 2 cartas.'''
        if len(self.cartas) < cantidad:
            print("No hay suficientes cartas en la baraja.")
            return []
        cartas_sacadas = []
        for i in range(cantidad):
            carta = self.cartas.pop()
            cartas_sacadas.append(carta)
            print(f"Carta sacada: {carta}")
        return cartas_sacadas