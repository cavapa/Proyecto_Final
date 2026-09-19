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
def check_winner():
    """Verifica si hay un ganador o empate."""
    wins = [
        # Filas
        [(-200, 67), (-67, 67), (67, 67)],
        [(-200, -67), (-67, -67), (67, -67)],
        [(-200, -200), (-67, -200), (67, -200)],
        # Columnas
        [(-200, 67), (-200, -67), (-200, -200)],
        [(-67, 67), (-67, -67), (-67, -200)],
        [(67, 67), (67, -67), (67, -200)],
        # Diagonales
        [(-200, 67), (-67, -67), (67, -200)],
        [(-200, -200), (-67, -67), (67, 67)]
    ]
    
    for line in wins:
        p1, p2, p3 = line
        if p1 in board and p2 in board and p3 in board:
            if board[p1] == board[p2] == board[p3]:
                return board[p1]  # Retorna 0 (X) o 1 (O)
                
    if len(board) == 9:
        return "Empate"
        
    return None
def tap(x, y):
    """Draw X or O in tapped square."""
    x = floor(x)
    y = floor(y)
    
    if (x, y) in board:
        print("¡Casilla ocupada! Elige otra.")
        return
        
    player = state['player']
    draw = players[player]
    draw(x, y)
    update()
    
    board[(x, y)] = player
    state['player'] = not player
    
    # Revisar si el juego ha terminado
    winner = check_winner()
    if winner is not None:
        up()
        goto(0, 0)
        color('green')
        if winner == "Empate":
            write("¡Empate!", align="center", font=("Arial", 40, "bold"))
        else:
            jugador = "X" if winner == 0 else "O"
            write(f"¡Ganó {jugador}!", align="center", font=("Arial", 40, "bold"))
        onscreenclick(None)  # Congela la pantalla

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
grid()
update()
onscreenclick(tap)
done()
