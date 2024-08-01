import pygame
from pygame.sprite import Sprite

class Rain_Drop(Sprite):
    def __init__(self, steady_rain_game):
        super().__init__()
        self.screen = steady_rain_game.screen
        self.color = (0, 0, 139)
        self.image = pygame.transform.scale(pygame.image.load('images/raindrop.png'), (30,30))
        self.rect = self.image.get_rect()
        self.rect.y = self.rect.height
        self.rect.x = self.rect.width
        self.drop_speed = 1.0

        self.y = float(self.rect.y)
        self.x = float(self.rect.x)
        

    def update(self):
        self.y += self.drop_speed
        self.rect.y = self.y
