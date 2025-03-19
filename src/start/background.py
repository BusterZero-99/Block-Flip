import pygame
import random

def drawBackground(self, BackgroundSprite):

	# Create the background:
    self.background_group = pygame.sprite.Group()
    self.bgsprite = []
    k = 0

    # Draw background image positions:
    for i in range(0, self.width, self.tile_size):
        for j in range(0, self.height, self.tile_size):

            img = random.choice([self.bgImgs[0], self.bgImgs[1]])

            self.bgsprite.append(BackgroundSprite(img, (i, j),1))
            self.background_group.add(self.bgsprite[k])
            k += 1
            self.background_group.draw(self.window)
