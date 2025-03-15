import pygame
from src.resource_path import Path

pygame.init()

# Variables:
# Designed to be a 3x4 aspect ratio
width = 288
height = 384
tile_size = 32
window_name = "Block Flip"

bg_colour = (0, 0, 0)

font = pygame.font.Font(Path('./assets/fonts/MinecraftRegular-Bmg3.otf'), 32)
icon = pygame.image.load(Path('./assets/images/icon.png'))
player_img = pygame.image.load(Path('./assets/images/player.png'))
bg_img1 = pygame.image.load(Path('./assets/images/sky1.png'))
bg_img2 = pygame.image.load(Path('./assets/images/sky2.png'))
placeHolder = pygame.image.load(Path('./assets/images/placeHolder.png'))
