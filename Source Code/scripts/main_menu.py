def boot_main(window, pg):
    # Import background image
    bg = pg.image.load('media/sprites/bg.png')

    # Import and resize images
    game_logo = pg.image.load("media/sprites/logo.png")
    game_logo = pg.transform.smoothscale(game_logo, (400, 200))

    green = pg.image.load("media/sprites/Green_A_1.png")
    green = pg.transform.scale(green, (60, 50))

    blue = pg.image.load("media/sprites/Blue_A_1.png")
    blue = pg.transform.scale(blue, (60, 50))

    purple = pg.image.load("media/sprites/Purple_1.png")
    purple = pg.transform.scale(purple, (60, 50))

    # Text
    game_font_import = pg.font.Font("media/fonts/ARCADE_N.TTF", 30)
    prompt_txt = game_font_import.render("PRESS ANY KEY TO PLAY", True, (240, 240, 240))
    green_txt = game_font_import.render("= 300 PTS", True, (0, 197, 0))
    blue_txt = game_font_import.render("= 200 PTS", True, (0, 198, 191))
    purple_txt = game_font_import.render("= 100 PTS", True, (179, 13, 209))

    clock = pg.time.Clock()

    # Main Menu Loop
    while True:
        # Local Keys
        for event in pg.event.get():
            # Closes game when close button is clicked
            if event.type == pg.QUIT:
                return False, "N/A"
            # Closes game with ESC key (27 means ESC)
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    return False, "N/A"
                else:
                    return True, "level_1"

        # Draws Background
        window.blit(bg, (0, 0))

        # Displays logo and message
        window.blit(game_logo, (440, 70))
        window.blit(prompt_txt, (330, 330))

        # Displays Score Breakdown
        window.blit(green, (440, 410))
        window.blit(blue, (440, 510))
        window.blit(purple, (440, 610))

        window.blit(green_txt, (540, 420))
        window.blit(blue_txt, (540, 520))
        window.blit(purple_txt, (540, 620))

        pg.display.update()
        clock.tick(30)

