import pygame as pg
import pymunk as pm
import sys
from random import randint, choice

from game_setting import *

balls_speed_list = [-ball_speed, ball_speed]
list_of_ball = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ach_list = []
timer_active = False
ach = False


class Ball:
    def __init__(self, ball_speed_list1, space, screen, volume):
        self.body = pm.Body()
        self.body.position = self.x, self.y = randint(no_border_size_on_x + ball_radius,
                                                      osu_field_length - ball_radius), randint(
            no_border_size_on_y + ball_radius, osu_field_height - ball_radius)
        self.catch = False
        self.body.velocity = choice(ball_speed_list1), choice(ball_speed_list1)
        self.shape = pm.Circle(self.body, ball_radius)

        self.shape.density = 1
        self.shape.elasticity = 1
        space.add(self.body, self.shape)

        self.ball_broke = pg.mixer.Sound('./sounds/osu/ball_broke.mp3')
        self.ball_broke.set_volume(volume)

        self.ball_tp = pg.mixer.Sound('./sounds/osu/ball_tp.mp3')
        self.ball_tp.set_volume(volume)

    def draw(self, name, screen, *args):
        pg.draw.circle(screen, WHITE, (self.body.position.x, self.body.position.y), ball_radius)
        self.ball_hb = pg.draw.circle(screen, DARK_GRAY, (self.body.position.x, self.body.position.y), ball_radius, 1)

        pg.font.init()
        myfont = pg.font.SysFont('Comic Sans MS', 25)
        textsurface = myfont.render(str(name), False, (0, 0, 0))
        screen.blit(textsurface, (self.body.position.x - 10, self.body.position.y - ball_radius))

        pg.key.set_repeat(100, 70)
        if not self.catch:
            if args and args[0].type == pg.MOUSEBUTTONDOWN and \
                    self.ball_hb.collidepoint(args[0].pos):
                ach_list.append(1)
                if name == list_of_ball[0]:
                    self.ball_broke.play()
                    pg.draw.circle(screen, DARK_GRAY, (self.body.position.x, self.body.position.y), ball_radius)
                    screen.blit(breake, (self.body.position.x, self.body.position.y))

                    self.body.position = self.x, self.y = 50, 250
                    self.body.velocity = 10, 10

                    self.catch = True
                    list_of_ball.pop(0)

                else:
                    self.ball_tp.play()
                    self.body.position = self.x, self.y = randint(no_border_size_on_x + ball_radius,
                                                                  osu_field_length - ball_radius), randint(
                        no_border_size_on_y + ball_radius, osu_field_height - ball_radius)

    def new_game(self):
        self.body.position = self.x, self.y = 0, 0
        list_of_ball = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def add_wall(p1, p2, space):
    body = pm.Body(body_type=pm.Body.STATIC)
    shape = pm.Segment(body, p1, p2, 20)
    shape.elasticity = 1
    space.add(body)
    space.add(shape)


def wall_create(space):
    add_wall((no_border_size_on_x, no_border_size_on_y),
             (no_border_size_on_x, HEIGHT - no_border_size_on_y), space)
    add_wall((no_border_size_on_x, no_border_size_on_y),
             (WIDTH - no_border_size_on_x, no_border_size_on_y), space)
    add_wall((no_border_size_on_x, HEIGHT - no_border_size_on_y),
             (WIDTH - no_border_size_on_x, HEIGHT - no_border_size_on_y), space)
    add_wall((WIDTH - no_border_size_on_x, no_border_size_on_y),
             (WIDTH - no_border_size_on_x, HEIGHT - no_border_size_on_y), space)

    add_wall((25, 200),
             (175, 200), space)
    add_wall((175, 200),
             (175, 500), space)
    add_wall((175, 500),
             (25, 500), space)
    add_wall((25, 500),
             (25, 200), space)


def ball_create():
    pass


def timer(count, screen, number_list):
    now_time = str(count)
    if len(now_time) == 1:
        screen.blit(number_list[int(now_time[0])], ((first_timer_number[0] - 20), first_timer_number[1]))
    elif len(now_time) == 2:
        screen.blit(number_list[int(now_time[0])], ((first_timer_number[0] - 30), first_timer_number[1]))
        screen.blit(number_list[int(now_time[1])], ((first_timer_number[0]), first_timer_number[1]))
    elif len(now_time) == 3:
        screen.blit(number_list[int(now_time[0])], ((first_timer_number[0] - 60), first_timer_number[1]))
        screen.blit(colon, ((first_timer_number[0] - 30), first_timer_number[1]))
        screen.blit(number_list[int(now_time[1])], ((first_timer_number[0] - 10), first_timer_number[1]))
        screen.blit(number_list[int(now_time[2])], ((first_timer_number[0] + 25), first_timer_number[1]))
    elif len(now_time) == 4:
        screen.blit(number_list[int(now_time[0])], ((first_timer_number[0] - 80), first_timer_number[1]))
        screen.blit(number_list[int(now_time[1])], ((first_timer_number[0] - 45), first_timer_number[1]))
        screen.blit(colon, ((first_timer_number[0] - 15), first_timer_number[1]))
        screen.blit(number_list[int(now_time[2])], ((first_timer_number[0] + 5), first_timer_number[1]))
        screen.blit(number_list[int(now_time[3])], ((first_timer_number[0] + 45), first_timer_number[1]))


