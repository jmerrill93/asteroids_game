import pygame
from circleshape import CircleShape
from constants import *



class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "gray", (int(self.position.x), int(self.position.y)), self.radius, SHOT_RADIUS)
    
    def update(self, dt):      
        self.position += self.velocity * dt