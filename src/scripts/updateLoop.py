from src.settings.defaultImports import pygame, drawUi


def updateWindow(self):
    self.window.fill(self.bg_colour)

    self.background_group.empty()
    self.background_group.add(self.bgsprite)
    self.background_group.draw(self.window)
    self.background_group.update()

    self.ground_group.empty()
    self.ground_group.add(self.gsprite)
    self.ground_group.draw(self.window)
    self.ground_group.update()

    self.platform_group.empty()
    self.platform_group.add(self.psprite)
    self.platform_group.draw(self.window)
    self.platform_group.update()

    self.player_group.draw(self.window)
    self.player_group.update()

    self.ui_group.empty()
    self.ui_group.add(self.bdsprite)
    self.ui_group.draw(self.window)
    self.ui_group.update()


    # Update window:
    pygame.display.update()
    pygame.time.Clock().tick(60)
