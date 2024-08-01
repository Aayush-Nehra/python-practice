import pygame
import sys
from star import Star
from random import random

class Game_Screen():
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 1000))
        pygame.display.set_caption("Beautiful stars")
        self.clock = pygame.time.Clock()

        self.stars = pygame.sprite.Group()
        self._create_stars()


    def _create_stars(self):
        star = Star(self)
        star_width, star_height = star.rect.size
        current_x = star_width 
        current_y = star_height

        while current_y < (1000 - 2 * star_height):
            while current_x < (1200 - 2 * star_width):
                random_num = random()*5
                print(random_num)
                #random_num = 1
                self._create_star(current_x * random_num, current_y * random_num)
                current_x += 2 * star_width

            current_x = star_width
            current_y += 2 * star_height

    def _create_star(self, x_position, y_position):
        new_star = Star(self)
        new_star.x = x_position
        new_star.rect.x = x_position
        new_star.rect.y = y_position
        self.stars.add(new_star)
        

    def _draw_stars(self):
        self.stars.draw(self.screen)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            # Make the most recently drawn screen visible.

            self._draw_stars()

            pygame.display.flip()
            self.clock.tick(60)

if __name__ == '__main__':
    # Make a game instance, and run the game.
    game_screen = Game_Screen()
    game_screen.run_game()
        