import pygame
import numpy as np
import random
from sklearn.neural_network import MLPClassifier

# Copy the previous functions from the original code
def entrenar_modelo_nuevo_sklearn():
    inputs = np.array([
        [0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0],
        [1, 1, 0], [1, 0, 1], [0, 1, 1], [1, 1, 1]
    ])
    outputs = np.array([
        [0, 0, 1], [0, 0, 1], [0, 0, 1], [1, 0, 0],
        [1, 0, 0], [0, 1, 0], [0, 0, 1], [0, 1, 0]
    ])
    model = MLPClassifier(hidden_layer_sizes=(16, 12), activation='relu', max_iter=500, random_state=42)
    model.fit(inputs, np.argmax(outputs, axis=1))
    return model

def crear_laberinto_con_camino(tamaño=10):
    laberinto = np.ones((tamaño, tamaño))
    camino = [(0, 0)]
    laberinto[0, 0] = 0
    x, y = 0, 0
    while (x, y) != (tamaño - 1, tamaño - 1):
        if random.random() < 0.5 and y < tamaño - 1:
            y += 1
        elif x < tamaño - 1:
            x += 1
        laberinto[x, y] = 0
        camino.append((x, y))
    for i in range(tamaño):
        for j in range(tamaño):
            if (i, j) not in camino and random.random() < 0.3:
                laberinto[i][j] = 1
    return laberinto

def obtener_sensores(laberinto, posicion, direccion):
    tamaño = laberinto.shape[0]
    sensores = [0, 0, 0]
    movimientos = {
        "N": [(-1, 0), (0, -1), (0, 1)],
        "S": [(1, 0), (0, 1), (0, -1)],
        "E": [(0, 1), (-1, 0), (1, 0)],
        "W": [(0, -1), (1, 0), (-1, 0)]
    }
    for idx, (di, dj) in enumerate(movimientos[direccion]):
        ni, nj = posicion[0] + di, posicion[1] + dj
        if not (0 <= ni < tamaño and 0 <= nj < tamaño) or laberinto[ni][nj] == 1:
            sensores[idx] = 1
    return sensores

def mover_robot(posicion, direccion, accion, laberinto):
    movimientos = {"N": (-1, 0), "S": (1, 0), "E": (0, 1), "W": (0, -1)}
    direcciones = ["N", "E", "S", "W"]
    if accion == "avanzar":
        nueva_posicion = (posicion[0] + movimientos[direccion][0], posicion[1] + movimientos[direccion][1])
    elif accion == "girar_derecha":
        nueva_direccion = direcciones[(direcciones.index(direccion) + 1) % 4]
        return posicion, nueva_direccion
    elif accion == "girar_izquierda":
        nueva_direccion = direcciones[(direcciones.index(direccion) - 1) % 4]
        return posicion, nueva_direccion
    else:
        nueva_posicion = posicion
    if 0 <= nueva_posicion[0] < laberinto.shape[0] and 0 <= nueva_posicion[1] < laberinto.shape[1] and laberinto[nueva_posicion] == 0:
        return nueva_posicion, direccion
    return posicion, direccion

# Pygame visualization
def simular_laberinto_pygame():
    pygame.init()
    
    # Maze parameters
    tamaño = 10
    cell_size = 60
    screen_width = tamaño * cell_size
    screen_height = tamaño * cell_size + 50  # Extra space for button
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Maze Robot Simulation")

    # Colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)

    # Create maze and robot
    laberinto = crear_laberinto_con_camino(tamaño)
    posicion = (0, 0)
    direccion = "E"
    objetivo = (tamaño - 1, tamaño - 1)
    model = entrenar_modelo_nuevo_sklearn()

    # Fonts
    font = pygame.font.Font(None, 36)
    
    # Next step button
    button_rect = pygame.Rect(10, screen_height - 40, 100, 30)
    
    # Game loop control
    running = True
    pasos = 0
    max_pasos = 100

    while running and posicion != objetivo and pasos < max_pasos:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    # Perform robot movement on button click
                    sensores = obtener_sensores(laberinto, posicion, direccion)
                    accion_idx = model.predict([sensores])[0]
                    accion = ["girar_derecha", "girar_izquierda", "avanzar"][accion_idx]
                    
                    nueva_posicion, nueva_direccion = mover_robot(posicion, direccion, accion, laberinto)
                    posicion, direccion = nueva_posicion, nueva_direccion
                    
                    pasos += 1

        # Drawing
        screen.fill(WHITE)
        
        # Draw maze
        for i in range(tamaño):
            for j in range(tamaño):
                rect = pygame.Rect(j*cell_size, i*cell_size, cell_size, cell_size)
                if laberinto[i, j] == 1:
                    pygame.draw.rect(screen, BLACK, rect)
                else:
                    pygame.draw.rect(screen, WHITE, rect, 1)
        
        # Draw robot
        robot_rect = pygame.Rect(posicion[1]*cell_size, posicion[0]*cell_size, cell_size, cell_size)
        pygame.draw.rect(screen, RED, robot_rect)
        
        # Draw goal
        goal_rect = pygame.Rect(objetivo[1]*cell_size, objetivo[0]*cell_size, cell_size, cell_size)
        pygame.draw.rect(screen, GREEN, goal_rect)
        
        # Draw next step button
        pygame.draw.rect(screen, BLUE, button_rect)
        button_text = font.render("Next Step", True, WHITE)
        screen.blit(button_text, (button_rect.x + 5, button_rect.y + 5))
        
        # Update display
        pygame.display.flip()

    pygame.quit()

# Run the simulation
simular_laberinto_pygame()