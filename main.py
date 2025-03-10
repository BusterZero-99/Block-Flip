# Pygame boilerplate

from src.settings.defaultImports import * 

pygame.init()

class Main():
    def __init__(self):

        # Change values for different window size, name and icon:
        self.width = ds.width
        self.height = ds.height
        self.window_name = ds.window_name
        self.bg_colour = ds.bg_colour

        self.icon = ds.icon
        self.bg_img = ds.bg_img
        self.background_image = pygame.transform.scale(self.bg_img, (64, 64))

        self.font = ds.font

        # Set window customisation to chosen values:
        self.window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.window_name)
        pygame.display.set_icon(self.icon)

        drawBackground(self, BackgroundSprite)

        # Update window:
        self.update()

    def update(self):

        # Update loop:
        while True:

            # Get inputs:
            for event in pygame.event.get():

                checkCloseWindow(self, event)
                spriteDetect(self, event)

                refreshBackground(self, event, drawBackground, BackgroundSprite)

            self.window.fill(self.bg_colour)

            self.background_group.empty()
            self.background_group.add(self.bgsprite)
            self.background_group.draw(self.window)
            self.background_group.update()

            # Update window:
            pygame.display.update()
            pygame.time.Clock().tick(60)

if __name__ == "__main__":
    Main()
