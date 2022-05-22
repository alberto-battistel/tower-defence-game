#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

from dataclasses import dataclass
import enum
 
import pygame
 
SCREENRECT = pygame.Rect(0,0,1024,800)

class GameState(enum.Enum):
	"""
	Enum for the Game's State Machine. Every state represents a
	known game state for the game engine.
	"""
	
	# Unknown state, indicating possible error or misconfiguration
	ukknown = "unknown"
	# The state the game engine would rightfully be set to before 
	# anything is initialized or configured.
	initializing = "initializing"
	# The game engine is initialized: pygame is configured, the sprites 
	# images are loaded, etc.
	initialized = "initialized"
	# The game engine is in map editing mode
	map_editing = "map_editing"
	# The game engine is in game playing mode
	game_playing = "game_playing"
	# The game is in the main menu
	main_menu = "main_menu"
	# the game engine is rendering the game ended screen
	game_ended = "game_ended"
	# The game engine is exiting und is unwinding
	quitting = "quitting"
	

class StateError(Exception):
	"""
	Raised if the game is in an unexpected game state at a point 
	where we expect it to be in a different state. For instance, to
	start in the game loop we must be initialized.
	"""


@dataclass
class TowerGame:
	
	screen: pygame.Surface
	screen_rect: pygame.Rect
	fullscreen: bool
	 
	@classmethod
	def create(cls, fullscreen=False):
		game = cls(
			screen=None,
			screen_rect=SCREENRECT,
			fullscreen=fullscreen,
			)
		game.init()
		return game
		
	def loop(self):
		pass
		
	def quit(self):
		pygame.quit()
		
	def start_game(self):
		self.loop()
		
	def init(self):
		pygame.init()
		window_style = pygame.FULLSCREEN if self.fullscreen else 0
		# We want 32 bits of color depth
		bit_depth = pygame.display.mode_ok(self.screen_rect.size, window_style, 32)
		screen = pygame.display.set_mode(self.screen_rect.size, window_style, bit_depth)
		pygame.mixer.pre_init(
			frequency=44100,
			size=32,
			channels=2,
			buffer=512,
			)
		pygame.font.init()
		self.screen = screen
			

def start_game():
    game = TowerGame.create()
    game.loop()

if __name__ == '__main__':
    start_game()

