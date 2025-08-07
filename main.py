# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import constants
from asteroid import Asteroid
from constants import *

from asteroidfield import AsteroidField

from player import Player

from shot import Shot

pygame.init()
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids,updatable,drawable)

    AsteroidField.containers = (updatable)

    Player.containers = (updatable,drawable)

    Shot.containers = (shots, updatable, drawable)

    asteroid_field = AsteroidField()

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)


    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: 720 {SCREEN_HEIGHT}")

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0, 0, 0))

        updatable.update(dt)

        for object in Asteroid.containers[0]:
            if object.check_for_collision(player):
                print("Game over!")
                exit()
            for shot in shots:
                if object.check_for_collision(shot):
                    object.split()
                    shot.kill()

        for object in drawable:
            object.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
