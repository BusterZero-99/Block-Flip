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

        setValues(self, pygame, ds)

        # Set window customisation to chosen values:
        self.window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.window_name)
        pygame.display.set_icon(self.icon)

        drawBackground(self, pygame, random, BasicSprite)
        drawGround(self, pygame, BasicSprite)

        drawPlatform(self, pygame, self.plat, BasicSprite, 2, 4, 4)
        drawPlatform(self, pygame, self.plat, BasicSprite, 3, 8, 2)
        drawPlatform(self, pygame, self.plat, BasicSprite, 1, 2, 2)
        drawPlatform(self, pygame, self.plat, BasicSprite, 3, 1, 6)

        drawUi(self, pygame, self.uiImgs, BasicSprite, self.width, self.height)

        drawPlayer(self, Player)

        print("Running...")

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
    print("Starting...")
    Main()
