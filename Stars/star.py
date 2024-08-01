import pygame
from pygame.sprite import Sprite
from random import Random

class Star(Sprite):
    def __init__(self, game_screen):
      super().__init__()
      self.screen = game_screen.screen
      
      self.image = pygame.transform.scale(pygame.image.load('images/star.png'), (50,50))
      self.rect = self.image.get_rect()

      self.rect.x = self.rect.width
      self.rect.y = self.rect.height

      self.x = float(self.rect.x)