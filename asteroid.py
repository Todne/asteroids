import circleshape
import pygame
import random
from constants import ASTEROID_MIN_RADIUS

class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20, 50)
        randvector1 = self.velocity.rotate(angle)
        randvector2 = self.velocity.rotate(-angle)
        newradius = self.radius - ASTEROID_MIN_RADIUS
        newasteroid1 = Asteroid(self.position.x, self.position.y, newradius)
        newasteroid2 = Asteroid(self.position.x, self.position.y, newradius)
        newasteroid1.velocity = randvector1 * 1.2
        newasteroid2.velocity = randvector2 * 1.2