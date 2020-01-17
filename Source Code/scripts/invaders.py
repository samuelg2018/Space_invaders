class Invader:
    def __init__(self, pg, window, x, y, invaders, color):
        self.pg = pg
        self.window = window
        self.x = x
        self.y = y
        self.invaders = invaders

        self.hitbox = (self.x, self.y, 60, 50)
        self.alive = True
        self.move_distance = 0.020
        self.orientation = "left"
        self.frame = 0
        self.counter = 0
        self.color = color

        # Game Over Text
        self.game_over_font = pg.font.Font("media/fonts/ARCADE_N.TTF", 30)
        self.game_over_txt = self.game_over_font.render("GAME OVER", 1, (240, 240, 240))

        # Load and resize invader sprites
        self.invader_green_a = [pg.image.load('media/sprites/Green_A_1.png'),
                                pg.image.load('media/sprites/Green_A_2.png')]
        self.invader_green_a[0] = pg.transform.scale(self.invader_green_a[0], (45, 35))
        self.invader_green_a[1] = pg.transform.scale(self.invader_green_a[1], (45, 35))

        self.invader_green_b = [pg.image.load('media/sprites/Green_B_1.png'),
                                pg.image.load('media/sprites/Green_B_2.png')]
        self.invader_green_b[0] = pg.transform.scale(self.invader_green_b[0], (45, 35))
        self.invader_green_b[1] = pg.transform.scale(self.invader_green_b[1], (45, 35))

        self.invader_blue_a = [pg.image.load('media/sprites/Blue_A_1.png'),
                               pg.image.load('media/sprites/Blue_A_2.png')]
        self.invader_blue_a[0] = pg.transform.scale(self.invader_blue_a[0], (45, 35))
        self.invader_blue_a[1] = pg.transform.scale(self.invader_blue_a[1], (45, 35))

        self.invader_blue_b = [pg.image.load('media/sprites/Blue_B_1.png'),
                               pg.image.load('media/sprites/Blue_B_2.png')]
        self.invader_blue_b[0] = pg.transform.scale(self.invader_blue_b[0], (45, 35))
        self.invader_blue_b[1] = pg.transform.scale(self.invader_blue_b[1], (45, 35))

        self.invader_purple = [pg.image.load('media/sprites/Purple_1.png'),
                               pg.image.load('media/sprites/Purple_2.png')]
        self.invader_purple[0] = pg.transform.scale(self.invader_purple[0], (45, 35))
        self.invader_purple[1] = pg.transform.scale(self.invader_purple[1], (45, 35))

    def update(self):
        if self.orientation == "left":
            if self.x >= 100:
                for i in range(len(self.invaders)):
                    self.invaders[i].x -= self.move_distance
            else:
                for i in range(len(self.invaders)):
                    self.invaders[i].y += 15
                    self.invaders[i].orientation = "right"

        elif self.orientation == "right":
            if self.x <= 1120:
                for j in range(len(self.invaders)):
                    self.invaders[j].x += self.move_distance
            else:
                for j in range(len(self.invaders)):
                    self.invaders[j].y += 15
                    self.invaders[j].orientation = "left"

    def draw(self):
        if self.alive:
            if self.frame % 10 <= 5:
                if self.color == "greenA":
                    self.window.blit(self.invader_green_a[0], (self.x, self.y))
                elif self.color == "greenB":
                    self.window.blit(self.invader_green_b[0], (self.x, self.y))
                elif self.color == "blueA":
                    self.window.blit(self.invader_blue_a[0], (self.x, self.y))
                elif self.color == "blueB":
                    self.window.blit(self.invader_blue_b[0], (self.x, self.y))
                elif self.color == "purple":
                    self.window.blit(self.invader_purple[0], (self.x, self.y))

            if self.frame % 10 > 5:
                if self.color == "greenA":
                    self.window.blit(self.invader_green_a[1], (self.x, self.y))
                elif self.color == "greenB":
                    self.window.blit(self.invader_green_b[1], (self.x, self.y))
                elif self.color == "blueA":
                    self.window.blit(self.invader_blue_a[1], (self.x, self.y))
                elif self.color == "blueB":
                    self.window.blit(self.invader_blue_b[1], (self.x, self.y))
                elif self.color == "purple":
                    self.window.blit(self.invader_purple[1], (self.x, self.y))
        self.frame += 0.25

