# Proyecto_Final
Proyecto Final

## Datos del Alumno
- **Nombre:** Ramiro Lugo Meza
- **Matrícula:** A01712509
- **Juego asignado:** Memoria (`memory.py`)

## Modificaciones realizadas
1. **Contador de pares:** Se agregó la variable `pares` al diccionario `state` para contar y desplegar en pantalla los pares descubiertos.
2. **Detección de victoria:** Se agregó la verificación `if not any(hide):` para mostrar el mensaje "¡Juego Terminado!" cuando se destapan todas las fichas.
3. **Tamaño del tablero:** Se redujo el número de fichas de 64 (32 pares) a 16 (8 pares) ajustando `tiles`, `hide` y el ciclo de dibujado.