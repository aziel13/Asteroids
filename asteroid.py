import pygame

import constants
from constants import *

from circleshape import CircleShape

import random


class Asteroid(CircleShape):

    def __init__(self,x,y,radius,):
        super().__init__(x, y, radius)
        self.rotation = 0

    def split(self):
        self.kill()

        if self.radius > ASTEROID_MIN_RADIUS:
            blue_angle = random.uniform(20, 50)

            new_radius = self.radius - ASTEROID_MIN_RADIUS

            new_asteroid1 = Asteroid(self.position.x,self.position.y, new_radius)
            new_asteroid1.velocity = self.velocity.rotate(blue_angle)
            new_asteroid1.velocity *= 1.2

            new_asteroid2 = Asteroid(self.position.x,self.position.y, new_radius)
            new_asteroid2.velocity = self.velocity.rotate(-blue_angle)
            new_asteroid2.velocity *= 1.2

    def draw(self, screen):
        pygame.draw.circle(screen,"white",self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)
