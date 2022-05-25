import pygame as pg
from game_setting import *
import sys


def terminate():
    pg.quit()
    sys.exit()


def cursor(screen, number):
    mouse_pos = pg.mouse.get_pos()
    screen.blit(list_of_cursor[number], mouse_pos)


def setting1(volume, fps, number_of_cursor):
    pg.init()

    screen = pg.display.set_mode(size)
    pg.display.set_caption('BBZv2')

    button_clicked_sd = pg.mixer.Sound('./sounds/general/sounds_click.ogg')
    button_clicked_sd.set_volume(volume)

    clock = pg.time.Clock()

    running = True
    go_back = False

    music_text_pos_x, music_text_pos_y = 482, 310
    setting_ball_pos_x, setting_ball_pos_y = 400, 530

    back_btn_hb = pg.draw.rect(screen, BG_BLUE, (back_btn_pos[0], back_button_pos[1], 50, 70), 1)
    delete_update_hb = pg.draw.rect(screen, BG_BLUE, (delete_update_pos[0], delete_update_pos[1], 150, 50), 1)

    while running:

        for event in pg.event.get():
            if event.type == pg.QUIT:
                terminate()

            if event.type == pg.MOUSEBUTTONDOWN:
                mouse_pos = pg.mouse.get_pos()
                if back_btn_hb.collidepoint(mouse_pos):
                    button_clicked_sd.play()
                    return volume, fps, number_of_cursor
                if volume_plus_hb.collidepoint(mouse_pos):
                    button_clicked_sd.play()
                    if volume <= 90:
                        volume += 10
                        if volume != 100:
                            aaa = float('0.' + str(int(volume)))
                        else:
                            aaa = 1
                    else:
                        volume = 0
                        aaa = 0
                    pg.mixer.music.set_volume(aaa)

                if fps_plus_hb.collidepoint(mouse_pos):
                    button_clicked_sd.play()
                    if fps < 90:
                        fps += 15
                    else:
                        fps = 15

                if volume_minus_hb.collidepoint(mouse_pos):
                    button_clicked_sd.play()
                    if volume >= 10:
                        volume -= 10
                        if volume != 0:
                            aaa = float('0.' + str(int(volume)))
                        else:
                            aaa = 0
                    else:
                        volume = 100
                        aaa = 1
                    pg.mixer.music.set_volume(aaa)

                if fps_minus_hb.collidepoint(mouse_pos):
                    button_clicked_sd.play()
                    if fps > 15:
                        fps -= 15
                    else:
                        fps = 90

                if cr_minus_hb.collidepoint(mouse_pos):
                    button_clicked_sd.play()
                    if number_of_cursor > 0:
                        number_of_cursor -= 1
                    else:
                        number_of_cursor = len(list_of_cursor) - 1

                if cr_plus_hb.collidepoint(mouse_pos):
                    button_clicked_sd.play()
                    if number_of_cursor < len(list_of_cursor) - 1:
                        number_of_cursor += 1
                    else:
                        number_of_cursor = 0

                if delete_update_hb.collidepoint(mouse_pos):
                    f = open('./txt document/updating.txt', 'w')
                    f.write('False')
                    f.close()
                    terminate()

        screen.fill(BG_BLUE)

        screen.blit(back_btn, back_btn_pos)
        screen.blit(setting_logo, setting_logo_pos)

        screen.blit(check_bg, (445, 300))
        screen.blit(check_bg, (445, 460))
        screen.blit(check_bg, (445, 570))

        screen.blit(list_of_cursor[number_of_cursor], (495, 575))

        volume_plus_hb = pg.draw.polygon(screen, BG_BLUE, [(plus_minus_pos_x, plus_minus_pos_y),
                                                           (plus_minus_pos_x, plus_minus_pos_y + 45),
                                                           (plus_minus_pos_x + 40, plus_minus_pos_y + 45 // 2)], 1)
        fps_plus_hb = pg.draw.polygon(screen, BG_BLUE, [(plus_minus_pos_x, plus_minus_pos_y_2),
                                                        (plus_minus_pos_x, plus_minus_pos_y_2 + 45),
                                                        (plus_minus_pos_x + 40, plus_minus_pos_y_2 + 45 // 2)], 1)
        cr_plus_hb = pg.draw.polygon(screen, BG_BLUE, [(plus_minus_pos_x, plus_minus_pos_y_2 + 110),
                                                       (plus_minus_pos_x, plus_minus_pos_y_2 + 155),
                                                       (plus_minus_pos_x + 40, plus_minus_pos_y_2 + 45 // 2 + 110)], 1)

        volume_minus_hb = pg.draw.polygon(screen, BG_BLUE, [(plus_minus_pos_x_2 + 40, plus_minus_pos_y),
                                                            (plus_minus_pos_x_2 + 40, plus_minus_pos_y + 45),
                                                            (plus_minus_pos_x_2, plus_minus_pos_y + 45 // 2)], 1)
        fps_minus_hb = pg.draw.polygon(screen, BG_BLUE, [(plus_minus_pos_x_2 + 40, plus_minus_pos_y_2),
                                                         (plus_minus_pos_x_2 + 40, plus_minus_pos_y_2 + 45),
                                                         (plus_minus_pos_x_2, plus_minus_pos_y_2 + 45 // 2)], 1)
        cr_minus_hb = pg.draw.polygon(screen, BG_BLUE, [(plus_minus_pos_x_2 + 40, plus_minus_pos_y_2 + 110),
                                                        (plus_minus_pos_x_2 + 40, plus_minus_pos_y_2 + 155),
                                                        (plus_minus_pos_x_2, plus_minus_pos_y_2 + 45 // 2 + 110)], 1)

        screen.blit(btn_plus, (plus_minus_pos_x, plus_minus_pos_y))
        screen.blit(btn_plus, (plus_minus_pos_x, plus_minus_pos_y_2))
        screen.blit(btn_plus, (plus_minus_pos_x, plus_minus_pos_y_2 + 110))

        screen.blit(btn_minus, (plus_minus_pos_x_2, plus_minus_pos_y))
        screen.blit(btn_minus, (plus_minus_pos_x_2, plus_minus_pos_y_2))
        screen.blit(btn_minus, (plus_minus_pos_x_2, plus_minus_pos_y_2 + 110))

        screen.blit(vol_text, vol_text_pos)
        screen.blit(fps_text, fps_text_pos)

        screen.blit(delete_update, delete_update_pos)

        myfont_vol = pg.font.SysFont('Digital-7 Mono1', 50)
        textsurface_vol = myfont_vol.render(str(volume), False, BLACK)
        if volume > 90:
            screen.blit(textsurface_vol, (music_text_pos_x - 10, music_text_pos_y))
        elif volume <= 0:
            screen.blit(textsurface_vol, (music_text_pos_x + 10, music_text_pos_y))
        else:
            screen.blit(textsurface_vol, (music_text_pos_x, music_text_pos_y))

        myfont_fps = pg.font.SysFont('Digital-7 Mono1', 50)
        textsurface_fps = myfont_fps.render(str(fps), False, BLACK)
        screen.blit(textsurface_fps, (482, 470))

        screen.blit(ball_wall, ball_wall_pos)

        pg.draw.circle(screen, RED, (setting_ball_pos_x + 15, setting_ball_pos_y + 15), 9, 0)
        pg.draw.circle(screen, DARK_RED, (setting_ball_pos_x + 15, setting_ball_pos_y + 15), 11, 2)

        take_fps = clock.tick(fps)
        speed_x = 100 * take_fps // 1000

        if setting_ball_pos_x < 670 and not go_back:
            setting_ball_pos_x += speed_x
        else:
            if setting_ball_pos_y < 632 and not go_back:
                setting_ball_pos_y += speed_x
            else:
                go_back = True
                if setting_ball_pos_x > 300:
                    setting_ball_pos_x -= speed_x
                else:
                    if setting_ball_pos_y > 530:
                        setting_ball_pos_y -= speed_x
                    else:
                        go_back = False

        if number_of_cursor == 0:
            pg.mouse.set_visible(1)
        else:
            pg.mouse.set_visible(0)
            if pg.mouse.get_focused():
                cursor(screen, number_of_cursor)

        pg.display.flip()
    pg.quit()


# setting1(50, 60, 0)
