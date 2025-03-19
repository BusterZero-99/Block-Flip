import pygame

def drawUi(self, sprites, spriteObject, width, height):

    self.ui_group = pygame.sprite.Group()
    self.bdsprite = []
    k = 0

	# Top border
    for x in range(0, width, self.tile_size):
        self.bdsprite.append(spriteObject(sprites[9], (x, 0),1))
        self.ui_group.add(self.bgsprite[k])
        k+=1


	# Bottom border
    for x in range(0, width, self.tile_size):
        self.bdsprite.append(spriteObject(sprites[25], (x, height - self.tile_size),1))
        self.background_group.add(self.bgsprite[k])
        k+=1

	# Left border
    for y in range(0, height, self.tile_size):
        self.bdsprite.append(spriteObject(sprites[16], (0, y),1))
        self.ui_group.add(self.bgsprite[k])
        k+=1

	# Right border
    for y in range(0, height, self.tile_size):
        self.bdsprite.append(spriteObject(sprites[18], (width - self.tile_size, y),1))
        self.ui_group.add(self.bgsprite[k])
        k+=1

    # Top-left corner
    self.bdsprite.append(spriteObject(sprites[8], (0, 0),1))
    self.ui_group.add(self.bgsprite[k])
    k += 1

	# Top-right corner
    self.bdsprite.append(spriteObject(sprites[10], (width - self.tile_size, 0),1))
    self.ui_group.add(self.bgsprite[k])
    k += 1

	# Bottom-left corner
    self.bdsprite.append(spriteObject(sprites[24], (0, height - self.tile_size),1))
    self.ui_group.add(self.bgsprite[k])
    k += 1

	# Bottom-right corner
    self.bdsprite.append(spriteObject(sprites[26], (width - self.tile_size, height - self.tile_size),1))
    self.ui_group.add(self.bgsprite[k])
