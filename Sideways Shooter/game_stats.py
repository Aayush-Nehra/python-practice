class GameStats:
    def __init__(self, aa_game) -> None:
        self.settings = aa_game.settings
        self.rem_lives = self.settings.no_of_lives

    def reset_game(self):
        self.rem_lives = self.settings.no_of_lives