import pygame
from game_setting import *
import math
import random


def print_text(text, x, y, font_input, font_size, color, screen):
    font = pygame.font.SysFont(font_input, font_size, True, False)
    surface = font.render(text, True, color)
    screen.blit(surface, (x, y))


def tank_game(volume, FPS, nomber_of_cursor):
    pygame.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    running = True
    image = pygame.image.load("./texture/tank_texture/negr_tank.png")
    pygame.display.set_icon(image)
    pygame.display.set_caption("СуперМегаПуперТанчики")
    wall_group = pygame.sprite.Group()
    bullet_group = pygame.sprite.Group()
    tank_group = pygame.sprite.Group()

    class Bullet(pygame.sprite.Sprite):
        def __init__(self, tank_pos, tank_angle):
            super().__init__(bullet_group)
            self.image = pygame.image.load('./texture/tank_texture/bullet_snowball.png')
            self.rect = self.image.get_rect()

            self.rect.x, self.rect.y = tank_pos
            self.angle = tank_angle

        def update(self):
            if pygame.sprite.spritecollideany(self, wall_group) or pygame.sprite.spritecollideany(self, tank_group):
                self.kill()
            elif self.rect.y > HEIGHT:
                self.rect.y = self.rect.y % HEIGHT
            elif self.rect.y < 0:
                self.rect.y = self.rect.y + HEIGHT

            elif self.rect.x > WIDTH:
                self.rect.x = self.rect.x % WIDTH
            elif self.rect.x < 0:
                self.rect.x = self.rect.x + WIDTH
            else:
                sin_angle = math.sin(self.angle / -57.3)
                cos_angle = math.cos(self.angle / -57.3)

                self.rect.x += tank_speed * 3 * cos_angle
                self.rect.y += tank_speed * 3 * sin_angle

    class Wall(pygame.sprite.Sprite):
        image = pygame.image.load('./texture/tank_texture/wall.png')

        def __init__(self, x_pos, y_pos):
            super().__init__(wall_group)
            self.image = Wall.image
            self.rect = self.image.get_rect()

            self.rect.x = x_pos
            self.rect.y = y_pos

    class Tank(pygame.sprite.Sprite):
        red = pygame.image.load("./texture/tank_texture/red_tank.png")
        blue = pygame.image.load("./texture/tank_texture/blue_tank.png")

        def __init__(self, tank_pos, key, tank_angle, name_image):
            super().__init__(tank_group)
            self.tank_pos = tank_pos
            if name_image == 'red':
                self.image = Tank.red
            else:
                self.image = Tank.blue

            self.rect = self.image.get_rect()
            self.rect.x, self.rect.y = tank_pos
            self.x1, self.y1 = self.rect.center

            self.angle = tank_angle
            self.factor = -1

            self.key = key

            self.sin_angle = math.sin(self.angle / -57.3)
            self.cos_angle = math.cos(self.angle / -57.3)

            self.image_now = name_image

            self.is_broken = False
            self.first_time = True

        @property
        def is__broken(self):
            return self.is_broken

        def update(self):
            self.sin_angle = math.sin(self.angle / -57.3)
            self.cos_angle = math.cos(self.angle / -57.3)

            keys = pygame.key.get_pressed()

            if self.rect.y > HEIGHT:
                self.y1 = self.y1 % HEIGHT
            elif self.rect.y < 0:
                self.y1 = self.y1 + HEIGHT

            elif self.rect.x > WIDTH:
                self.x1 = self.x1 % WIDTH
            elif self.rect.x < 0:
                self.x1 = self.x1 + WIDTH
            elif pygame.sprite.spritecollideany(self, wall_group):
                self.x1 += -1 * self.cos_angle
                self.y1 += -1 * self.sin_angle

            elif pygame.sprite.spritecollideany(self, bullet_group):

                bullet_group.empty()

                self.image = pygame.transform.rotate(pygame.image.load("./texture/tank_texture/negr_tank.png"), self.angle)
                self.is_broken = True

            elif self.is_broken:
                pass
            elif self.first_time and keys[self.key] and not self.is_broken:
                self.x1 += tank_speed * self.cos_angle
                self.y1 += tank_speed * self.sin_angle
                self.factor *= -1
                Bullet((self.rect.x + 25 + tank_speed * 25 * self.cos_angle,
                        self.rect.y + 25 + tank_speed * 25 * self.sin_angle), self.angle)
                self.first_time = False
            elif keys[self.key] and not self.is_broken:
                self.x1 += tank_speed * self.cos_angle
                self.y1 += tank_speed * self.sin_angle
            elif not self.is_broken:
                self.angle += 2 * self.factor
                if self.angle >= 360 or self.angle <= -360:
                    self.angle = 0
                self.first_time = True
                if self.image_now == 'red':
                    self.image = pygame.transform.rotate(self.red, self.angle)
                if self.image_now == 'blue':
                    self.image = pygame.transform.rotate(self.blue, self.angle)
                self.rect = self.image.get_rect()
            self.rect.center = (self.x1, self.y1)

    def wall_create():
        x = 100
        y = 50

        nx = (WIDTH - wall_size * 4) // 50
        ny = HEIGHT // 50
        n_mid = (nx - 2) * (ny - 2) * 30 // 100  # 20 процентов от кол-ва свободных клеток

        allowed_x = wall_size * 2
        allowed_y = wall_size * 1

        back_allowed_x = WIDTH - allowed_x
        back_allowed_y = HEIGHT - allowed_y

        for n in range(n_mid):
            x_pos = random.randrange(allowed_x, back_allowed_x, 50)
            y_pos = random.randrange(allowed_y, back_allowed_y, 50)
            Wall(x_pos, y_pos)

    def cursor(screen, number):
        mouse_pos = pg.mouse.get_pos()
        screen.blit(list_of_cursor[number], mouse_pos)

    red_tank = Tank(red_tank_pos, pygame.K_SPACE, 0, 'red')
    blue_tank = Tank(blue_tank_pos, pygame.K_KP_5, 0, 'blue')

    restart_img = pygame.transform.scale(pygame.image.load("./texture/tank_texture/return.png"), (400, 100))
    restart_rect = restart_img.get_rect()

    exit_img = pygame.transform.scale(pygame.image.load("./texture/tank_texture/exit.png"), (100, 100))
    exit_rect = exit_img.get_rect()

    print(restart_rect)

    wall_create()
    running1 = True
    while running:
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN and not running1:
                mouse_pos = event.pos
                if 300 < mouse_pos[0] < 500 and 400 < mouse_pos[1] < 500:
                    tank_game()
                if 500 < mouse_pos[0] < 600 and 550 < mouse_pos[1] < 650:
                    return

        if running1:
            bullet_group.update()
            tank_group.update()

            screen.fill(GRAY)

            bullet_group.draw(screen)
            tank_group.draw(screen)
            wall_group.draw(screen)
            if red_tank.is__broken:

                text = "Голубые выйграли"
                tc = BLUE
                print("Голубые выйграли")
                running1 = False
            elif blue_tank.is__broken:
                text = "Красные выйграли"
                tc = RED
                print("Красные выйграли")
                running1 = False
        else:

            wall_group.empty()
            bullet_group.empty()
            wall_group.update()
            screen.fill(GRAY)
            tank_group.update()
            tank_group.draw(screen)
            print_text(text, 25, 250, "Comic Sans MS", 100, tc, screen)

            screen.blit(restart_img, (300, 400))
            screen.blit(exit_img, (500, 550))

        if nomber_of_cursor != 0:
            pg.mouse.set_visible(0)
            if pg.mouse.get_focused():
                cursor(screen, nomber_of_cursor)
        else:
            pg.mouse.set_visible(1)

        clock.tick(60)
        pygame.display.flip()
    pygame.quit()
    wall_group.empty()
    tank_group.empty()
    bullet_group.empty()




# tank()
