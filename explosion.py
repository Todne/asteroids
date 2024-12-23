import circleshape
import pygame
from constants import PLAYER_BOMB_EXPLOSION_RADIUS

class Explosion(circleshape.CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_BOMB_EXPLOSION_RADIUS)
        self.countdown = 1

    def draw(self, screen):
        pygame.draw.circle(screen, "red", self.position, self.radius, 100)

    def update(self, dt):
        self.countdown -= dt
        if self.countdown <= 0:
            self.kill()