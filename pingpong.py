import sys
import random

import pygame as pg
import pymunk as pm

from game_setting import *

space = pm.Space()
ach = False


def print_text(text, x, y, font_size, color, screen):
    font = pg.font.SysFont("hooge 05_55", font_size, True, False)
    surface = font.render(text, True, color)
    screen.blit(surface, (x, y))


class Ball():
    def __init__(self, screen, space):
        self.body = pm.Body()
        self.reset()

        self.shape = pm.Circle(self.body, 8)
        self.shape.density = 1
        self.shape.elasticity = 1

        space.add(self.body, self.shape)
        self.shape.collision_type = 1

        self.screen = screen
        self.scored_red = 0
        self.scored_blue = 0
        self.color = WHITE

    def draw(self):
        x, y = self.body.position
        pg.draw.circle(self.screen, self.color, (x, y), 8)
        if self.body.position.x <= 0:
            self.scored_blue += 1
        if self.body.position.x >= 1000:
            self.scored_red += 1

        if self.body.position.x >= 1000 or self.body.position.x <= 0:
            self.reset()

    def standardize_velocity(self, space=0, arbiter=0, data=0):
        self.body.velocity = self.body.velocity * (self.start_velocity / self.body.velocity.length)
        self.start_velocity += 50
        if self.body.velocity.x > 0:
            self.color = RED
        else:
            self.color = BLUE

    def reset(self):
        self.body.position = mid_x, mid_y
        self.body.velocity = 350 * random.choice([-1, 1]), -150 * random.choice([-1, 1])
        self.start_velocity = 350
        self.color = WHITE
        return False


class Wall():
    def __init__(self, p1, p2, collision_number=None):
        self.body = pm.Body(body_type=pm.Body.STATIC)
        self.shape = pm.Segment(self.body, p1, p2, 10)
        self.shape.elasticity = 1

        space.add(self.shape, self.body)

        if collision_number:
            self.shape.collision_type = collision_number

    def draw(self, screen):
        pg.draw.line(screen, GREEN, self.shape.a, self.shape.b, 5)


class player():
    def __init__(self, x):
        self.body = pm.Body(body_type=pm.Body.KINEMATIC)
        self.body.position = x, mid_y
        self.shape = pm.Segment(self.body, [0, -50], [0, 50], 10)
        self.shape.elasticity = 1

        space.add(self.body, self.shape)
        self.shape.collision_type = 100

        self.score = 0

    def draw(self, screen, color):
        p1 = self.body.local_to_world(self.shape.a)
        p2 = self.body.local_to_world(self.shape.b)
        pg.draw.line(screen, color, p1, p2, 10)

    def update_rad(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_w] and self.body.position.y > 210:
            self.body.velocity = 0, -600
        elif keys[pg.K_s] and self.body.position.y < 490:
            self.body.velocity = 0, 600
        else:
            self.body.velocity = 0, 0

    def update_blue(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_UP] and self.body.position.y > 210:
            self.body.velocity = 0, -600
        elif keys[pg.K_DOWN] and self.body.position.y < 490:
            self.body.velocity = 0, 600
        else:
            self.body.velocity = 0, 0


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


def pingpong(vol, FPS, nomber_of_cursor):
    global ach
    pg.init()

    screen = pg.display.set_mode(size)

    clock = pg.time.Clock()

    button_clicked_sd = pg.mixer.Sound('./sounds/general/sounds_click.ogg')
    button_clicked_sd.set_volume(vol)

    running = True
    game_play = False
    red_win, blue_win = False, False
    achievement_now = None

    ball = Ball(screen, space)
    wall_left = Wall([left, up], [left, down], 102)
    wall_right = Wall([right, up], [right, down], 101)
    wall_up = Wall([left, up], [right, up], 2)
    wall_down = Wall([left, down], [right, down], 2)

    player1 = player(30)
    player2 = player(970)

    collide_with_player = space.add_collision_handler(1, 100)
    collide_with_player.post_solve = ball.standardize_velocity

    exit_btn = pg.draw.rect(screen, BLUE, (0, 650, 60, 50), 1)

    x, y = mid_x - 80, 600
    x2, y2 = 0, 0

    moving = False

    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.MOUSEBUTTONDOWN:
                mouse_pos = pg.mouse.get_pos()
                if start_btn.collidepoint(mouse_pos) and not game_play:
                    button_clicked_sd.play()
                    game_play = True
                    red_win, blue_win = False, False
                    ball.scored_blue, ball.scored_red = 0, 0
                if exit_btn.collidepoint(mouse_pos):
                    button_clicked_sd.play()
                    return
                if x < event.pos[0] < x + 100 and y < event.pos[1] < y + 30:
                    moving = True
            if event.type == pg.MOUSEMOTION:
                if moving:
                    x2, y2 = event.rel
                    x, y = x + x2, y + y2
                    if x <= 0 or x >= WIDTH or y <= 0 or y >= WIDTH:
                        x, y = mid_x - 80, 600
                        moving = False
                    if not list_of_achievements[8]:
                        achievement_now = pg.image.load('./texture/achievements/start.png')
                        ach = True
                        list_of_achievements[8] = True
            if event.type == pg.MOUSEBUTTONUP and event.button == 1:
                moving = False

        screen.fill(BLACK)

        wall_left.draw(screen)
        wall_right.draw(screen)
        wall_up.draw(screen)
        wall_down.draw(screen)

        player1.draw(screen, RED)
        player2.draw(screen, BLUE)

        if game_play:
            player.update_rad(player1)
            player.update_blue(player2)

            start_color = GRAY
            ball.draw()

            if ball.scored_red == 5 or ball.scored_blue == 5:
                game_play = False
                if ball.scored_red == 5:
                    if ball.scored_blue == 4 and not list_of_achievements[9]:
                        achievement_now = pg.image.load('./texture/achievements/lose.png')
                        ach = True
                        list_of_achievements[9] = True
                    red_win = True
                elif ball.scored_blue == 5:
                    if ball.scored_red == 4 and not list_of_achievements[9]:
                        achievement_now = pg.image.load('./texture/achievements/lose.png')
                        ach = True
                        list_of_achievements[9] = True
                    blue_win = True


        else:
            ball.body.position = mid_x, mid_y
            start_color = WHITE

        if red_win:
            print_text('winner', 350, 300, 70, RED, screen)
        elif blue_win:
            print_text('winner', 350, 300, 70, BLUE, screen)
        screen.blit(ping_pong_logo, ping_pong_logo_pos)

        print_text(f'Score = {ball.scored_red}', left * -2, 600, 20, RED, screen)
        print_text(f'Score = {ball.scored_blue}', right - 300, 600, 20, BLUE, screen)

        start_btn = pg.draw.rect(screen, BLACK, (x, y, 140, 30), 1)
        print_text('START', x, y, 40, start_color, screen)

        print_text('EX', 10, 660, 40, WHITE, screen)

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

        pg.display.flip()

        clock.tick(FPS)
        space.step(1 / FPS)
    pg.quit()


# pingpong(0, 60, 0)
