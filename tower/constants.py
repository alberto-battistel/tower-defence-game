#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import pygame

SCREENRECT = pygame.Rect(0,0,1024,800)
MOUSE_LEFT, MOUSE_MIDDLE, MOUSE_RIGHT = 1, 2, 3
DESIRED_FPS = 40

# Mapping of sprite ID to asset filename
SPRITES = {
    "game_logo": "game_logo.png",
    "land": "land.png",
    "road": "road.png",
    "road_edge": "road_edge.png",
    "road_large_corner": "road_large_corner.png",
    "road_small_corner": "road_small_corner.png",
    "road_escape": "road_escape.png",
    "road_spawn": "road_spawn.png",
    "decor_1": "decor_1.png",
    "decor_2": "decor_2.png",
    "decor_3": "decor_3.png",
    "decor_4": "decor_4.png",
    "decor_5": "decor_5.png",
    "decor_6": "decor_6.png",
    "decor_7": "decor_7.png",
    "decor_8": "decor_8.png",
    "decor_10": "decor_10.png",
    "decor_11": "decor_11.png",
    "decor_12": "decor_12.png",
    "decor_13": "decor_13.png",
    "decor_14": "decor_14.png",
    "decor_15": "decor_15.png",
    "decor_16": "decor_16.png",
    "decor_17": "decor_17.png",
    "decor_18": "decor_18.png",
    "stone_1": "stone_1.png",
    "stone_2": "stone_2.png",
    "stone_3": "stone_3.png",
    "stone_4": "stone_4.png",
    "bush_1": "bush_1.png",
    "bush_3": "bush_3.png",
    "backdrop": "main_bg.png",
    "blank": "blank.png",
    "turret": "tower.png",
    "projectile": "rock.png",
}

# Holds the converted and imported sprite images. The key is a tuple
# of (flipped_x, flipped_y, sprite_name)
IMAGE_SPRITES: Dict[Tuple[bool, bool, str], pg.Surface] = {}

SOUNDS = {
    "footstep_1": "footstep01.ogg",
    "footstep_2": "footstep02.ogg",
    "footstep_3": "footstep03.ogg",
    "footstep_4": "footstep04.ogg",
    "thud": "thud.wav",
    "beep": "beep.ogg",
}

# Sound IDs to what they're used as.
SOUND_TURRET = "thud"
SOUND_FOOTSTEPS = "footstep_4"
SOUND_ESCAPED = "beep"
