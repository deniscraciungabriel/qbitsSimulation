import pygame
import numpy as np
import sys
import math

pygame.init()

WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GRAY = (200, 200, 200)
QUBIT_RADIUS = 30
FONT_SIZE = 36

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Quantum Computer Simulator")

class Qubit:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.state = np.array([1.0, 0.0])
        self.collapsed = False
        self.angle = 0

    def apply_gate(self, gate):
        if gate == 'H':
            self.state = np.array([(self.state[0] + self.state[1])/np.sqrt(2),
                                   (self.state[0] - self.state[1])/np.sqrt(2)])
            self.collapsed = False
        elif gate == 'X':
            self.state = np.array([self.state[1], self.state[0]])
            self.collapsed = False
        elif gate == 'M':
            prob_0 = self.state[0]**2
            if np.random.random() < prob_0:
                self.state = np.array([1.0, 0.0])
            else:
                self.state = np.array([0.0, 1.0])
            self.collapsed = True

    def reset(self):
        self.state = np.array([1.0, 0.0])
        self.collapsed = False

    def draw(self):
        pygame.draw.circle(screen, BLUE, (self.x, self.y), QUBIT_RADIUS, 2)
        
        if self.collapsed:
            text = '0' if self.state[0] == 1 else '1'
            font = pygame.font.Font(None, FONT_SIZE)
            text_surf = font.render(text, True, BLACK)
            text_rect = text_surf.get_rect(center=(self.x, self.y))
            screen.blit(text_surf, text_rect)
        else:
            self.angle = (self.angle + 4) % 360
            end_x = self.x + QUBIT_RADIUS * math.cos(math.radians(self.angle))
            end_y = self.y + QUBIT_RADIUS * math.sin(math.radians(self.angle))
            pygame.draw.line(screen, RED, (self.x, self.y), (end_x, end_y), 2)

            prob_0 = round(self.state[0]**2, 2)
            prob_1 = round(self.state[1]**2, 2)
            font = pygame.font.Font(None, 24)
            text_surf = font.render(f"|0>: {prob_0}", True, BLACK)
            text_rect = text_surf.get_rect(center=(self.x, self.y + 50))
            screen.blit(text_surf, text_rect)
            text_surf = font.render(f"|1>: {prob_1}", True, BLACK)
            text_rect = text_surf.get_rect(center=(self.x, self.y + 70))
            screen.blit(text_surf, text_rect)

class Button:
    def __init__(self, x, y, w, h, label):
        self.rect = pygame.Rect(x, y, w, h)
        self.label = label

    def draw(self):
        pygame.draw.rect(screen, GRAY, self.rect)
        pygame.draw.rect(screen, BLACK, self.rect, 2)
        font = pygame.font.Font(None, 28)
        text_surf = font.render(self.label, True, BLACK)
        text_rect = text_surf.get_rect(center=self.rect.center)
        screen.blit(text_surf, text_rect)

qubits = [Qubit(WIDTH//4, HEIGHT//2), Qubit(3*WIDTH//4, HEIGHT//2)]
buttons = [
    Button(50, 500, 80, 40, 'H'),
    Button(150, 500, 80, 40, 'X'),
    Button(250, 500, 100, 40, 'Measure'),
    Button(370, 500, 80, 40, 'Reset')
]

selected_gate = None

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            
            for button in buttons:
                if button.rect.collidepoint(pos):
                    if button.label == 'Reset':
                        for q in qubits:
                            q.reset()
                    else:
                        selected_gate = button.label
                    break
            else:
                for q in qubits:
                    dx = pos[0] - q.x
                    dy = pos[1] - q.y
                    if dx**2 + dy**2 <= QUBIT_RADIUS**2:
                        if selected_gate:
                            q.apply_gate(selected_gate)
                            selected_gate = None

    screen.fill(WHITE)
    
    for q in qubits:
        q.draw()
    
    for button in buttons:
        button.draw()
    
    if selected_gate:
        font = pygame.font.Font(None, 28)
        text_surf = font.render(f"Selected: {selected_gate}", True, BLACK)
        screen.blit(text_surf, (50, 550))
    
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()