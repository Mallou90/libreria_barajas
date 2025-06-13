# Pruebas unitarias para la clase BarajaEspañola
import unittest
import random
import sys
from pathlib import Path

# Añade el directorio src al path de Python
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.baraja import BarajaEspañola

class TestBarajaEspañola(unittest.TestCase):
    def setUp(self):
        """Inicializa una nueva baraja para cada test."""
        self.baraja = BarajaEspañola()

    def test_tipo_baraja(self):
        """Verifica que el tipo de baraja sea correcto."""
        self.assertEqual(self.baraja.tipo_baraja(), "Baraja Española")

    def test_cantidad_cartas_inicial(self):
        """Verifica que la baraja tenga 40 cartas al inicio."""
        self.assertEqual(self.baraja.cantidad_cartas, 40)

    def test_barajar_mantiene_cartas(self):
        """Verifica que barajar no pierda ni duplique cartas."""
        cartas_antes = set(self.baraja.cartas)
        self.baraja.barajar()
        cartas_despues = set(self.baraja.cartas)
        self.assertEqual(cartas_antes, cartas_despues)
        self.assertEqual(len(self.baraja.cartas), 40)

    def test_sacar_carta_reduce_mazo(self):
        """Verifica que sacar una carta reduzca el mazo."""
        carta = self.baraja.sacar_carta()
        self.assertIsInstance(carta, str)
        self.assertEqual(self.baraja.cantidad_cartas, 39)

    def test_sacar_varias_cartas(self):
        """Verifica que se puedan sacar múltiples cartas."""
        cartas = self.baraja.sacar_varias_cartas(5)
        self.assertEqual(len(cartas), 5)
        self.assertEqual(self.baraja.cantidad_cartas, 35)

    def test_reiniciar_restaura_mazo(self):
        """Verifica que reiniciar restaure el mazo completo."""
        self.baraja.sacar_varias_cartas(10)
        self.baraja.reiniciar()
        self.assertEqual(self.baraja.cantidad_cartas, 40)

if __name__ == '__main__':
    unittest.main()