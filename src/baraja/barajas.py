# En este archivo vamos a definir la clase Baraja
import random

class Baraja:
    def __init__(self):
        '''Inicializa una baraja vacía.'''
        self.cartas = [] # Lista para almacenar las cartas de la baraja

    # Propiedades de la clase Baraja
    @property
    def carta_elegida(self):
        '''Devuelve una carta al azar de la baraja o None si está vacía.'''
        if self.cartas:
            return random.choice(self.cartas)
        return None
    def tipo_baraja(self):
        '''Método abstracto que debe ser implementado por las subclases.'''
        return None
    @property
    def cantidad_cartas(self):
        '''Devuelve la cantidad de cartas en la baraja.'''
        return len(self.cartas)