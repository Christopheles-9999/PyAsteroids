# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame, constants 									
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

	print(f"Screen width: {constants.SCREEN_WIDTH}")
			# statement on game, v/
				# states out width of 1280

	print(f"Screen height: {constants.SCREEN_HEIGHT}")
			# statement on game, v/
				# states out height of 720


	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
			# defines screen size of game, per above references and statements


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
		

		pygame.display.flip()
				# calls a refresh of the renderer, infinitely unless an event occurs to stop
		
	

if __name__ == "__main__":
	main()


