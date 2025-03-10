import pygame

def spriteDetect(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            for sprite in self.bgsprite:
                if sprite.rect.collidepoint(x, y):

                    # Call sprite DIE function:
                    sprite.dieFunct()
                    self.bgsprite.remove(sprite)

def refreshBackground(self, event, drawBackground, BackgroundSprite):
	if event.type == pygame.KEYDOWN:
		if event.key == pygame.K_r:
			drawBackground(self, BackgroundSprite)

def checkCloseWindow(self, event):
    
    # Close Python instance when "X" button clicked:
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()