import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from bomb import Bomb
from explosion import Explosion

def main():
    pygame.init()
    timer = pygame.time.Clock()
    dt = 0
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    bombs = pygame.sprite.Group()
    explosions = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    Bomb.containers = (bombs, updatable, drawable)
    Explosion.containers = (explosions, updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for object in updatable:
            object.update(dt)
        for asteroid in asteroids:
            if asteroid.check_collision(player):
                print("Game over!")
                exit()
            for shot in shots:
                if asteroid.check_collision(shot):
                    shot.kill()
                    asteroid.split()
            for explosion in explosions:
                if asteroid.check_collision(explosion):
                    asteroid.kill()
        screen.fill((0, 0, 0))
        for object in drawable:
            object.draw(screen)
        pygame.display.flip()
        dt = timer.tick(60) / 1000

if __name__ == "__main__":
    main()
