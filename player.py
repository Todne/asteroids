import circleshape
import pygame
import shot
import bomb
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN, PLAYER_BOMB_COOLDOWN, SCREEN_WIDTH, SCREEN_HEIGHT

class Player(circleshape.CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shot_cooldown_timer = 0
        self.bomb_counter = 1
        self.bomb_cooldown_timer = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)
        

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        if self.shot_cooldown_timer <= 0:
            newshot = shot.Shot(self.position.x, self.position.y)
            newshot.velocity = pygame.Vector2(0,1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
            self.shot_cooldown_timer = PLAYER_SHOOT_COOLDOWN

    def drop_bomb(self):
        if self.bomb_counter > 0:
            if self.bomb_cooldown_timer <= 0:
                bomb.Bomb(self.position.x, self.position.y)
                self.bomb_cooldown_timer = PLAYER_BOMB_COOLDOWN

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.shot_cooldown_timer -= dt
        self.bomb_cooldown_timer -= dt
        self.position.x %= SCREEN_WIDTH
        self.position.y %= SCREEN_HEIGHT

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_e]:
            self.drop_bomb()
        if keys[pygame.K_SPACE]:
            self.shoot()