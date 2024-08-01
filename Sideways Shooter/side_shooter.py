import sys
import pygame
from bullet import Bullet
from settings import Settings
from ship import Ship

class SideShooter():
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.settings.screen_height,self.settings.screen_width))
        self.ship = Ship(self)
        pygame.display.set_caption("Side Shooter")
        self.bullets = pygame.sprite.Group()
        self.bullet = Bullet(self)

    def run_game(self):
        while True:
            self._check_events()
            #update logic
            self.ship.move_ship()
            self.bullets.update()
            #render logic
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            if event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keyup_events(self, event):
        if event.key == pygame.K_UP:
            self.ship.move_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.move_down = False

    def _check_keydown_events(self, event):
        if event.key == pygame.K_UP:
            self.ship.move_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.move_down = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _fire_bullet(self):
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        for bullet in self.bullets.copy():
            if bullet.rect.x >= self.settings.screen_width:
                self.bullets.remove(bullet)
        pygame.display.flip()
        

if __name__ == '__main__':
    side_shooter = SideShooter()
    side_shooter.run_game()

