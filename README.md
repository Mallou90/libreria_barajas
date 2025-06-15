# Proyecto_libreria
Mi primer proyecto para crear una librería con Python y aprender a hacerlo usando Github.
En este caso se trata de una librería de barajas, tanto española como francesa.

## Instalación

```bash
pip install barajas
```

## Características

### Baraja Española
- Barajar
- Sacar una o varias cartas
- Reiniciar la baraja
- En un futuro la implementación de algún juego sencillo

### Baraja Francesa
- Barajar
- Sacar una o varias cartas
- Reiniciar la baraja
- En un futuro la implementación de algún juego sencillo

## Estructura del proyecto
'''
proyecto_barajas/
├── src/
|   |──__init__.py
│   └── baraja/
│       ├── __init__.py
│       ├── baraja.py
│       ├── baraja_española.py
│       └── baraja_francesa.py
├── tests/
│   |── test_baraja_española.py
|   └──__init__.py
├── setup.py
├── requirements.txt
└── README.md
'''

## Uso

### Baraja Española
```python
from baraja import BarajaEspañola

# Crear una instancia de la baraja española
baraja = BarajaEspañola()

# Mostrar el estado inicial
print(f"Tipo de baraja: {baraja.tipo_baraja()}")  # Baraja Española
print(f"Número de cartas: {baraja.cantidad_cartas}")  # 40

# Barajar y sacar cartas
baraja.barajar()
carta = baraja.sacar_carta()  # Saca y muestra una carta
print(f"Carta sacada: {carta}")
print(f"Cartas restantes: {baraja.cantidad_cartas}")  # 39

# Sacar varias cartas
mano = baraja.sacar_varias_cartas(5)  # Saca 5 cartas
print(f"Cartas en mano: {mano}")
print(f"Cartas restantes: {baraja.cantidad_cartas}")  # 34

# Reiniciar la baraja
baraja.reiniciar()
print(f"Cartas después de reiniciar: {baraja.cantidad_cartas}")  # 40
```

### Baraja Francesa
```python
from baraja import BarajaFrancesa

# Crear una instancia de la baraja francesa
baraja = BarajaFrancesa()

# Mostrar el estado inicial
print(f"Tipo de baraja: {baraja.tipo_baraja()}")  # Baraja Francesa
print(f"Número de cartas: {baraja.cantidad_cartas}")  # 52

# Barajar y sacar cartas
baraja.barajar()
carta = baraja.sacar_carta()
print(f"Carta sacada: {carta}")
print(f"Cartas restantes: {baraja.cantidad_cartas}")  # 51

# Sacar varias cartas
mano = baraja.sacar_varias_cartas(5)
print(f"Cartas en mano: {mano}")
print(f"Cartas restantes: {baraja.cantidad_cartas}")  # 46

# Reiniciar la baraja
baraja.reiniciar()
print(f"Cartas después de reiniciar: {baraja.cantidad_cartas}")  # 52
```

## Desarrollo

1. Clona este repositorio

2. Crea un entorno virtual:
   ```bash
   python -m venv venv
   venv\Scripts\activate  # En Mac: source venv/bin/activate
   ```
3. Instala las dependencias de desarrollo:
   ```bash
   pip install -r requirements.txt
   ```
4. Instala el paquete en modo desarrollo:
   ```bash
   pip install -e .
   ```
## Ejecutar Pruebas

```bash
python -m unittest tests/test_baraja_española.py
```

## Buenas Prácticas Implementadas

1. **Programación Orientada a Objetos**: Uso de herencia y clases abstractas
2. **Documentación**: Docstrings detallados para clases y métodos
3. **Pruebas**: Cobertura completa de pruebas unitarias
4. **Código Limpio**: Nombres descriptivos y estructura clara