import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, image, vector2, tile_size, platforms):
        pygame.sprite.Sprite.__init__(self)

        self.vector2 = vector2
        self.platforms = platforms
        self.tile_size = tile_size

        # Set Player Object's image and position using given values:
        self.original_image = image
        self.image = image
        self.rect = self.image.get_rect(topleft=vector2)

        # Other variable settings:
        self.angle = 0
        self.moving_up = False
        self.velocity_y = 0
        self.gravity = 1
        self.max_jump_height = 3 * self.tile_size
        self.jump_start_y = None

    def update(self):
        if self.moving_up:
            if self.jump_start_y is None:
                self.jump_start_y = self.rect.y
            if self.rect.y <= self.jump_start_y - self.max_jump_height:
                self.moving_up = False
            else:
                self.velocity_y = -self.max_jump_height / 10

        self.velocity_y += self.gravity
        self.rect.y += self.velocity_y

        # Check for collision with platforms
        if pygame.sprite.spritecollideany(self, self.platforms):
            self.rect.y -= self.velocity_y
            self.velocity_y = 0
            self.jump_start_y = None

    def rotate(self, angle):
        self.angle += angle
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect(center = self.rect.center)

    def start_move_up(self):
        if self.velocity_y == 0:
            self.moving_up = True
            self.rotate(-90)

def handlePlayerEvents(player, event):
    if event.type == pygame.MOUSEBUTTONDOWN:
        if player.rect.collidepoint(event.pos):
            player.start_move_up()
