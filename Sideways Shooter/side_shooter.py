import sys
import pygame
from bullet import Bullet
from settings import Settings
from ship import Ship
from alien import Alien

class SideShooter():
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.ship = Ship(self)
        pygame.display.set_caption("Side Shooter")
        self.bullets = pygame.sprite.Group()
        self.bullet = Bullet(self)
        self.aliens = pygame.sprite.Group()
        self._create_fleet()

    def _create_alien(self, x_pos, y_pos):
        alien = Alien(self)
        alien.x = x_pos
        alien.y = y_pos
        alien.rect.y = y_pos
        alien.rect.x = x_pos
        self.aliens.add(alien)

    def _create_fleet(self):
        alien = Alien(self)
        alein_width, alien_height = alien.rect.size
        current_x, current_y = self.settings.screen_width - 2 * alein_width, alien_height
        # print(current_x, self.settings.screen_width - 3 * alein_width)
        while current_x > (self.settings.screen_width - 15 * alein_width):
            while current_y < (self.settings.screen_height - 2 * alien_height):
                self._create_alien(current_x, current_y)
                current_y += 2 * alein_width
            current_y = alien_height
            current_x -= 2 * alein_width 

    def run_game(self):
        while True:
            self._check_events()
            #update logic
            self.ship.move_ship()
            self.bullets.update()
            self._update_aliens()
            
            #render logic
            self._update_screen()
            self.clock.tick(60)

    def _update_aliens(self):
        self.aliens.update()
        self._change_direction_and_drop_alien()

    def _change_direction_and_drop_alien(self):
        move_towards_ship = False
        for alien in self.aliens.sprites():
            if alien.rect.bottom == self.settings.screen_height:
                self.settings.move_down = -1
                move_towards_ship = True
            elif alien.rect.top == 0:
                self.settings.move_down = 1
                move_towards_ship = True
        if move_towards_ship == True:
            for alien in self.aliens.sprites():
                alien.rect.x -= self.settings.alien_speed * 10
            move_towards_ship = False

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
        self._destroy_aliens_hitting_bullet()
        self.ship.blitme()
        self._update_bullets()
        self.aliens.draw(self.screen)
        pygame.display.flip()

    def _update_bullets(self):
        for bullet in self.bullets.copy():
            if bullet.rect.x >= self.settings.screen_width:
                self.bullets.remove(bullet)
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()

    def _destroy_aliens_hitting_bullet(self):
        collisons = pygame.sprite.groupcollide(self.bullets, self.aliens, False, True)
        
if __name__ == '__main__':
    side_shooter = SideShooter()
    side_shooter.run_game()

