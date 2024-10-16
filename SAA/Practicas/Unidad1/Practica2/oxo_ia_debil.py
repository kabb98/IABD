import random

# Inicializar el tablero
board = [""] * 9
player_turn = True
game_over = False

# Función para imprimir el tablero
def print_board(board):
    for i in range(0, 9, 3):
        print(board[i], "|", board[i+1], "|", board[i+2])
        if i < 6:
            print("---------")

# Función para verificar si un jugador ha ganado
def check_winner(board, player):
    for line in [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]:
        if all(board[i] == player for i in line):
            return True
    return False

# Función para que la IA haga un movimiento aleatorio
def ai_move(board):
    empty_cells = [i for i in range(9) if board[i] == ""]
    if empty_cells:
        return random.choice(empty_cells)
    else:
        return None

# Ciclo principal del juego
movimientos = 0
while not game_over:
    print_board(board)
    if player_turn:
        movimientos += 1
        print("Tu turno (X)")
        move = input("Elige una casilla (0-8): ")
        if move.isdigit() and 0 <= int(move) < 9 and board[int(move)] == "":
            board[int(move)] = "X"
            player_turn = False
    else:
        print("Turno de la IA (O)")
        ai_position = ai_move(board)
        if ai_position is not None:
            board[ai_position] = "O"
            player_turn = True
    if check_winner(board, "X"):
        print_board(board)
        print(f"¡Ganaste en {movimientos} movimientos!")
        
        game_over = True
    elif check_winner(board, "O"):
        print_board(board)
        print("¡La IA ganó!")
        game_over = True
    elif "" not in board:
        print_board(board)
        print("Empate")
        game_over = True

print("Fin del juego")