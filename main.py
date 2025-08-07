# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import constants
from constants import *

from player import Player

pygame.init()
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable,drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)


    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: 720 {SCREEN_HEIGHT}")

    while True:
        screen.fill((0, 0, 0))

        for playerx in player.containers[0]:
            playerx.update(dt)

        for drawablex in player.containers[1]:
            drawablex.draw(screen)

        pygame.display.flip()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
