import pygame

# Base class for game objects

class CircleShape(pygame.sprite.Sprite):
    
    def __init__(self, x, y, radius):
        # we will be using this later
        
        if hasattr(self, "containers"):
            super().__init__(self.containers)
                # ? hasattr = hasAttribute
        
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def collisions(self, other_circle):
            # 2nd argument can be named as anything, as its meant to capture for a value for use

        distance = self.position.distance_to(other_circle.position)
                # variable of distance is generated through
                    # self.position (referencing to 1st object relative position)
                    # then calculate the distance to other_circle.position
                        # using .distance_to() method off of self.position

        if self.radius >= distance or other_circle.radius >= distance:
                # compares the self.radius OR other_circle.radius against the value of [distance]
            return True
                    # returns True to confirm collision is occurring


    def draw(self, screen):
        
        # sub-classes must override
        pass

    def update(self, dt):
        
        # sub-classes must override
        pass
