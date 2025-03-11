import pygame


def updateWindow(self):
    self.window.fill(self.bg_colour)

    self.background_group.empty()
    self.background_group.add(self.bgsprite)
    self.background_group.draw(self.window)
    self.background_group.update()

    self.player_group.draw(self.window)
    self.player_group.update()

    # Update window:
    pygame.display.update()
    pygame.time.Clock().tick(60)
