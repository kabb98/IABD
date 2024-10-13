

"""# OXO con inteligencia fuerte"""

import random

# Inicializar el tablero
board = [""] * 9
# Parámetros de Q-learning
learning_rate = 0.1
discount_factor = 0.9
# Crear una tabla Q para el agente (en este caso, el jugador "X")
q_table = {}
# Función para codificar el estado del tablero a una cadena
def encode_state(board):
    return "".join(board)
# Función para que la IA haga un movimiento basado en Q-learning
def ai_move(board):
    state = encode_state(board)
    if state not in q_table:
        q_table[state] = [0.0] * 9  # Inicializar valores Q para el estado
    legal_moves = [i for i, cell in enumerate(board) if cell == ""]
    if random.uniform(0, 1) < exploration_prob:
        return random.choice(legal_moves)
    else:
        return max(legal_moves, key=lambda move: q_table[state][move])

# Función para actualizar la tabla Q después de una jugada
def update_q_table(state, action, reward, next_state):
    if state not in q_table:
        q_table[state] = [0.0] * 9
    if next_state not in q_table:
        q_table[next_state] = [0.0] * 9
    q_table[state][action] = q_table[state][action] + learning_rate * (reward + discount_factor * max(q_table[next_state]) - q_table[state][action])

# Función para verificar si un jugador ha ganado
def check_winner(board, player):
    for line in [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]:
        if all(board[i] == player for i in line):
            return True
    return False

# Parámetro de exploración
exploration_prob = 0.1

# Ciclo principal del juego
for _ in range(10000):
    board = [""] * 9
    state = encode_state(board)

    while True:
        if "X" not in board and "O" not in board:
            action = random.randint(0, 8)
        else:
            action = ai_move(board)

        if board[action] == "":
            board[action] = "X"

        next_state = encode_state(board)

        if check_winner(board, "X"):
            reward = 1
        elif check_winner(board, "O"):
            reward = -1
        elif "" not in board:
            reward = 0
        else:
            reward = 0  # Juego en curso

        update_q_table(state, action, reward, next_state)

        if check_winner(board, "X"):
            break
        state = next_state

# Ahora, puedes utilizar la tabla Q entrenada para jugar contra la IA
board = [ ""] * 9
player_turn = True
while True:
    if player_turn:
        print("Tu turno (X)")
        move = int(input("Elige una casilla (0-8): "))
        if board[move] == "":
            board[move] = "X"
            player_turn = False
    else:
        print("Turno de la IA (O)")
        action = ai_move(board)
        board[action] = "O"
        player_turn = True
    # Mostrar el tablero
    for i in range(0, 9, 3):
        print(" ".join(board[i:i+3]))

    if check_winner(board, "X"):
        print("¡Ganaste!")
        break
    elif check_winner(board, "O"):
        print("¡La IA ganó!")
        break
    elif "" not in board:
        print("Empate")
        break