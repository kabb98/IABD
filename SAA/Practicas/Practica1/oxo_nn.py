import random
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

# Inicializar el tablero
board = [""] * 9

# Función para codificar el estado del tablero a una cadena
def encode_state(board):
    return "".join(board)

# Función para crear una red neuronal simple
def create_model():
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(128, activation='relu', input_shape=(9,)),
        tf.keras.layers.Dense(64, activation='relu'),
        tf.keras.layers.Dense(9, activation='linear')  # 9 salidas para cada casilla
    ])
    model.compile(optimizer='adam', loss='mean_squared_error')
    return model

# Función para que la IA haga un movimiento basado en la red neuronal
def ai_move(board, model):
    state = np.array([1 if cell == "X" else -1 if cell == "O" else 0 for cell in board])
    q_values = model.predict(np.array([state]))[0]
    legal_moves = [i for i, cell in enumerate(board) if cell == ""]
    q_values_available = [q_values[i] for i in legal_moves]
    return legal_moves[np.argmax(q_values_available)]

# Función para verificar si un jugador ha ganado
def check_winner(board, player):
    for line in [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]:
        if all(board[i] == player for i in line):
            return True
    return False

# Ciclo principal del juego
model = create_model()
errors = []  # Lista para almacenar los errores en cada iteración
for _ in range(1000):
    board = [""] * 9
    state = np.array([1 if cell == "X" else -1 if cell == "O" else 0 for cell in board])
    while True:
        if "X" not in board and "O" not in board:
            action = random.randint(0, 8)
        else:
            action = ai_move(board, model)
        if board[action] == "":
            board[action] = "X"
        next_state = np.array([1 if cell == "X" else -1 if cell == "O" else 0 for cell in board])
        if check_winner(board, "X"):
            reward = 1
        elif check_winner(board, "O"):
            reward = -1
        elif "" not in board:
            reward = 0
        else:
            reward = 0  # Juego en curso
        target = model.predict(np.array([state]))[0]
        target[action] = reward
        error = model.fit(np.array([state]), np.array([target]), epochs=1, verbose=0).history['loss'][0]
        errors.append(error)
        if check_winner(board, "X"):
            break
        state = next_state

# Generar la gráfica de evolución del error
plt.plot(errors)
plt.xlabel('Iteración')
plt.ylabel('Error')
plt.title('Evolución del error en el aprendizaje')
plt.show()

# Ahora, puedes utilizar la red neuronal entrenada para jugar contra la IA
board = [""] * 9
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
        action = ai_move(board, model)
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