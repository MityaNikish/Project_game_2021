import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, img, width, hight, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(img, (width, hight))
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)