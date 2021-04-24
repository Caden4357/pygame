class Settings():
    # A class to store game settings
    def __init__(self):
        #initialize game settings and screen settings
        self.screen_width = 1200
        self.screen_height = 900
        self.bg_color = (135,206,250)

        #Bullet settings
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 16
        self.bullet_color = (60, 60, 60)