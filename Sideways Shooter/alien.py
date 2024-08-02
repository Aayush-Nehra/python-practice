import pygame
from pygame.sprite import Sprite
from random import randint

class Alien(Sprite):
    def __init__(self, side_shooter):
        super().__init__()
        self.screen = side_shooter.screen
        self.settings = side_shooter.settings
        self.alien_type = "alien" + str(randint(1,6))

        self.image = pygame.transform.scale(pygame.image.load("images/"+self.alien_type + ".png"), (40,40))
        self.rect = self.image.get_rect()

        self.rect.x = self.settings.screen_width - 80
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
