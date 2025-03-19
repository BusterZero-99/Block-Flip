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

        setValues(self, ds)

        # Set window customisation to chosen values:
        self.window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.window_name)
        pygame.display.set_icon(self.icon)

        drawBackground(self, BasicSprite)
        drawGround(self, BasicSprite)

        drawUi(self, self.uiImgs, BasicSprite, self.width, self.height)

        drawPlayer(self, Player)

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
