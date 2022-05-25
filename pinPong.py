import pygame as pg
import pymunk as pm

from game_setting import *


class Player_red(pg.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(*group)

        self.image = pg.image.load('./texture/pingpong/player_red.png')
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 50, HEIGHT // 2 + self.rect[1] // 2

    def update(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            if self.rect.y > 155:
                self.rect.y -= 1
        if keys[pg.K_s]:
            if self.rect.y < 445:
                self.rect.y += 1


class Player_blue(pg.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(*group)

        self.image = pg.image.load('./texture/pingpong/player_blue.png')
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 950, HEIGHT // 2 + self.rect[1] // 2

    def update(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_UP]:
            if self.rect.y > 155:
                self.rect.y -= 1
        if keys[pg.K_DOWN]:
            if self.rect.y < 445:
                self.rect.y += 1



class Ball:
    def __init__(self, space):
        self.body = pm.Body()
        self.body.position = self.x, self.y = 500, 350
        # self.rect = pg.Rect(self.x, self.y, 2 * ball_radius, 2 * ball_radius)
        # self.rect.x = self.x
        # self.rect.y = self.y
        print(ball_speed)
        self.body.velocity = 2
        self.shape = pm.Circle(self.body, ball_radius)

        self.shape.density = 1
        self.shape.elasticity = 1
        space.add(self.body, self.shape)


def add_wall(p1, p2, space):
    body = pm.Body(body_type=pm.Body.STATIC)
    shape = pm.Segment(body, p1, p2, 20)
    shape.elasticity = 1
    space.add(body)
    space.add(shape)

def wall_create(space):
    add_wall((0, 150),
             (1000, 150), space)
    add_wall((0, 550),
             (1000, 550), space)

def draw_screen(screen):
    pg.draw.line(screen, GREEN, (0, 150), (1000, 150), 5)
    pg.draw.line(screen, GREEN, (0, 550), (1000, 550), 5)


def PingPong():
    pg.init()

    screen = pg.display.set_mode(size)
    space = pm.Space()

    wall_create(space)

    all_sprites = pg.sprite.Group()
    Player_red(all_sprites)
    Player_blue(all_sprites)
    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        all_sprites.update()
        screen.fill(BLACK)
        draw_screen(screen)
        all_sprites.draw(screen)
        pg.display.flip()
    pg.quit()


PingPong()
