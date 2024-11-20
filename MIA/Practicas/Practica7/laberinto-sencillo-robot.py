import pygame
import numpy as np
import random
from sklearn.neural_network import MLPClassifier

class MazeRobotSimulation:
    def __init__(self, size=7):
        pygame.init()
        
        # Screen setup
        self.size = size
        self.cell_size = 70
        self.screen_width = size * self.cell_size
        self.screen_height = size * self.cell_size + 80
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Maze Robot Navigation")

        # Colors
        self.COLORS = {
            'BACKGROUND': (240, 248, 255),  # Light blue
            'WALL': (70, 70, 90),           # Dark grayish blue
            'PATH': (230, 230, 250),        # Lavender
            'ROBOT': (255, 69, 0),          # Red-orange
            'GOAL': (50, 205, 50),          # Lime green
            'BUTTON': (100, 149, 237),      # Cornflower blue
            'TEXT': (255, 255, 255),        # White
            'OUTLINE': (119, 136, 153)      # Slate gray
        }

        # Fonts
        pygame.font.init()
        self.font = pygame.font.Font(None, 36)
        
        # Game elements
        self.maze = self.create_maze()
        self.robot_pos = (0, 0)
        self.robot_dir = "E"
        self.goal = (size - 1, size - 1)
        self.model = self.train_neural_network()
        
        # Button
        self.button_rect = pygame.Rect(
            self.screen_width // 2 - 100, 
            self.screen_height - 60, 
            200, 
            40
        )
        
        # Game state
        self.steps = 0
        self.max_steps = 100

    def create_maze(self):
        maze = np.ones((self.size, self.size))
        path = [(0, 0)]
        maze[0, 0] = 0
        x, y = 0, 0
        
        while (x, y) != (self.size - 1, self.size - 1):
            if random.random() < 0.5 and y < self.size - 1:
                y += 1
            elif x < self.size - 1:
                x += 1
            maze[x, y] = 0
            path.append((x, y))
        
        for i in range(self.size):
            for j in range(self.size):
                if (i, j) not in path and random.random() < 0.3:
                    maze[i][j] = 1
        return maze

    def train_neural_network(self):
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

    def get_sensors(self):
        movimientos = {
            "N": [(-1, 0), (0, -1), (0, 1)],
            "S": [(1, 0), (0, 1), (0, -1)],
            "E": [(0, 1), (-1, 0), (1, 0)],
            "W": [(0, -1), (1, 0), (-1, 0)]
        }
        sensores = [0, 0, 0]
        for idx, (di, dj) in enumerate(movimientos[self.robot_dir]):
            ni, nj = self.robot_pos[0] + di, self.robot_pos[1] + dj
            if (not (0 <= ni < self.size and 0 <= nj < self.size)) or self.maze[ni][nj] == 1:
                sensores[idx] = 1
        return sensores

    def move_robot(self, action):
        movimientos = {"N": (-1, 0), "S": (1, 0), "E": (0, 1), "W": (0, -1)}
        direcciones = ["N", "E", "S", "W"]
        
        if action == "avanzar":
            nueva_pos = (
                self.robot_pos[0] + movimientos[self.robot_dir][0], 
                self.robot_pos[1] + movimientos[self.robot_dir][1]
            )
        elif action == "girar_derecha":
            nueva_dir = direcciones[(direcciones.index(self.robot_dir) + 1) % 4]
            return self.robot_pos, nueva_dir
        elif action == "girar_izquierda":
            nueva_dir = direcciones[(direcciones.index(self.robot_dir) - 1) % 4]
            return self.robot_pos, nueva_dir
        else:
            nueva_pos = self.robot_pos
        
        if (0 <= nueva_pos[0] < self.size and 
            0 <= nueva_pos[1] < self.size and 
            self.maze[nueva_pos] == 0):
            return nueva_pos, self.robot_dir
        return self.robot_pos, self.robot_dir

    def draw(self):
        self.screen.fill(self.COLORS['BACKGROUND'])
        
        # Draw maze
        for i in range(self.size):
            for j in range(self.size):
                rect = pygame.Rect(j*self.cell_size, i*self.cell_size, self.cell_size, self.cell_size)
                if self.maze[i, j] == 1:
                    pygame.draw.rect(self.screen, self.COLORS['WALL'], rect)
                    pygame.draw.rect(self.screen, self.COLORS['OUTLINE'], rect, 2)
                else:
                    pygame.draw.rect(self.screen, self.COLORS['PATH'], rect)
                    pygame.draw.rect(self.screen, self.COLORS['OUTLINE'], rect, 1)
        
        # Draw robot as a directional triangle
        center_x = self.robot_pos[1]*self.cell_size + self.cell_size // 2
        center_y = self.robot_pos[0]*self.cell_size + self.cell_size // 2
        triangle_size = self.cell_size * 0.6
        
        # Calculate triangle points based on direction
        if self.robot_dir == "N":
            points = [
                (center_x, center_y - triangle_size/2),
                (center_x - triangle_size/2, center_y + triangle_size/2),
                (center_x + triangle_size/2, center_y + triangle_size/2)
            ]
        elif self.robot_dir == "S":
            points = [
                (center_x, center_y + triangle_size/2),
                (center_x - triangle_size/2, center_y - triangle_size/2),
                (center_x + triangle_size/2, center_y - triangle_size/2)
            ]
        elif self.robot_dir == "E":
            points = [
                (center_x + triangle_size/2, center_y),
                (center_x - triangle_size/2, center_y - triangle_size/2),
                (center_x - triangle_size/2, center_y + triangle_size/2)
            ]
        else:  # W
            points = [
                (center_x - triangle_size/2, center_y),
                (center_x + triangle_size/2, center_y - triangle_size/2),
                (center_x + triangle_size/2, center_y + triangle_size/2)
            ]
        
        pygame.draw.polygon(self.screen, self.COLORS['ROBOT'], points)
        pygame.draw.polygon(self.screen, self.COLORS['OUTLINE'], points, 3)
        
        # Draw goal
        goal_rect = pygame.Rect(
            self.goal[1]*self.cell_size, 
            self.goal[0]*self.cell_size, 
            self.cell_size, 
            self.cell_size
        )
        pygame.draw.rect(self.screen, self.COLORS['GOAL'], goal_rect)
        pygame.draw.rect(self.screen, self.COLORS['OUTLINE'], goal_rect, 3)
        
        # Draw button
        pygame.draw.rect(self.screen, self.COLORS['BUTTON'], self.button_rect, border_radius=10)
        button_text = self.font.render(f"Next Step ({self.steps})", True, self.COLORS['TEXT'])
        text_rect = button_text.get_rect(center=self.button_rect.center)
        self.screen.blit(button_text, text_rect)
        
        pygame.display.flip()

    def run(self):
        running = True
        while running and self.robot_pos != self.goal and self.steps < self.max_steps:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.button_rect.collidepoint(event.pos):
                        sensors = self.get_sensors()
                        action_idx = self.model.predict([sensors])[0]
                        action = ["girar_derecha", "girar_izquierda", "avanzar"][action_idx]
                        
                        self.robot_pos, self.robot_dir = self.move_robot(action)
                        self.steps += 1
            
            self.draw()
        
        pygame.quit()

# Run the simulation
MazeRobotSimulation().run()