def drawGround(self, pygame, BasicSprite):
    # Create the ground:
    self.ground_group = pygame.sprite.Group()
    self.gsprite = []
    k = 0
    img = self.placeHolder

    # Draw ground tiles only on the bottom row:
    for i in range(0, self.width, self.tile_size):
        self.gsprite.append(BasicSprite(img, (i, self.height - self.tile_size), 1))
        self.ground_group.add(self.gsprite[k])
        k += 1

    self.ground_group.draw(self.window)
