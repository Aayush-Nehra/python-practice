class Settings():
    def __init__(self) -> None:
        self.screen_height = 800
        self.screen_width = 800
        self.bg_color = (230, 230, 230)

        #ship settings
        self.ship_speed = 2

        #bullet settings
        self.bullet_color = (255,0,0)
        self.bullet_height = 2
        self.bullet_width = 5
        self.bullet_speed = 4
        self.no_of_active_bullet = 8