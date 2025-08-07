# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import constants
from asteroid import Asteroid
from constants import *

from asteroidfield import AsteroidField

from player import Player

pygame.init()
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Asteroid.containers = (asteroids,updatable,drawable)

    AsteroidField.containers = (updatable)

    Player.containers = (updatable,drawable)

    asteroid_field = AsteroidField()

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)


    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: 720 {SCREEN_HEIGHT}")

    while True:
        screen.fill((0, 0, 0))

        for object in player.containers[0]:
            object.update(dt)

        for object in asteroid_field.containers:
            object.update(dt)

        for object in Asteroid.containers[1]:
            object.update(dt)

        for object in Asteroid.containers[0]:
            if object.check_for_collision(player):
                print("Game over!")
                exit()

        for object in player.containers[1]:
            object.draw(screen)

        for object in Asteroid.containers[2]:
            object.update(dt)




        pygame.display.flip()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
