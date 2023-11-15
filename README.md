# Laberinto Solver

Este repositorio contiene un script en Python para resolver un laberinto representado como una matriz bidimensional. El script utiliza un algoritmo de búsqueda en profundidad (DFS, por sus siglas en inglés) para encontrar el camino desde la entrada hasta la salida del laberinto.

## Contenido del Repositorio

- `tablero.py`: El script principal que contiene la lógica para resolver el laberinto.
- `LICENSE`: La licencia del proyecto (GNU General Public License v3.0).
- `README.md`: Este archivo que proporciona información sobre el proyecto.

## Requisitos

- Python 3.6 o superior

## Uso

1. Clona el repositorio:

   ```bash
   git clone https://github.com/yisuschrist/labyrinth-solver.git
   ```

2. Navega al directorio del repositorio:

   ```bash
   cd laberinto
   ```

3. Ejecuta el script:

   ```bash
   python tablero.py
   ```

   El script generará un laberinto y mostrará el proceso de resolución paso a paso, marcando el camino tomado hasta la salida.

## Descripción del Laberinto

El laberinto se representa como una lista de listas, donde cada lista es una fila del laberinto. Cada casilla se representa con un espacio (' ') si hay un pasillo o con la letra 'X' si hay un muro. La entrada se marca como 'E' y la salida como 'S'.

```python
laberinto = [
    ['E', 'X', 'X', 'X', 'X'],
    [' ', 'X', ' ', ' ', ' '],
    [' ', 'X', ' ', 'X', ' '],
    [' ', ' ', ' ', 'X', ' '],
    ['X', 'X', 'X', 'X', 'S']
]
```

Esto corresponde a un laberinto como el siguiente:

<div align="center">
    <img src="https://aprendeconalf.es/docencia/python/retos/img/laberinto.png" alt="Laberinto"/>
</div>

## Algoritmo de Búsqueda en Profundidad (DFS)

1. **Inicialización:** Comienza desde la entrada del laberinto y marca la casilla actual como visitada.

2. **Exploración de Vecinos:** Examina cada vecino no visitado de la casilla actual en las cuatro direcciones posibles (arriba, abajo, izquierda y derecha).

3. **Movimiento Recursivo:** Si encuentra un vecino no visitado, se mueve a ese vecino y repite el proceso de exploración desde esa nueva posición de manera recursiva.

4. **Retroceso:** Si no hay vecinos no visitados desde la posición actual, retrocede al nodo anterior (si existe) y continúa la exploración desde allí.

5. **Condición de Salida:** El algoritmo continúa explorando hasta que encuentra la salida del laberinto. Una vez que la salida se alcanza, el algoritmo termina y se obtiene el camino que lleva desde la entrada hasta la salida.

## Implementación en el Script

En el script proporcionado:

- La función buscar_solucion maneja la lógica principal del algoritmo DFS.
- La función siguiente_casilla busca el próximo movimiento posible desde la casilla actual, utilizando el enfoque de búsqueda en profundidad.

Es importante destacar que este enfoque puede no ser eficiente para laberintos muy grandes, ya que puede llegar a explorar muchas rutas antes de encontrar la solución. Sin embargo, para laberintos pequeños y medianos, proporciona una implementación clara y comprensible del algoritmo de búsqueda en profundidad.

## Créditos

- **Co-Autor:** Alejandro Gonzalez Teruel
- **URL:** https://github.com/alejandrom1999
- **Versión:** 1.0
- **Fecha:** 03/09/2023
- **URL del Proyecto:** https://github.com/yisuschrist/labyrinth-solver

## Reto de Programación

Este script aborda un reto de programación relacionado con la resolución de laberintos. Puedes encontrar más detalles sobre el reto en la siguiente URL: [Reto de Programación - Laberinto](https://aprendeconalf.es/docencia/python/retos/laberinto/).

¡Diviértete resolviendo laberintos!
