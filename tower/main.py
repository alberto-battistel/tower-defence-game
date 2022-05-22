#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

from dataclasses import dataclass
 
import pygame
 
SCREENRECT = pygame.Rect(0,0,1024,800)
 
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

