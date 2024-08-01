import pygame
import sys
from raindrop import Rain_Drop

class Game_Screen():
    def __init__(self) -> None:
        pygame.init()
        self.screen_width = 1200
        self.screen_height = 1000
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Raindrops")
        self.clock = pygame.time.Clock()

        self.raindrops = pygame.sprite.Group()
        #self._create_drops()
        self._create_raindrops()

    def _create_raindrops(self):
        """Create all drops on screen"""
        raindrop = Rain_Drop(self)
        drop_width, drop_height = raindrop.rect.size
        
        current_x, current_y = drop_width, drop_height

        while current_y < (self.screen_height - 10 * drop_height):
            while current_x < (self.screen_width - 2 * drop_width):
                self._create_raindrop(current_x, current_y)
                current_x += 2 * drop_width
            #Finished a row; reset x value, and increment y value
            current_x = drop_width
            current_y += 2 * drop_height

    def _create_raindrop(self, x_position, y_position):
        new_drop = Rain_Drop(self)
        new_drop.x = x_position
        new_drop.y = y_position
        new_drop.rect.x = x_position
        new_drop.rect.y = y_position

        # print("new_drop x:" + str(new_drop.x) + "new_drop y" + str(new_drop.y))
        self.raindrops.add(new_drop)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            # Make the most recently drawn screen visible.
            self.raindrops.update()

            self.screen.fill((0,0,0))
            self.raindrops.draw(self.screen)
            
            pygame.display.flip()
            self.clock.tick(60)

        
if __name__ == '__main__':
    # Make a game instance, and run the game.
    game_screen = Game_Screen()
    game_screen.run_game()