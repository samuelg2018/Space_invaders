class Explosion:
    def __init__(self, pg, window, explosion_x, explosion_y, invader):
        self.pg = pg
        self.window = window
        self.explosion_x = explosion_x
        self.explosion_y = explosion_y
        self.invader = invader
        self.counter = 0

        # Import and resize explosions
        self.explosion_green = [self.pg.image.load('media/sprites/Green_Explosion.png'),
                                self.pg.image.load('media/sprites/Green_Explosion_2.png')]
        self.explosion_green[0] = self.pg.transform.scale(self.explosion_green[0], (45, 35))
        self.explosion_green[1] = self.pg.transform.scale(self.explosion_green[1], (45, 35))

        self.explosion_blue = [self.pg.image.load('media/sprites/Blue_Explosion.png'),
                               self.pg.image.load('media/sprites/Blue_Explosion_2.png')]
        self.explosion_blue[0] = self.pg.transform.scale(self.explosion_blue[0], (45, 35))
        self.explosion_blue[1] = self.pg.transform.scale(self.explosion_blue[1], (45, 35))

        self.explosion_purple = [self.pg.image.load('media/sprites/Purple_Explosion.png'),
                                 self.pg.image.load('media/sprites/Purple_Explosion_2.png')]
        self.explosion_purple[0] = self.pg.transform.scale(self.explosion_purple[0], (45, 35))
        self.explosion_purple[1] = self.pg.transform.scale(self.explosion_purple[1], (45, 35))

    def draw(self):
        if self.invader.color == "greenA" or self.invader.color == "greenB":
            if self.counter % 10 <= 5:
                self.window.blit(self.explosion_green[0], (self.explosion_x, self.explosion_y))
            elif self.counter % 10 > 5:
                self.window.blit(self.explosion_green[1], (self.explosion_x, self.explosion_y))
        elif self.invader.color == "blueA" or self.invader.color == "blueB":
            if self.counter % 10 <= 5:
                self.window.blit(self.explosion_blue[0], (self.explosion_x, self.explosion_y))
            elif self.counter % 10 > 5:
                self.window.blit(self.explosion_blue[1], (self.explosion_x, self.explosion_y))
        elif self.invader.color == "purple":
            if self.counter % 10 <= 5:
                self.window.blit(self.explosion_purple[0], (self.explosion_x, self.explosion_y))
            elif self.counter % 10 > 5:
                self.window.blit(self.explosion_purple[1], (self.explosion_x, self.explosion_y))

        self.counter += 1

