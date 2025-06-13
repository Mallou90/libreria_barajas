import sys
import os

# Añade la raíz del proyecto al sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.baraja.baraja_española import BarajaEspañola

baraja = BarajaEspañola()
baraja.barajar()
print(baraja)
carta_sacada = baraja.sacar_carta()
