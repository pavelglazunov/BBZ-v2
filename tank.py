import os
import sys
import math
import random

import pygame as pg

from game_setting import *

wall_group = pg.sprite.Group()
all_sprites = pg.sprite.Group()
bullet_group = pg.sprite.Group()

list_of_x = []
list_of_y = []


class Wall(pg.sprite.Sprite):
    image = pg.image.load('./texture/tank_texture/wall.png')

    def __init__(self, x_pos, y_pos, screen):
        super().__init__(wall_group)
        self.image = Wall.image
        self.rect = self.image.get_rect()
        self.rect.x = x_pos
        self.rect.y = y_pos
        screen.blit(self.image, (self.rect.x, self.rect.y))
        self.mask = pg.mask.from_surface(self.image)


class Bullet(pg.sprite.Sprite):
    pass
    # image = pg.image.load('./texture/tank_texture/bullet_snowball.png')
    #
    # def __init__(self, x_pos, y_pos, screen, direction, *group):
    #     super().__init__(bullet_group)
    #     self.image = pg.Surface((2 * 10, 2 * 10),
    #                                 pg.SRCALPHA, 32)
    #     self.rect = self.image.get_rect()
    #     self.direction_x = direction[0]
    #     self.direction_y = direction[1]
    #     self.rect.x, self.rect.y = x_pos + 20, y_pos + 20
    #     pg.draw.rect(screen, RED, (self.rect.x, self.rect.y, 20, 20), 1)
    #     # print(direction)
    #
    #     print(self.direction_x, self.direction_y)
    #
    #
    # def update(self, screen):
    #
    #     if pg.sprite.spritecollideany(self, wall_group):
    #         self.kill()
    #     else:
    #         # self.rect = self.rect.move(x, y)
    #         self.rect.x += self.direction_x * 2
    #         self.rect.y += self.direction_y * 2
    # pg.draw.circle(screen, RED, (self.rect.x, self.rect.y), 10, 0)

    # screen.blit(self.image, (self.rect.x, self.rect.y))
    # self.rect = self.rect.move(self.rect.x, self.rect.y)


#

# def players(screen):
#     blue_tank = pg.image.load('./texture/tank_texture/blue_tank.png').convert_alpha()
#     red_tank = pg.image.load('./texture/tank_texture/red_tank.png').convert_alpha()
#
#     blue_tank_x = (WIDTH - wall_size * 4)
#     blue_tank_y = wall_size
#
#     red_tank_x = wall_size * 3
#     red_tank_y = HEIGHT - wall_size * 2
#     print(blue_tank_x, blue_tank_y)
#
#
#     screen.blit(blue_tank, (blue_tank_x, blue_tank_y))
#     screen.blit(red_tank, (red_tank_x, red_tank_y))
# pg.draw.rect(screen, RED, (100, 550, 30, 30), 0)
# pg.draw.rect(screen, GREEN, (850, 100, 30, 30), 0)

# screen.blit(pg.image.load('./texture/tank_texture/blue_tank.png').convert_alpha(), (0, 0))


class Blue(pg.sprite.Sprite):
    image = pg.image.load('./texture/tank_texture/blue_tank.png')
    n = 1

    def __init__(self, *group):
        super().__init__(*group)

        self.image = Blue.image
        self.rect = self.image.get_rect()
        # print(self.rect)
        # print(self.rect)
        # print(self.image.get_rect().x)
        self.rect.x, self.rect.y = pg.math.Vector2(800, 50)
        self.direction_blue = pg.math.Vector2(3, 0)
        self.angel_blue = 2

        self.mask = pg.mask.from_surface(self.image)

        self.rotated_blue = False
        self.shot = True

    def update(self, screen):
        keys = pg.key.get_pressed()
        if keys[pg.K_KP5]:

            if self.shot:
                # Bullet(self.rect.x, self.rect.y, screen, self.direction_red, bullet_group)
                self.shot = False
            if not pg.sprite.spritecollideany(self, wall_group):
                self.rotated_blue = False
                # self.rect.move(self.direction_red)
                self.rect.x += self.direction_blue.x
                self.rect.y += self.direction_blue.y
                # print(self.direction_red.x, self.direction_red.y)
            else:
                self.rect.x += 1
                if pg.sprite.spritecollideany(self, wall_group):
                    self.rect.x -= 2
                else:
                    self.rect.x -= 1
                self.rect.y += 1
                if pg.sprite.spritecollideany(self, wall_group):
                    self.rect.y -= 4
                else:
                    self.rect.y -= 1
                self.rect.x -= 1
                if pg.sprite.spritecollideany(self, wall_group):
                    self.rect.x += 5
                else:
                    self.rect.x += 1
                self.rect.y -= 1
                if pg.sprite.spritecollideany(self, wall_group):
                    self.rect.y += 5
                else:
                    self.rect.y += 1

                self.rotated_blue = True
        else:
            self.shot = True
            #
            if not self.rotated_blue:
                self.angel_blue = -self.angel_blue
                self.rotated_blue = True
                self.rect.x -= self.direction_blue.x
                self.rect.y -= self.direction_blue.y

            # else:
            #     self.rect.x -= self.direction_red.x * 0.0000001
            #     self.rect.y -= self.direction_red.y * 0.0000001
            self.direction_blue.rotate_ip(self.angel_blue)

        angle_blue = self.direction_blue.angle_to((1, 0))
        rotated_blue_tank = pg.transform.rotate(self.image, angle_blue)
        screen.blit(rotated_blue_tank,
                    rotated_blue_tank.get_rect(center=(round(self.rect.x + 22), round(self.rect.y + 22))))


