"""
Paquete de barajas de cartas.
"""
from .barajas import Baraja
from .baraja_española import BarajaEspañola
from .baraja_francesa import BarajaFrancesa

__version__ = "0.1.0"
__all__ = ["Baraja", "BarajaEspañola", "BarajaFrancesa"]