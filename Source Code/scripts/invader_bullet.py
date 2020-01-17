from random import randint


class InvaderBullet:
    def __init__(self, pg, window, invaders):

        self.pg = pg
        self.window = window
        self.invaders = invaders
        self.bullet_sprite = pg.image.load('media/sprites/i_Bullet.png')

        # Randomly select an invader's x and y
        selection = randint(0, len(self.invaders) - 1)
        self.random_x = self.invaders[selection].x + 22
        self.random_y = self.invaders[selection].y + 35

    def update(self):
        self.random_y += 10

    def draw(self):
        self.window.blit(self.bullet_sprite, (self.random_x, self.random_y))




