import pygame as pg
import random
import sys
import os

from game_setting import *
from new_tank import tank_game
from osu import Osu
from setting import setting1
from brick import brick
from pingpong import pingpong

# from achievements import Achievements


list_of_lines = []
list_of_color = []

all_sprites = pg.sprite.Group()
achievements_group = pg.sprite.Group()

GRAVITY = 1
screen_rect = (0, 0, WIDTH, HEIGHT)

ach = False


class Snow(pg.sprite.Sprite):
    # сгенерируем частицы разного размера
    fire = [pg.transform.scale(pg.image.load('./texture/menu/snow.png'), (10, 10))]

    def __init__(self):
        super().__init__(all_sprites)
        self.image = random.choice(self.fire)
        self.rect = self.image.get_rect()

        # координаты
        self.rect.x, self.rect.y = random.randint(0, 1000), random.randint(-70, -10)

        # гравитация будет одинаковой (значение константы)
        self.gravity = GRAVITY

    def update(self):
        # перемещаем частицу
        self.rect.y += GRAVITY

        # убиваем, если частица ушла за экран
        if not self.rect.colliderect(screen_rect):
            self.kill()


def create_snow():
    # количество создаваемых частиц
    snow_count = 10
    for i in range(snow_count):
        Snow()


def draw_bg_line(screen):
    line_thick = 15
    start_pos_x = -400
    start_pos_y = 700
    step = 25

    if list_of_lines == []:
        for i in range(100):
            ox = oy = random.randint(200, 500)
            color_bg_line = (0, 0, random.randint(200, 255))
            pg.draw.polygon(screen, color_bg_line, [(start_pos_x, start_pos_y), (start_pos_x + line_thick, start_pos_y),
                                                    (start_pos_x + line_thick + ox, start_pos_y - oy),
                                                    (start_pos_x + ox, start_pos_y - oy)])
            start_pos_x += line_thick + step
            list_of_lines.append(ox)
            list_of_color.append(color_bg_line)
    else:
        for i in range(100):
            ox = oy = list_of_lines[i]
            color = list_of_color[i]
            pg.draw.polygon(screen, color, [(start_pos_x, start_pos_y), (start_pos_x + line_thick, start_pos_y),
                                            (start_pos_x + line_thick + ox, start_pos_y - oy),
                                            (start_pos_x + ox, start_pos_y - oy)])
            start_pos_x += line_thick + step
            list_of_lines.append(ox)


def cursor(screen, number):
    mouse_pos = pg.mouse.get_pos()
    screen.blit(list_of_cursor[number], mouse_pos)


def terminate():
    pg.quit()
    sys.exit()


def achievement(image, screen):
    global x, y, ach

    if x >= WIDTH - ach_size and y == 0:
        x -= 2
        if x == WIDTH - ach_size:
            y += 0.5
    else:
        if x == WIDTH - ach_size:
            pass
        if x <= WIDTH:
            x += 2
        else:
            x = WIDTH
            y = 0
            ach = False
            return
    screen.blit(image, (x, y))


