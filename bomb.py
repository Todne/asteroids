import circleshape
import pygame
from constants import PLAYER_BOMB_RADIUS, PLAYER_BOMB_EXPLOSION_RADIUS, PLAYER_BOMB_COUNTDOWN

class Bomb(circleshape.CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_BOMB_RADIUS)
        self.countdown = PLAYER_BOMB_COUNTDOWN

    def draw(self, screen):
        pygame.draw.circle(screen, "red", self.position, self.radius, 2)

    def update(self, dt):
        self.countdown -= 1
        if self.countdown <= 0:
            self.kill()