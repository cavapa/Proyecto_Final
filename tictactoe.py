"""Tic Tac Toe

Exercises

1. Give the X and O a different color and width.
2. What happens when someone taps a taken spot?
3. How would you detect when someone has won?
4. How could you create a computer player?
"""

from turtle import *

from freegames import line


def grid():
    """Draw tic-tac-toe grid."""
    line(-67, 200, -67, -200)
    line(67, 200, 67, -200)
    line(-200, -67, 200, -67)
    line(-200, 67, 200, 67)


def drawx(x, y):
    """Dibuja el jugador X."""
    color('blue')
    width(4)
    line(x + 20, y + 20, x + 113, y + 113)
    line(x + 20, y + 113, x + 113, y + 20)

def drawo(x, y):
    """Dibuja el jugador O."""
    color('red')
    width(4)
    up()
    goto(x + 67, y + 20)
    down()
    circle(46)


def floor(value):
    """Round value down to grid with square size 133."""
    return ((value + 200) // 133) * 133 - 200


state = {'player': 0}
players = [drawx, drawo]
board = {}  # Diccionario para registrar las casillas ocupadas

def tap(x, y):
    """Draw X or O in tapped square."""
    x = floor(x)
    y = floor(y)
    
    # Validación: si la coordenada ya existe en el tablero, ignorar el clic
    if (x, y) in board:
        print("¡Casilla ocupada! Elige otra.")
        return
        
    player = state['player']
    draw = players[player]
    draw(x, y)
    update()
    
    # Guardar la coordenada como ocupada por el jugador actual
    board[(x, y)] = player
    
    state['player'] = not player

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
grid()
update()
onscreenclick(tap)
done()
