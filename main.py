# 𝔹𝕝𝕠𝕔𝕜 𝔽𝕝𝕚𝕡

'''

This is a basic game I am developing called "𝔹𝕝𝕠𝕔𝕜 𝔽𝕝𝕚𝕡".
This is made from 𝚝𝚎𝚛𝚛𝚒𝚋𝚕𝚎 code.
Add 𝔰𝔲𝔤𝔤𝔢𝔰𝔱𝔦𝔬𝔫𝔰 please. Please add bug issues.

The font used (MinecraftRegular-Bmg3.otf) has been unmodified, and was created by 𝕁𝔻𝔾𝕣𝕒𝕡𝕙𝕚𝕔𝕤.
It is issued under the ᴘᴜʙʟɪᴄ ᴅᴏᴍᴀɪɴ from fontspace.com

I created the new textures myself.

'''

from src.settings.defaultImports import *

pygame.init()

class Main():
    def __init__(self):

        # Change values for different window size, name and icon:
        self.width = ds.width
        self.height = ds.height
        self.window_name = ds.window_name
        self.bg_colour = ds.bg_colour
        self.tile_size = ds.tile_size

        self.icon = pygame.transform.scale(ds.icon, (self.tile_size, self.tile_size))
        self.player_img = pygame.transform.scale(ds.player_img, (self.tile_size, self.tile_size))
        self.bg_img1 = pygame.transform.scale(ds.bg_img1, (self.tile_size, self.tile_size))
        self.bg_img2 = pygame.transform.scale(ds.bg_img2, (self.tile_size, self.tile_size))
        self.placeHolder = pygame.transform.scale(ds.placeHolder, (self.tile_size, self.tile_size))

        self.font = ds.font

        # Set window customisation to chosen values:
        self.window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.window_name)
        pygame.display.set_icon(self.icon)

        drawBackground(self, BasicSprite)

        drawGround(self, BasicSprite)

        self.player = Player(self.player_img, (self.width / 2 - self.tile_size/2, self.height - self.tile_size * 2), self.tile_size, self.ground_group)

        self.player_group = pygame.sprite.Group()
        self.player_group.add(self.player)

        # Update window:
        self.update()

    def update(self):

        # Update loop:
        while True:

            # Get inputs:
            for event in pygame.event.get():

                checkCloseWindow(self, event)
                spriteDetect(self, event)
                handlePlayerEvents(self.player, event)

                refreshBackground(self, event, drawBackground, BasicSprite)

            updateWindow(self)

if __name__ == "__main__":
    Main()
