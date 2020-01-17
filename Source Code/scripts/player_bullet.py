class PlayerBullet:
    def __init__(self, pg, window, player):

        self.pg = pg
        self.window = window
        self.bullet_sprite = pg.image.load('media/sprites/P_Bullet.png')
        self.y = 600
        self.x = player.x + 26.5

    def update(self):
        self.y -= 30

    def draw(self):
        self.window.blit(self.bullet_sprite, (self.x, self.y))
