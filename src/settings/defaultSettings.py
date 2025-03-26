import pygame
from src.scripts.resource_path import Path
from src.scripts.loadSpritesheet import loadSpritesheet

pygame.init()

# Variables:
# Designed to be a 3x4 aspect ratio
width = 288
height = 384
tile_size = 32
window_name = "Block Flip"

bg_colour = (0, 0, 0)

font        = pygame.font.Font(Path('./assets/fonts/MinecraftRegular-Bmg3.otf'), 32)
icon        = pygame.transform.scale(pygame.image.load(Path('./assets/images/icon.png')),        (tile_size, tile_size))
player_img  = pygame.transform.scale(pygame.image.load(Path('./assets/images/player.png')),      (tile_size, tile_size))
placeHolder = pygame.transform.scale(pygame.image.load(Path('./assets/images/placeHolder.png')), (tile_size, tile_size))

uiImgs = loadSpritesheet(Path('./assets/images/uiSpritesheet.png'), 8, 8, tile_size)
bgImgs = loadSpritesheet(Path('./assets/images/bgSpritesheet.png'), 16, 16, tile_size)
