import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, side_shooter) -> None:
        super().__init__()
        self.settings = side_shooter.settings
        self.color = self.settings.bullet_color
        self.screen = side_shooter.screen
        self.rect = pygame.Rect(0 ,0 , self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midleft = side_shooter.ship.rect.midright

        self.x = float(self.rect.x)

    def update(self):
        self.x += self.settings.bullet_speed
        self.rect.x = self.x

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)