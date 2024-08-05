import pygame

class Ship():
    def __init__(self, side_shooter) -> None:
        self.screen = side_shooter.screen
        self.settings = side_shooter.settings
        self.screen_rect = side_shooter.screen.get_rect()

        self.image = pygame.transform.rotate(pygame.image.load('images/ship.bmp'),-90)
        self.rect = self.image.get_rect()

        self.rect.midleft = self.screen_rect.midleft

        #continuous movement of ship
        self.move_up = False
        self.move_down = False
        
        #ship movement positon
        self.y = float(self.rect.y)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def move_ship(self):
        if self.move_up == True:
            self.y -= self.settings.ship_speed
        if self.move_down == True:
            self.y += self.settings.ship_speed

        self.rect.y = self.y 

    def center_ship(self):
        self.rect.midleft = self.screen_rect.midleft
