# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from asteroid import *
from player import *
from asteroidfield import *
from circleshape import *				
# import constants				
		# imports from modules for use in main.py
from constants import *
		# states what to import from what module
		# using * denotes all datasets that exist in that module
			# similar to SQL in coding~



def main():
		# core function

	pygame.init()
			# initializes pygame module, the core game "node"

	print(f"Starting Asteroids!")
			# statement on game, v/

	print(f"Screen width: {SCREEN_WIDTH}")
			# statement on game, v/
				# states out width of 1280

	print(f"Screen height: {SCREEN_HEIGHT}")
			# statement on game, v/
				# states out height of 720


	clock = pygame.time.Clock()
			# builds a clock constructor off of the sub-module of time within the module of pygame
			# captured within the variable of [clock]
	dt = 0
			# creates a variable for recording frames that have occured, "delta time", or "change of time"


	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
			# defines screen size of game, per above references and statements


	updateable = pygame.sprite.Group()
			# defines for sprites that need to be updated
	drawable = pygame.sprite.Group()
			# groups to house objects that fall under update() & draw() methods
	asteroids = pygame.sprite.Group()
			# group to house the asteroids generated through asteroid.py file & class/methods
	shots = pygame.sprite.Group()
			# group to house the shots fired from player ship

	Player.containers = (updateable, drawable)
			# applies the Player class to the 2 groups via container property
	
	Asteroid.containers = (asteroids, updateable, drawable)
			# applies the Asteroid class to the 2 groups via container property
	
	AsteroidField.containers = (updateable,)
			# applies to the AsteroidField class, which is not repeat drawn & is not an Asteroid, but a fixed field that is updated

	Shot.containers = (updateable, drawable, shots)
	

	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
			# defines where the player should spawn in relation to the screen

	asteroid_field = AsteroidField()


	while True:
				# creates infinite loop to run game
					# ~ turns on the game file

		for event in pygame.event.get():	
					# creates an instance to check the events that occur within the game environment

			if event.type == pygame.QUIT:
						# notes instance of what to occur when the event type is "quitting the game"

				return
							# allow it to occur without issue
		

		screen.fill(color=(0,0,0), rect=None, special_flags=0)
				# render the screen based on properties
						# black , no special size, no special flag
						# https://www.pygame.org/docs/ref/surface.html#pygame.Surface.fill <~ reff
		


		dt = clock.tick(60) / 1000
				# creates a time notation to process loops at 1/60th of a millisecond
		
		# player.update(dt)
					# disabling to reference instead with Groups
		
		for updatez in updateable:
			updatez.update(dt)
				# method call to refresh the movement of the player character based on key pressed
		#			# print(f"Number of asteroids: {len(asteroids)}")
				# q?^^ ~ troubleshooting why asteroids are not visibly spawning on screen

		# player.draw(screen)
					# disabling to reference instead with Groups							
		for thing in drawable:
			thing.draw(screen)
					# places the player into the render

		for asteroid in asteroids:
				# ! goal is to check if the Player is colliding with Asteroids as they generate
					# uses a for Loop to iterate each item that exists within the asteroids group
						# defined above within main.py

			if player.collisions(asteroid):
					# defines a check using the player variable, with the collisions method, against asteroid instance
						# the method itself can only return a True or False as part of its code
				
				# action defined to occur if True is returned
				print("Game over!")
						# generates in the console
				sys.exit()
						# trigger closing of the game
		

		pygame.display.flip()
				# calls a refresh of the renderer, infinitely unless an event occurs to stop
		
	

if __name__ == "__main__":
	main()


