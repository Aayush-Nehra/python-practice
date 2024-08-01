import pygame
import sys
from bird import Bird

class BlueSky:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((500,500))
        pygame.display.set_caption("Blue Sky")
        self.bg_color = (173, 216, 230)
        self.bird = Bird(self)
    
    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.bg_color)
            self.bird.blitme()
            pygame.display.flip()

if __name__ == "__main__":
    blue_sky = BlueSky()
    blue_sky.run_game()

