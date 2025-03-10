import pygame

class TextSprite(pygame.sprite.Sprite):
    def __init__(self, text, font, vector2):
        pygame.sprite.Sprite.__init__(self)

        self.vector2 = vector2

        # Set Text Object's text and position using given values:
        self.text = text
        self.image = font.render(self.text, True, (255, 255, 255))
        self.rect = self.image.get_rect(topleft = vector2)