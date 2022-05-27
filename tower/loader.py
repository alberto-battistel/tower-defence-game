#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import pygame

import importli.resources

def load(module_path, name):
	return import.resources.path(module_path, name)
	
def import_image(asset_name: str):
	with load("tower.assets.gfx", asset_name) as resource:
		return pygame.image.load(resource).convert_alpha() 

def import_sound(asset_name: str):
	"""
	Imports, as sound effect, 'asset_name'
	"""
	with load("tower.asset.audio", asset_name) as resource:
		return pygame.mixer.Sound(resource)
