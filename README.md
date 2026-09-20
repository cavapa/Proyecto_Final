
# Proyecto Final - Tic Tac Toe

- Patricio Castillo

## Proceso de Solución del Reto
Para cumplir con los requerimientos del proyecto, implementamos las siguientes modificaciones sobre el código base de `freegames`:

1. **Personalización de Símbolos:** Modificamos las funciones `drawx` y `drawo`. Se cambió el color de los trazos (azul para X, rojo para O) y se recalcularon las coordenadas `(x, y)` usando desplazamientos específicos para centrar las figuras perfectamente dentro de la cuadrícula de 133x133 píxeles.
2. **Validación de Casillas Ocupadas:** Declaramos un diccionario global llamado `board`. En la función `tap(x, y)`, agregamos una condicional que verifica si las coordenadas del clic ya existen en el diccionario. Si existen, la función retorna inmediatamente, ignorando el clic. Si están libres, se dibuja la figura y se guarda la coordenada.
3. **Detección de Ganador y Empate:** Creamos la función `check_winner()`, la cual contiene una lista con todas las combinaciones de coordenadas ganadoras (filas, columnas y diagonales). Tras cada jugada, se itera sobre esta lista buscando coincidencias en el diccionario `board`. Si hay un ganador o el tablero se llena (9 casillas), el juego imprime el resultado en pantalla y deshabilita los clics usando `onscreenclick(None)`.


