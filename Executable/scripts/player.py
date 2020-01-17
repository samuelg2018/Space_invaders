class Ship:
    def __init__(self, pg, window):
        self.window = window
        self.pg = pg

        self.score = 0
        self.lives = 3
        self.x = 587
        self.y = 640
        self.move_distance = 20
        self.counter = 0
        self.player_sprite = pg.image.load('media/sprites/Player.png')

    def draw_player(self):
        self.window.blit(self.player_sprite, (self.x, self.y))



