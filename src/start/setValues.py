def setValues(self, pygame, ds):

    self.width = ds.width
    self.height = ds.height
    self.window_name = ds.window_name
    self.bg_colour = ds.bg_colour
    self.tile_size = ds.tile_size

    self.icon = ds.icon
    self.player_img = ds.player_img
    self.placeHolder = ds.placeHolder

    self.uiImgs = ds.uiImgs
    self.bgImgs = ds.bgImgs

    self.font = ds.font

    self.plat = 0


    self.platform_group = pygame.sprite.Group()
    self.psprite = []
