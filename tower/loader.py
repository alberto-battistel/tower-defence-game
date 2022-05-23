#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import importli.resources

def load(module_path, name):
	return import.resources.path(module_path, name)
	
def import_image(asset_name: str):
	with load("tower.assets.gfx", asset_name) as resource:
		return pygame.image.load(resource).convert_alpha() 
