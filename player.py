import pygame
from constants import *
from circleshape import CircleShape

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x,y,PLAYER_RADIUS)
        self.rotation = 0
                # defines the object boundaries of the player "character"


    def draw(self, screen):
        pygame.draw.polygon(screen,"white",self.triangle(),2)
                # defines the visual shape of the player "character"


    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
                # defines the 3 points needed to render the player "character"


    def rotate(self, dt):
        self.rotation +=  PLAYER_TURN_SPEED * dt 
                # defines the rotation speed w/ the dt variable for acceleration


    def update(self, dt):
        keys = pygame.key.get_pressed()
                # assigns keys for triggering action if detected

        if keys[pygame.K_a]:
            self.rotate(-dt)
                    # if key a is pressed, rotate player character counter clockwise by value

        if keys[pygame.K_d]:
            self.rotate(dt)
                    # if key a is pressed, rotate player character clockwise by value