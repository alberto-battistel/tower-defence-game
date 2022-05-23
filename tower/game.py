#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

from dataclasses import dataclass, field
import enum
 
import pygame
 
SCREENRECT = pygame.Rect(0,0,1024,800)
MOUSE_LEFT, MOUSE_MIDDLE, MOUSE_RIGHT = 1, 2, 3

class GameState(enum.Enum):
	"""
	Enum for the Game's State Machine. Every state represents a
	known game state for the game engine.
	"""
	
	# Unknown state, indicating possible error or misconfiguration
	unknown = "unknown"
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
	state: GameState
	game_menu: GameLoop = field(init=False, default=None)
	
	@classmethod
	def create(cls, fullscreen=False):
		game = cls(
			screen=None,
			screen_rect=SCREENRECT,
			fullscreen=fullscreen,
			state=GameState.initializing,
			)
		game.init()
		return game
		
	def set_state(self, new_state):
		self.state = new_state
		
	def assert_state_is(self, *expected_states:GameState):
		"""
		Asserts that the game engine is one of
		'expected_states'. If that assertion fails, raise
		'StateError'
		"""
		if not self.state in expected_states:
			raise StateError(
				f"Expected the game state to be one of {expected_states} not {self.state}"
				)
		
	def start_game(self):
		self.assert_state_is(GameState.initialized)
		self.set_state(GameState.main_menu)
		self.loop()
	
	def init(self):
		self.assert_state_is(GameState.initializing)
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
		self.game_menu = GameMenu(game=self)
		self.set_state(GameState.initialized)
		
	def loop(self):
		while self.state != GameState.quitting:
			if self.state == GameState.main_menu:
				self.game_menu.loop()
			elif self.state == GameState.map_editing:
				# ...etc...
			elif self.state == GameState.game_playing:
				# ...etc...
		self.quit()
		
	def quit(self):
		pygame.quit()	


@dataclass
class GameLoop:
	game: TowerGame
	
	def handle_events(self):
		"""
		Sample event handler that ensures quit events and normal event 
		loop processing takes place. Without this the game will hang and 
		repaints by the operating system will not happen, causing the 
		game window to hang.
		"""
		for event in pygame.event.get():
			if (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE) or
				event.type == pygame.QUIT:
				self.set_state(GameState.quitting)
			# Delegates the event to a sub-event handler 'handle_event'
			self.handle_event(event)
			
	def loop(self):
		while self.state != GameState.quitting:
			self.handle_events()
			
	def handle_event(self):
		"""
		Handles a singular event.
		"""
		
	# Convenient shortcut
	def set_state(self, new_state):
		self.game.set_state(new_state)
	
	@property
	def screen(self):
		return self.game.screen
		
	@property
	def state(self):
		return self.game.state

		
class GameMenu(GameLoop):
	pass


class GameEditing(GameLoop):
	pass
	
	
def start_game():
    game = TowerGame.create()
    game.loop()

if __name__ == '__main__':
    start_game()

