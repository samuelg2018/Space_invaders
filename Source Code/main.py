import pygame as pg
from scripts.main_menu import boot_main
import scripts.default_values as default
from scripts.level_1 import boot_level_1


# Main
if __name__ == "__main__":
    # Window initialization
    pg.init()
    window = pg.display.set_mode((default.screen_x, default.screen_y))
    pg.display.set_caption("Space Invaders")

    # Sequence Variables
    running = True
    level = "main_menu"

    # Main Loop
    while running:
        # Scene Select
        if level == "main_menu":
            running, level = boot_main(window, pg)
        if level == "level_1":
            running, level = boot_level_1(window, pg)
    # Program Finalization
    pg.quit()
