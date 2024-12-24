import circleshape
import pygame
from constants import SHOT_RADIUS, PLAYER_SHOOT_LIFETIME

class Shot(circleshape.CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        self.shot_lifetime = PLAYER_SHOOT_LIFETIME

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
        self.shot_lifetime -= dt
        if self.shot_lifetime <= 0:
            self.kill()