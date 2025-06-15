
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.baraja import BarajaFrancesa

def main():
    baraja = BarajaFrancesa()
    print("Baraja creada:", baraja.tipo_baraja())
    print("Cartas en la baraja:", baraja.cantidad_cartas)

    print("\nBarajando...")
    baraja.barajar()

    print("\nSacando 5 cartas:")
    cartas = baraja.sacar_varias_cartas(5)
    for carta in cartas:
        print("Carta sacada:", carta)
    print("Cartas restantes en la baraja:", baraja.cantidad_cartas)

    print("\nReiniciando la baraja...")
    baraja.reiniciar()
    print("Cartas en la baraja tras reiniciar:", baraja.cantidad_cartas)

if __name__ == "__main__":
    main()