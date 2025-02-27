import pygame
import random
from asteroid import Asteroid
from constants import *

        # ALL FOLLOWING DATA WAS PROVIDED FOR USE AS PART OF COURSE
            # will review and breakdown at later date~

class AsteroidField(pygame.sprite.Sprite):
    edges = [
        [
            pygame.Vector2(1, 0),
            lambda y: pygame.Vector2(-ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT),
        ],
        [
            pygame.Vector2(-1, 0),
            lambda y: pygame.Vector2(
                SCREEN_WIDTH + ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT
            ),
        ],
        [
            pygame.Vector2(0, 1),
            lambda x: pygame.Vector2(x * SCREEN_WIDTH, -ASTEROID_MAX_RADIUS),
        ],
        [
            pygame.Vector2(0, -1),
            lambda x: pygame.Vector2(
                x * SCREEN_WIDTH, SCREEN_HEIGHT + ASTEROID_MAX_RADIUS
            ),
        ],
    ]

    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.spawn_timer = 0.0

    def spawn(self, radius, position, velocity):
        #           # print(f"Spawning asteroid at {position} with radius {radius}")
                # q?^^
        asteroid = Asteroid(position.x, position.y, radius)
        asteroid.velocity = velocity
        #           # print(f"Asteroid created with velocity {asteroid.velocity}")
                # q?^^

    def update(self, dt):
        #           # print(f"AsteroidField update called with dt={dt}")
                # troubleshooting to see why Asteroids are not spawning as expected - ?^^

        self.spawn_timer += dt
        #           # print(f"Spawn timer: {self.spawn_timer}, Spawn rate: {ASTEROID_SPAWN_RATE}")
                # q?^^
        if self.spawn_timer > ASTEROID_SPAWN_RATE:
            self.spawn_timer = 0
            #           # print("Spawn timer threshold reached, spawning asteroid")
                    # q?^^
            
            # spawn a new asteroid at a random edge
            edge = random.choice(self.edges)
            speed = random.randint(40, 100)
            velocity = edge[0] * speed
            velocity = velocity.rotate(random.randint(-30, 30))
            position = edge[1](random.uniform(0, 1))
            kind = random.randint(1, ASTEROID_KINDS)
            self.spawn(ASTEROID_MIN_RADIUS * kind, position, velocity)

