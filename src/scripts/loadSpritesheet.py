import pygame

def loadSpritesheet(file_path, sprite_width, sprite_height, tile_size):

	# Load the spritesheet image
	spritesheet = pygame.image.load(file_path)
	
	# Get the dimensions of the spritesheet
	sheet_width, sheet_height = spritesheet.get_size()

	sprites = []
	
	# Loop through the spritesheet and extract each sprite
	for y in range(0, sheet_height, sprite_height):
		for x in range(0, sheet_width, sprite_width):

			sprite = pygame.transform.scale(spritesheet.subsurface(pygame.Rect(x, y, sprite_width, sprite_height)), (tile_size, tile_size))
			sprites.append(sprite)
	
	return sprites
