import pygame

class Player (pygame.sprite.Sprite):
    def __init__(self, image, vector2):
        pygame.sprite.Sprite.__init__(self)

        self.vector2 = vector2

        # Set Player Object's image and position using given values:
        self.original_image = image
        self.image = image
        self.rect = self.image.get_rect(topleft = vector2)

    def update(self):
        pass

    def rotate(self, angle):#
        self.angle += angle
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect(center = self.rect.center)

    '''def dieFunct(self):
        print(f"Player died at {self.rect}")'''

def handleEvents(player, event):
    if event.type == pygame.MOUSEBUTTONDOWN:
        if player.rect.collidepoint(event.pos):
            player.rotate(45)
