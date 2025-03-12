import pygame
from shot import Shot
from constants import *
from circleshape import CircleShape

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x,y,PLAYER_RADIUS)
                                                # inherets build logic from CircleShape, for x y and PLAYER_RADIUS
                
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


    def shoot(self):
                                                # create new shot at player position
        
        new_shot = Shot(self.position.x, self.position.y)               # ! updated from self.position > self.position.x & self.position.y
                                                # allows to refer to player self for origin point of bullet, (0,0)
        
        shot_direction = pygame.Vector2(0,1)
                                                # the call to pygame.Vector2 is inferring:
                                                        # pygame as the class, and the logic of Vector2, for 2dimentional
                                                                # https://www.pygame.org/docs/ref/math.html?highlight=vector2#pygame.math.Vector2
                                                        # sets the speed of the shot
                                                        # the y value of 1 denotes how it should fire 
                                                                # "upwards"(+) when enacted, versus a downward(-)
                                                                # adding an v value would indicate a right(+) value or left(-) one
        

        shot_direction.rotate(self.rotation)            
                                                # keeps the alignment of the shot in parity with the rotation of the ship itself
                                                # so it always fires out of the nose
        

        new_shot.velocity = shot_direction * PLAYER_SHOOT_SPEED         
                                                # speed of the bullet is enhanced based on the speed of the ship in motion
                                                # + the static value of PLAYER_SHOOT_SPEED as defined in constants


    def update(self, dt):
        keys = pygame.key.get_pressed()
                                                # assigns keys for triggering action if detected

        if keys[pygame.K_a]:
            self.rotate(-dt)
                                                # if key a is pressed, rotate player character counter clockwise by value

        if keys[pygame.K_d]:
            self.rotate(dt)
                                                # if key a is pressed, rotate player character clockwise by value

        if keys[pygame.K_s]:
            self.move(-dt)
                                                # if key a is pressed, move character ship in negative momentum based on dt value
                                                        # utilizes move()

        if keys[pygame.K_w]:
            self.move(dt)
                                                # if key a is pressed, move character ship in positive momentum based on dt value
                                                        # utilizes move()

        if keys[pygame.K_SPACE]:
            self.shoot()
                                                # creates a new bullet


    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
                                                # logic for creating forward movement within game for player object shape/model
        self.position += forward * PLAYER_SPEED * dt
                                                # logic for how to adjust position based on that movement value provided