# En este archivo vamos a definir la clase Baraja
from abc import ABC, abstractmethod

class Baraja(ABC):
    def __init__(self):
        '''Inicializa una baraja vacía.'''
        self.cartas = []

    @abstractmethod
    def tipo_baraja(self) -> str:
        '''Método abstracto que debe ser implementado por las subclases.'''
        pass

    @property
    def cantidad_cartas(self) -> int:
        '''Devuelve la cantidad de cartas en la baraja.'''
        return len(self.cartas)
# En este archivo vamos a definir la clase Baraja
from abc import ABC, abstractmethod

class Baraja(ABC):
    def __init__(self):
        '''Inicializa una baraja vacía.'''
        self.cartas = []

    @abstractmethod
    def tipo_baraja(self) -> str:
        '''Método abstracto que debe ser implementado por las subclases.'''
        pass

    @property
    def cantidad_cartas(self) -> int:
        '''Devuelve la cantidad de cartas en la baraja.'''
        return len(self.cartas)