import pygame
from constants import *
from circleshape import CircleShape


class Shot(CircleShape):
    def __init__(self, x, y ):
                                        # class constructor

        super().__init__(x, y, SHOT_RADIUS)
                                        # calls to the builder of CircleShape

        self.velocity = pygame.Vector2(0, 0)
                                        # initializes velocity vector

    def update(self, dt):

        self.position += self.velocity * dt


    def draw(self, surface):            
                                        # copy of logic from asteroid.py
        
        pygame.draw.circle(surface, (255, 0, 255), (self.position.x, self.position.y), self.radius, 1)