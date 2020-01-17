from scripts.invaders import Invader
from scripts.player import Ship
from scripts.player_bullet import PlayerBullet
from scripts.invader_bullet import InvaderBullet
from scripts.explosions import Explosion


def game_over(pg, window, clock):
    font_import = pg.font.Font("media/fonts/ARCADE_N.TTF", 30)
    game_over_txt = font_import.render("GAME OVER", 1, (240, 240, 240))
    window.fill((0, 0, 0))
    window.blit(game_over_txt, (510, 400))
    pg.display.update()
    clock.tick(30)


def boot_level_1(window, pg):
    bullets = []
    invaders = []
    invader_bullets = []
    explosions = []
    player = Ship(pg, window)
    clock = pg.time.Clock()
    frame = 0
    counter = 0
    i_bullet_frame = 0

    # Load sound
    p_bullet_sound = pg.mixer.Sound("media/sound/shoot.wav")
    i_bullet_sound = pg.mixer.Sound("media/sound/invader_shoot.wav")
    i_explosion_sound = pg.mixer.Sound("media/sound/invader_killed.wav")
    p_explosion_sound = pg.mixer.Sound("media/sound/player_killed.wav")

    # Load background image
    bg = pg.image.load('media/sprites/bg.png')

    # Ready text
    game_font_import = pg.font.Font("media/fonts/ARCADE_N.TTF", 20)
    ready_txt = game_font_import.render("GET READY !!!", 1, (240, 240, 240))

    while True:
        for event in pg.event.get():
            # Closes Windows With Red X Button
            if event.type == pg.QUIT:
                return False, "N/A"
            # Closes Window with ESC key (27 means ESC)
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    return False, "N/A"
                # Shoots player bullet with space
                if event.key == pg.K_SPACE:
                    bullets.append(PlayerBullet(pg, window, player))  # Creates a new bullet every time you fire.
                    p_bullet_sound.play()

        if player.lives > 0:
            # Player Movement
            keys = pg.key.get_pressed()
            if keys[pg.K_LEFT] and player.x > 20:
                player.x -= player.move_distance
            elif keys[pg.K_RIGHT] and player.x < 1200:
                player.x += player.move_distance

            # Create Text
            score_txt = game_font_import.render("Score:" + str(player.score), 1, (240, 240, 240))
            lives_txt = game_font_import.render("Lives:" + str(player.lives), 1, (240, 240, 240))

            # Draw background
            window.blit(bg, (0, 0))

            # Show "get ready" text and spawn invaders
            if frame < 60:
                window.blit(ready_txt, (510, 400))
            if frame == 60:
                for i in range(11):
                    invaders.append(Invader(pg, window, 300 + (70 * i), 120, invaders, "greenA"))
                    invaders.append(Invader(pg, window, 300 + (70 * i), 180, invaders, "greenB"))
                    invaders.append(Invader(pg, window, 300 + (70 * i), 240, invaders, "blueA"))
                    invaders.append(Invader(pg, window, 300 + (70 * i), 300, invaders, "blueB"))
                    invaders.append(Invader(pg, window, 300 + (70 * i), 360, invaders, "purple"))

            # Draw and updates invaders
            for invader in invaders:
                invader.update()
                invader.draw()

            # Draw explosions
            for explosion in explosions:
                explosion.explosion_x = explosion.invader.x
                explosion.explosion_y = explosion.invader.y
                explosion.draw()

            if explosions:
                if explosions[0].counter == 10:
                    explosions = explosions[1:]

            # Invader bullets creation
            if i_bullet_frame == 60:
                invader_bullets.append(InvaderBullet(pg, window, invaders))  # Creates a new bullet every time you fire.
                i_bullet_sound.play()
                i_bullet_frame = 0

            # Invader collision
            if len(bullets) > 0:
                invader_hit = False
                for invader in invaders:
                    if invader.alive:
                        for bullet_index, bullet in enumerate(bullets):
                            if invader.x <= bullet.x <= invader.x + 45 and invader.y <= bullet.y <= invader.y + 35:
                                invader.alive = False
                                invader_hit = True

                                explosion_x = invader.x
                                explosion_y = invader.y

                                explosions.append(Explosion(pg, window, explosion_x, explosion_y, invader))

                                if invader.color == "greenA" or invader.color == "greenB":
                                    player.score += 300
                                elif invader.color == "blueA" or invader.color == "blueB":
                                    player.score += 200
                                elif invader.color == "purple":
                                    player.score += 100
                                break
                        else:
                            continue
                        break
                if invader_hit:
                    i_explosion_sound.play()
                    del bullets[bullet_index]

            # Player collision
            if invader_bullets:
                if player.lives != 0:
                    for i_bullet_index, i_bullet in enumerate(invader_bullets):
                        if player.x <= i_bullet.random_x <= player.x + 53 and player.y <= i_bullet.random_y + 34 <= player.y + 62:
                            player.lives -= 1
                            p_explosion_sound.play()
                            invader_bullets = invader_bullets[1:]
                            break

            # Draw player sprite
            player.draw_player()

            # Draw player bullets
            skip_index = 0
            for bullet in bullets:
                if bullet.y < -50:
                    skip_index += 1
                    continue

                bullet.update()
                bullet.draw()

            # Draw invader bullets
            skip_index_2 = 0
            if frame > 60:
                for i_bullet in invader_bullets:
                    if i_bullet.random_y > 720:
                        skip_index_2 += 1
                        continue

                    i_bullet.update()
                    i_bullet.draw()

            # Erases bullets outside of the screen
            bullets = bullets[skip_index:len(bullets)]
            invader_bullets = invader_bullets[skip_index_2:len(invader_bullets)]

            # Draw text for Score and Lives
            window.blit(score_txt, (30, 10))
            window.blit(lives_txt, (1100, 10))

            # If invaders reach the bottom
            for invader in range(len(invaders)):
                if invaders[invader].y > 600:
                    if counter < 70:
                        game_over(pg, window, clock)
                        counter += 1
                    else:
                        return True, "main_menu"

            pg.display.update()
            clock.tick(30)  # Set game to 30 fps.
            frame += 1
            i_bullet_frame += 1

        else:
            if counter < 70:
                game_over(pg, window, clock)
                counter += 1
            else:
                return True, "main_menu"