def start_menu():
    global ach
    pg.init()
    screen = pg.display.set_mode(size, pg.RESIZABLE)
    pg.display.set_caption(game_name)

    clock = pg.time.Clock()

    vol = 50
    vol1 = 50

    FPS = 60
    FPS1 = 60

    pg.mixer.music.load('./sounds/general/menu_fon.mp3')
    pg.mixer.music.set_volume(vol)
    pg.mixer.music.play(-1)

    button_clicked_sd = pg.mixer.Sound('./sounds/general/sounds_click.ogg')
    button_clicked_sd.set_volume(vol)

    nomber_of_cursor = 0

    f = open('./txt document/setting.txt', 'w')
    f.write('50\n')
    f.write('60\n')
    f.close()

    running = True

    screen.fill(BG_BLUE)

    tank_x, tank_y = 550, -300
    tank_button = pg.draw.rect(screen, BG_BLUE, (tank_button_pos[0], tank_button_pos[1], 100, 150), 1)
    tank_here = False

    osu_x, osu_y = 350, -200
    osu_button = pg.draw.rect(screen, BG_BLUE, (osu_button_pos[0], osu_button_pos[1], 100, 150), 1)
    osu_here = False

    stone_x, stone_y = 150, -100
    stone_button = pg.draw.rect(screen, BG_BLUE, (stone_button_pos[0], stone_button_pos[1], 100, 150), 1)
    stone_here = False

    snake_x, snake_y = 750, -400
    snake_button = pg.draw.rect(screen, BG_BLUE, (snake_pos[0], snake_pos[1], 100, 150), 1)
    snake_here = False

    exit_btn_x, exit_btn_y = 1050, 650

    exit_here = False

    setting_btn_x, setting_btn_y = -100, 640

    setting_here = False
    snow_back = False

    full_snow_pos_x, full_snow_pos_y = 0, 620
    snowman_pos_x, snowman_pos_y = 850, 500

    achievement_now = None

    while running:
        keys = pg.key.get_pressed()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                terminate()
            if event.type == pg.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if tank_button.collidepoint(mouse_pos):
                    if tank_here:
                        button_clicked_sd.play()
                        tank_game(vol1, FPS1, nomber_of_cursor)
                elif osu_button.collidepoint(mouse_pos):
                    if osu_here:
                        button_clicked_sd.play()
                        Osu(vol1, FPS1, nomber_of_cursor)
                elif stone_button.collidepoint(mouse_pos):
                    if stone_here:
                        button_clicked_sd.play()
                        brick(vol1, FPS1, nomber_of_cursor)
                        pg.display.set_mode(size)
                elif snake_button.collidepoint(mouse_pos):
                    if snake_here:
                        button_clicked_sd.play()
                        pingpong(vol1, FPS1, nomber_of_cursor)
                elif exit_btn.collidepoint(mouse_pos):
                    if exit_here:
                        button_clicked_sd.play()
                        terminate()
                elif setting_button.collidepoint(mouse_pos):
                    if setting_here:
                        button_clicked_sd.play()
                        vol1, FPS1, nomber_of_cursor1 = setting1(vol, FPS, nomber_of_cursor)
                        vol = vol1
                        FPS = FPS1
                        nomber_of_cursor = nomber_of_cursor1
                        button_clicked_sd.set_volume(vol)
                elif (snowman_pos_x + 40 < mouse_pos[0] < snowman_pos_x + 115) and \
                        (snowman_pos_y + 30 < mouse_pos[1] < snowman_pos_y + 170) and (nomber_of_cursor == 3) and \
                        not list_of_achievements[1]:
                    achievement_now = pg.image.load('./texture/achievements/snowman.png')
                    ach = True
                    list_of_achievements[1] = True

                try:
                    if shovel_hb.collidepoint(mouse_pos):
                        if not list_of_achievements[0]:
                            achievement_now = pg.image.load('./texture/achievements/snow.png')
                            ach = True
                            list_of_achievements[0] = True
                        snow_back = True
                except UnboundLocalError:
                    pass

        if snake_y < snake_pos[1]:
            stone_y += button_speed
            osu_y += button_speed
            tank_y += button_speed
            snake_y += button_speed
            if stone_y > stone_button_pos[1]:
                stone_y = stone_button_pos[1]
                stone_here = True
            if osu_y > osu_button_pos[1]:
                osu_y = osu_button_pos[1]
                osu_here = True
            if tank_y > tank_button_pos[1]:
                tank_y = tank_button_pos[1]
                tank_here = True
        else:
            snake_here = True
            if exit_btn_x > 0:
                exit_btn_x -= button_speed_exe
                setting_btn_x += button_speed_exe
            else:
                exit_here = True
                setting_here = True

        screen.fill(BG_BLUE)
        draw_bg_line(screen)
        create_snow()
        all_sprites.update()

        all_sprites.draw(screen)

        screen.blit(bbz_logo, bbz_logo_pos)
        screen.blit(r_steam, r_steam_pos)
        screen.blit(full_snow, (full_snow_pos_x, full_snow_pos_y))

        if not snow_back:
            if full_snow_pos_y > 95:
                full_snow_pos_y -= full_snow_speed
                exit_btn_y -= full_snow_speed
                setting_btn_y -= full_snow_speed
                exit_btn = pg.draw.rect(screen, BG_BLUE, (exit_btn_x, exit_btn_y, 50, 50), 1)
                setting_button = pg.draw.rect(screen, BG_BLUE, (setting_btn_x, setting_btn_y, 50, 50), 1)
                snowman_pos_y -= full_snow_speed
            else:
                screen.blit(shovel, shovel_pos)
                shovel_hb = pg.draw.rect(screen, BG_BLUE, (shovel_pos[0], shovel_pos[1], 20, 30), 1)

        else:
            take_fps = clock.tick(FPS)
            snow_speed = 100 * take_fps // 1000
            if full_snow_pos_y < 620:
                full_snow_pos_y += snow_speed
                exit_btn_y += snow_speed
                setting_btn_y += snow_speed
                exit_btn = pg.draw.rect(screen, BG_BLUE, (exit_btn_x, exit_btn_y, 50, 50), 1)
                setting_button = pg.draw.rect(screen, BG_BLUE, (setting_btn_x, setting_btn_y, 50, 50), 1)
                snowman_pos_y += snow_speed
            else:
                snow_back = False

        fps_now = str(clock.get_fps()).split('.')
        myfont = pg.font.SysFont('Digital-7 Mono', 50)
        if clock.get_fps() > 45:
            textsurface = myfont.render(str(fps_now[0]), False, GREEN)
        elif 25 < clock.get_fps() < 45:
            textsurface = myfont.render(str(fps_now[0]), False, YELLOW)
        else:
            textsurface = myfont.render(str(fps_now[0]), False, RED)
        screen.blit(textsurface, (0, 0))

        screen.blit(snowman, (snowman_pos_x, snowman_pos_y))
        screen.blit(stone, (stone_x, stone_y))
        screen.blit(osu, (osu_x, osu_y))
        screen.blit(tank, (tank_x, tank_y))
        screen.blit(snake, (snake_x, snake_y))
        screen.blit(exit_button, (exit_btn_x, exit_btn_y))
        screen.blit(setting, (setting_btn_x, setting_btn_y))

        if nomber_of_cursor != 0:
            pg.mouse.set_visible(0)
            if pg.mouse.get_focused():
                cursor(screen, nomber_of_cursor)
        else:
            pg.mouse.set_visible(1)

        if ach:
            achievement(achievement_now, screen)

        clock.tick(FPS1)
        pg.display.flip()

    pg.quit()


start_menu()
