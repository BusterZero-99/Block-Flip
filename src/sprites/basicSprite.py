import pygame

class BasicSprite (pygame.sprite.Sprite):
	def __init__(self, image, vector2, spriteType: int):
		pygame.sprite.Sprite.__init__(self)

		self.vector2 = vector2

		# Set Baisc Sprite's image and position using given values:
		self.image = image
		self.rect = self.image.get_rect(topleft = vector2)

	def update(self):
		pass

	def dieFunct(self):
		print(f"Sprite died at {self.vector2}")
		self.kill()