class Red(pg.sprite.Sprite):
    image = pg.image.load('./texture/tank_texture/red_tank.png')
    n = 1

    def __init__(self, *group):
        super().__init__(*group)

        self.image = Red.image
        self.rect = self.image.get_rect()
        # print(self.rect)
        # print(self.rect)
        # print(self.image.get_rect().x)
        self.rect.x, self.rect.y = pg.math.Vector2(150, 600)
        self.direction_red = pg.math.Vector2(3, 0)
        self.angel_red = 2

        self.mask = pg.mask.from_surface(self.image)

        self.rotated_red = False
        self.shot = True

    def update(self, screen):
        keys = pg.key.get_pressed()
        if keys[pg.K_SPACE]:

            if self.shot:
                # Bullet(self.rect.x, self.rect.y, screen, self.direction_red, bullet_group)
                self.shot = False
            if not pg.sprite.spritecollideany(self, wall_group):
                self.rotated_blue = False
                # self.rect.move(self.direction_red)
                self.rect.x += self.direction_red.x
                self.rect.y += self.direction_red.y
                # print(self.direction_red.x, self.direction_red.y)
            else:
                self.rect.x += 1
                if pg.sprite.spritecollideany(self, wall_group):
                    self.rect.x -= 2
                else:
                    self.rect.x -= 1
                self.rect.y += 1
                if pg.sprite.spritecollideany(self, wall_group):
                    self.rect.y -= 4
                else:
                    self.rect.y -= 1
                self.rect.x -= 1
                if pg.sprite.spritecollideany(self, wall_group):
                    self.rect.x += 5
                else:
                    self.rect.x += 1
                self.rect.y -= 1
                if pg.sprite.spritecollideany(self, wall_group):
                    self.rect.y += 5
                else:
                    self.rect.y += 1

                self.rotated_red = True
        else:
            self.shot = True
            #
            if not self.rotated_red:
                self.angel_red = -self.angel_red
                self.rotated_red = True
                self.rect.x -= self.direction_red.x
                self.rect.y -= self.direction_red.y

            # else:
            #     self.rect.x -= self.direction_red.x * 0.0000001
            #     self.rect.y -= self.direction_red.y * 0.0000001
            self.direction_red.rotate_ip(self.angel_red)

        angle_red = self.direction_red.angle_to((1, 0))
        rotated_red_tank = pg.transform.rotate(self.image, angle_red)
        screen.blit(rotated_red_tank,
                    rotated_red_tank.get_rect(center=(round(self.rect.x + 22), round(self.rect.y + 22))))


def wall_create(screen):
    x = 100
    y = 50
    nx = (WIDTH - wall_size * 4) // 50
    ny = HEIGHT // 50
    n_mid = (nx - 2) * (ny - 2) * 10 // 100  # 20 процентов от кол-ва свободных клеток
    allowed_x = wall_size * 4
    allowed_y = wall_size * 2
    back_allowed_x = WIDTH - allowed_x
    back_allowed_y = HEIGHT - allowed_y

    if list_of_x == [] and list_of_y == []:
        # print(111)
        for n in range(n_mid):
            # aaa = pg.draw.rect(screen, RED, (self.rect.x - 25, self.rect.y - 25, 50, 50), 1)
            x_pos = random.randrange(allowed_x, back_allowed_x, 50)
            # if x_pos ==
            y_pos = random.randrange(allowed_y, back_allowed_y, 50)

            wall = Wall(x_pos, y_pos, screen)
            list_of_x.append(x_pos)
            list_of_y.append(y_pos)
        # print(list_of_x)
        # print(list_of_y)
    else:
        x = 100
        for n in range(n_mid):
            x_pos = list_of_x[n]
            y_pos = list_of_y[n]
            # aaa = pg.draw.rect(screen, RED, (x_pos, y_pos, 51, 50), 1)

            wall = Wall(x_pos, y_pos, screen)

        for i in range(nx):
            wall = Wall(x, 0, screen)
            wall = Wall(x, 650, screen)
            x += wall_size
        x = 100
        y = 50
        for i in range(ny):
            wall = Wall(x, y, screen)
            wall = Wall(850, y, screen)
            y += wall_size

            # for i in range(nx):
            #     Wall(x, 0)
            #     Wall(x, 650)
            #     x += wall_size
            # x = 100
            # for j in range(ny):
            #     screen.blit(self.image, (x, y))
            #     screen.blit(self.image, (WIDTH - x * 1.5, y))
            #     y += wall_size

            # if x_pos == 850 and y_pos == 100:
            #     x_pos = random.randrange(100, 900, 50)
            #     y_pos = random.randrange(100, 600, 50)
            #     print(123)
            # if x_pos == 100 and y_pos == 550:
            #     print(122)
            #     x_pos = random.randrange(100, 900, 50)
            #     y_pos = random.randrange(100, 600, 50)


