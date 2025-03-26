def drawPlatform(self, pygame, plat, BasicSprite, x, y, length):

    img = self.placeHolder
    x *= self.tile_size
    y *= self.tile_size

    for i in range(x, (self.tile_size*length) + x, self.tile_size):
        self.psprite.append(BasicSprite(img, (i, y), 2))
        self.platform_group.add(self.psprite[plat])
        plat += 1