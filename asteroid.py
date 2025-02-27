from constants import *
from circleshape import CircleShape
from pygame import *
from player import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
                # inferred to be added based on the setup done for the Player class in player.py
                    # further it appears to use inheritance logic based on any "child" classes that use a parent of CircleShape
                    
        self.x = x
        self.y = y
        self.radius = radius
    

    def draw(self, surface):
            # surface pulls from pygame.sprite.Sprite
            # position is typically stored as self.position or (self.x, self.y)
            # will need to use radius as argument setup in draw

        pygame.draw.circle(surface, (255, 0, 255), (self.position.x, self.position.y), self.radius, 2)
                # surface calls to the *^[Circleshape class within the imported circleshape.py]
                    # which in turn pulls from pygame.sprite.Sprite
                        # @ hasattr >>> hasAttribute
                # COLOR refers to either using a RGB value or plain stated string
                # position is called to note*^, and is defined therein as pygame vector
                    # requires an X and Y pair (tuple) to be defined, 
                    # or can just be called using self.position, as it will look up the hierachy chain for values
                # radius is called to note*^ as well,
                    # which is inherited from [pygame.sprite.Sprite]
                        # https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.Sprite
                # value is for thickness of line around sprite generated
                    # 0 would be filled object
                    # 2 creates a line thickness of 2px
    

    def update(self, dt):
            # incl the argument for 'dt' as its part of the requirement for using the update() method

        self.position += self.velocity * dt
                # self.position is the value of the asteroid that is meant to be affected by its carried movement
                    # as part of the update call
                # it should be updated based on an incremental value of
                    # self.velocity >>> which exists within the CircleShape class
                    # dt >>> the delta time value which is also part of the CircleShape class
                            # !! really need to start using origin file as part of the property notation 
                            # to make this clearer as to where the variable is being collected  
                
        
