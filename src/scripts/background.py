import pygame

def drawBackground(self, BackgroundSprite):

	# Create the background:
    self.background_group = pygame.sprite.Group()
    self.bgsprite = []
    k = 0

    # Draw background image positions:
    for i in range(0, self.width, 64):
        for j in range(0, self.height, 64):
            self.bgsprite.append(BackgroundSprite(self.background_image, (i, j),1))
            self.background_group.add(self.bgsprite[k])
            k += 1
            self.background_group.draw(self.window)