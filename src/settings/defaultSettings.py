import pygame
from src.resource_path import Path

pygame.init()

# Variables:
width = 270
height = 600 
window_name = "Block Flip"

bg_colour = (0, 0, 0)

font = pygame.font.Font(Path('./assets/fonts/MinecraftRegular-Bmg3.otf'), 32)
icon = pygame.image.load(Path('./assets/images/icon_file.png'))
dirt = pygame.image.load(Path('./assets/images/dirt.png'))