def game_over(screen, cause, number_list, time):
    if cause == 'time':
        screen.blit(no_time, no_time_pos)
        screen.blit(time_out, time_out_pos)
        count = 10 - len(list_of_ball)
        screen.blit(number_list[count], (660, 300))
    if cause == 'ball':
        screen.blit(win_logo, win_logo_pos)
        timer(time, screen, number_list)
    screen.blit(restart_btn, restart_btn_pos)


def cursor(screen, number):
    mouse_pos = pg.mouse.get_pos()
    screen.blit(list_of_cursor[number], mouse_pos)


def achievement(image, screen):
    global x, y, ach

    if x >= WIDTH - ach_size and y == 0:
        x -= 1
        if x == WIDTH - ach_size:
            y += 0.5
    else:
        if x == WIDTH - ach_size:
            pass
        if x <= WIDTH:
            x += 1
        else:
            x = WIDTH
            y = 0
            ach = False
            return
    screen.blit(image, (x, y))


def terminate():
    pg.quit()
    sys.exit()


def Osu(volume, FPS, nomber_of_cursor):
    global ach
    pg.init()
    pg.mixer.init()

    button_clicked_sd = pg.mixer.Sound('./sounds/general/sounds_click.ogg')
    button_clicked_sd.set_volume(volume)

    screen = pg.display.set_mode((size))
    space = pm.Space()

    clock = pg.time.Clock()

    number_list = []
    for i in range(10):
        number_list.append(pg.image.load(f'./texture/osu/time_number/{i}.png'))
    start_btn_now = start_btn
    dif_color_now = WHITE

    osu_play = True
    game_start = False

    end_game = False

    seconds = 0
    mil = 0
    sec = 0
    minutes = 0

    achievement_now = None

    while osu_play:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                terminate()
            if event.type == pg.MOUSEBUTTONDOWN:
                mouse_pos = pg.mouse.get_pos()

                if exit_btn_hb.collidepoint(mouse_pos):
                    button_clicked_sd.play()
                    try:
                        for ball in balls:
                            ball.new_game()
                        list_of_ball.clear()
                        for i in range(1, 11):
                            list_of_ball.append(i)
                    except UnboundLocalError:
                        pass
                    return
                try:
                    if restart_btn_hb.collidepoint(mouse_pos) and game_start and end_game:
                        button_clicked_sd.play()
                        end_game = False
                        game_start = False
                        dif_color_now = WHITE
                        start_btn_now = start_btn
                        seconds = 0
                        mil = 0
                        sec = 0
                        minutes = 0
                        for ball in balls:
                            ball.new_game()

                        for i in range(1, 11):
                            list_of_ball.append(i)
                except UnboundLocalError:
                    pass

                if not game_start:
                    if start_btn_hb.collidepoint(mouse_pos) and dif_color_now != WHITE:
                        button_clicked_sd.play()
                        game_start = True
                        timer_active = True
                        balls = [Ball(balls_speed_list, space, screen, volume) for _ in range(10)]
                        wall_create(space)
                    elif ez_btn_hb.collidepoint(mouse_pos):
                        button_clicked_sd.play()
                        ball_speed = 100
                        balls_speed_list = [-ball_speed, ball_speed]
                        start_btn_now = start_btn_green
                        dif_color_now = BTN_GREEN

                    elif normal_btn_hb.collidepoint(mouse_pos):
                        button_clicked_sd.play()
                        ball_speed = 250
                        balls_speed_list = [-ball_speed, ball_speed]
                        start_btn_now = start_btn_yellow
                        dif_color_now = BTN_YELLOW
                    elif hard_btn_hb.collidepoint(mouse_pos):
                        button_clicked_sd.play()
                        ball_speed = 600
                        balls_speed_list = [-ball_speed, ball_speed]
                        dif_color_now = BTN_RED
                        start_btn_now = start_btn_red
                    elif impossible_btn_hb.collidepoint(mouse_pos):
                        button_clicked_sd.play()
                        ball_speed = 750
                        balls_speed_list = [-ball_speed, ball_speed]
                        dif_color_now = BTN_PERPLE
                        start_btn_now = start_btn_perple

        screen.fill(DARK_GRAY)
        screen.blit(logo, logo_pos)
        pg.draw.rect(screen, dif_color_now, (no_border_size_on_x, no_border_size_on_y,
                                             osu_field_length, osu_field_height), 1)
        pg.draw.rect(screen, dif_color_now, (25, 200, 150, 300), 1)

        screen.blit(exit_btn, exit_btn_pos)
        exit_btn_hb = pg.draw.rect(screen, DARK_GRAY, (0, 630, 70, 70), 1)

        if not game_start:

            screen.blit(dif_logo, (dif_logo_pos))

            screen.blit(ez_btn, (ez_btn_pos))
            screen.blit(normal_btn, (normal_btn_pos))
            screen.blit(hard_btn, (hard_btn_pos))
            screen.blit(impossible_btn, (impossible_btn_pos))
            screen.blit(start_btn_now, (start_btn_pos))

            # hb = hitbox
            start_btn_hb = pg.draw.rect(screen, DARK_GRAY, (start_btn_pos[0], start_btn_pos[1], 130, 50), 1)
            ez_btn_hb = pg.draw.rect(screen, DARK_GRAY, (ez_btn_pos[0], ez_btn_pos[1], 50, 50), 1)
            normal_btn_hb = pg.draw.rect(screen, DARK_GRAY, (normal_btn_pos[0], normal_btn_pos[1], 50, 50), 1)
            hard_btn_hb = pg.draw.rect(screen, DARK_GRAY, (hard_btn_pos[0], hard_btn_pos[1], 50, 50), 1)
            impossible_btn_hb = pg.draw.rect(screen, DARK_GRAY, (impossible_btn_pos[0], impossible_btn_pos[1], 50, 50),
                                             1)

        else:
            if list_of_ball == []:
                timer_active = False
                end_game = True
                if len(ach_list) == 10 and not list_of_achievements[2] and dif_color_now != BTN_GREEN:
                    achievement_now = pg.image.load('./texture/achievements/catch10.png')
                    ach = True
                    list_of_achievements[2] = True
                if sec <= 60 and dif_color_now == BTN_PERPLE and not list_of_achievements[3]:
                    achievement_now = pg.image.load('./texture/achievements/fast.png')
                    ach = True
                    list_of_achievements[3] = True
                game_over(screen, 'ball', number_list, time)
                restart_btn_hb = pg.draw.rect(screen, DARK_GRAY, (restart_btn_pos[0], restart_btn_pos[1], 140, 100), 1)

            if minutes == 15:
                end_game = True
                game_over(screen, 'time', number_list, None)
                restart_btn_hb = pg.draw.rect(screen, DARK_GRAY, (restart_btn_pos[0], restart_btn_pos[1], 140, 100), 1)

            screen.blit(time_txt, time_txt_pos)
            if timer_active:
                if mil == FPS:
                    sec += 1
                    if sec == 60:
                        sec = 0
                        minutes += 1
                        if minutes == 15:
                            timer_active = False

                    mil = -1
                mil += 1
                if minutes == 0:
                    time = str(sec)
                    timer(time, screen, number_list)

                else:
                    if sec < 10:
                        time = str(minutes) + '0' + str(sec)
                        timer(time, screen, number_list)
                    else:
                        time = str(minutes) + str(sec)
                        timer(time, screen, number_list)
                for ball in balls:
                    ball.draw(i, screen, event)
                    i += 1
                i = 1

        fps_now = str(clock.get_fps()).split('.')
        myfont = pg.font.SysFont('Digital-7 Mono', 50)
        if clock.get_fps() > 45:
            textsurface = myfont.render(str(fps_now[0]), False, GREEN)
        elif 25 < clock.get_fps() < 45:
            textsurface = myfont.render(str(fps_now[0]), False, YELLOW)
        else:
            textsurface = myfont.render(str(fps_now[0]), False, RED)
        screen.blit(textsurface, (0, 0))

        if ach:
            achievement(achievement_now, screen)

        if nomber_of_cursor != 0:
            pg.mouse.set_visible(0)
            if pg.mouse.get_focused():
                cursor(screen, nomber_of_cursor)
        else:
            pg.mouse.set_visible(1)

        clock.tick(FPS)
        space.step(1 / FPS)
        pg.display.flip()
    pg.quit()

# Osu(0, 90, 0)
