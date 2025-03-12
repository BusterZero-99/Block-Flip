import pygame

class Player (pygame.sprite.Sprite):
    def __init__(self, image, vector2):
        pygame.sprite.Sprite.__init__(self)

        self.vector2 = vector2

        # Set Player Object's image and position using given values:
        self.original_image = image
        self.image = image
        self.rect = self.image.get_rect(topleft = vector2)

        self.angle = 0

    def update(self):
        pass # I don't know what to do here...

    def rotate(self, angle):
        self.angle += angle
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect(center = self.rect.center)

    '''def dieFunct(self):
        print(f"Player died at {self.rect}")'''

def handlePlayerEvents(self, player, event):
    if event.type == pygame.MOUSEBUTTONDOWN:
        if player.rect.collidepoint(event.pos):
            player.rotate(-90) # Rotates player 90 degrees Clockwise