def tanks(vol, FPS, nomber_of_cursor):
    game_name = 'BBZ'

    pg.init()
    pg.display.set_caption(game_name)

    screen = pg.display.set_mode(size, pg.RESIZABLE)

    running = True
    now_draw = True

    # FPS = 60

    clock = pg.time.Clock()
    screen.fill(GRAY)
    # draw_wall(screen)
    # mid_wall_draw(screen)
    wall_create(screen)
    # players(screen)
    # Wall(screen)
    # Blue(all_sprites)
    Red(all_sprites)
    Blue(all_sprites)

    back_button = pg.image.load('./texture/tank_texture/house_btn.png')
    back_button_hitbox = pg.draw.rect(screen, GRAY, (back_button_pos[0], back_button_pos[1], 50, 50), 1)

    # all_sprites.update(screen)
    # Player(all_sprites)

    n = 1
    x = 0
    while running:

        # if list_of_x == [] and list_of_y == []:
        #     print(111)
        #     for n in range(n_mid):
        #         aaa = pg.draw.rect(screen, RED, (self.rect.x - 25, self.rect.y - 25, 50, 50), 1)
        #         x_pos = random.randrange(allowed_x, back_allowed_x, 50)
        #         y_pos = random.randrange(allowed_y, back_allowed_y, 50)
        #         screen.blit(self.image, (x_pos, y_pos))
        #         list_of_x.append(x_pos)
        #         list_of_y.append(y_pos)
        #     print(list_of_x)
        #     print(list_of_y)
        # else:
        #     for n in range(n_mid):
        #         x_pos = list_of_x[n]
        #         y_pos = list_of_y[n]
        #         # aaa = pg.draw.rect(screen, RED, (x_pos, y_pos, 51, 50), 1)
        #
        #         screen.blit(self.image, (x_pos, y_pos))
        #
        #         # if x_pos == 850 and y_pos == 100:
        #         #     x_pos = random.randrange(100, 900, 50)
        #         #     y_pos = random.randrange(100, 600, 50)
        #         #     print(123)
        #         # if x_pos == 100 and y_pos == 550:
        #         #     print(122)
        #         #     x_pos = random.randrange(100, 900, 50)
        #         #     y_pos = random.randrange(100, 600, 50)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.MOUSEBUTTONDOWN:
                mouse_pos = pg.mouse.get_pos()
                if back_button_hitbox.collidepoint(mouse_pos):
                    return
            # if event.type == pg.KEYDOWN:
            #     if pg.K_SPACE:
            #         print(1552)
        # keys = pg.key.get_pressed()
        # if [pg.K_SPACE]:
        #     pass

        # elif event.type == pg.KEYDOWN:
        #     if event.key == pg.K_UP:
        #         n += 1
        #         Red().update(n)
        #         all_sprites.draw(screen)

        # print(123)

        # try:
        #     Player.rect.collidepoint(Wall.rect)
        # except AttributeError:
        #     print(123333)
        #     all_sprites.update('stop')
        # all_sprites.update('up')
        # elif event.key == pg.K_RIGHT:
        #     all_sprites.update('right')
        # all_sprites.draw(screen)
        # all_sprites.update()

        bullet_group.update(screen)
        screen.fill(GRAY)
        wall_create(screen)
        screen.blit(bullet_bar_red, bullet_bar_red_pos)
        screen.blit(bullet_bar_blue, bullet_bar_blue_pos)

        # Blue()

        # for n in range(33):
        #     x_pos = list_of_x[n]
        #     y_pos = list_of_y[n]
        #     aaa = pg.draw.rect(screen, RED, (x_pos - 1, y_pos - 1, 52, 52), 1)

        # screen.blit(self.image, (x_pos, y_pos))
        x += 1
        # all_sprites.update(x, screen)

        # all_sprites.draw(screen)
        # Red().update(screen)
        screen.blit(back_button, (back_button_pos[0], back_button_pos[1]))
        # Player(all_sprites)
        # wall_group.draw(screen)
        # bullet_group.update(screen)

        bullet_group.draw(screen)
        all_sprites.update(screen)

        fps_now = str(clock.get_fps()).split('.')
        myfont = pg.font.SysFont('Digital-7 Mono', 50)
        if clock.get_fps() > 45:
            textsurface = myfont.render(str(fps_now[0]), False, GREEN)
        elif 25 < clock.get_fps() < 45:
            textsurface = myfont.render(str(fps_now[0]), False, YELLOW)
        else:
            textsurface = myfont.render(str(fps_now[0]), False, RED)
        screen.blit(textsurface, (0, 0))

        # all_sprites.update()
        # draw_wall(screen)
        # mid_wall_draw(screen)
        # players(screen)
        clock.tick(FPS)
        pg.display.flip()
    pg.quit()
# tanks(0, 60, 0)
