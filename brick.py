import pygame
import math
import sys

from game_setting import *

text_map = [
    'aaaaaaaaaaaa',
    'a          a',
    'a          a',
    'a    □□    a',
    'a          a',
    'a          a',
    'a          a',
    'aaaaaaaaaaaa'
]

air_map = set()
world_map = set()

ach = False

for y in range(len(text_map)):
    for x in range(len(text_map[y])):
        if text_map[y][x] == '□':
            world_map.add((x * SIDE, y * SIDE))
for y in range(len(text_map)):
    for x in range(len(text_map[y])):
        if text_map[y][x] == 'a':
            air_map.add((x * SIDE, y * SIDE))


class PLayer:
    def __init__(self):
        self.x, self.y = player_pos
        self.angle = player_angle

    @property
    def pos(self):
        return (self.x, self.y)

    def movement(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.x += player_speed * cos_a
            self.y += player_speed * sin_a
        if keys[pygame.K_s]:
            self.x -= player_speed * cos_a
            self.y -= player_speed * sin_a
        if keys[pygame.K_a]:
            self.x += player_speed * sin_a
            self.y -= player_speed * cos_a
        if keys[pygame.K_d]:
            self.x -= player_speed * sin_a
            self.y += player_speed * cos_a

        if keys[pygame.K_r]:
            self.angle -= 0.02
        if keys[pygame.K_t]:
            self.angle += 0.02


def ray_casting(screen, player_pos, player_angle):
    cur_angle = player_angle - HALF_FOV
    x0, y0 = player_pos
    for ray in range(NUM_RAYS):
        sin_a = math.sin(cur_angle)
        cos_a = math.cos(cur_angle)
        for depth in range(MAX_DEPTH):
            x = x0 + depth * cos_a
            y = y0 + depth * sin_a
            if (x // SIDE * SIDE, y // SIDE * SIDE) in world_map:
                depth *= math.cos(cur_angle - player_angle)
                proj_height = PROJ_COEFF / depth
                c = 255 / (1 + depth * depth * 0.0001)
                color = (c, c // 4, c // 4)
                pygame.draw.rect(screen, color, (ray * SCALE, HALF_HEIGHT - proj_height // 2, SCALE, proj_height))
                break
            if (x // SIDE * SIDE, y // SIDE * SIDE) in air_map:
                depth *= math.cos(cur_angle - player_angle)
                proj_height = PROJ_COEFF / depth
                color = BLUE
                pygame.draw.rect(screen, color, (ray * SCALE, HALF_HEIGHT - proj_height // 2, SCALE, proj_height))
                break
        cur_angle += DELTA_ANGLE


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


def brick(vol, FPS, nomber_of_cursor):
    global ach
    pygame.init()
    screen = pygame.display.set_mode((WIDTH_B, HEIGHT_B))
    clock = pygame.time.Clock()
    player = PLayer()

    button_clicked_sd = pg.mixer.Sound('./sounds/general/sounds_click.ogg')
    button_clicked_sd.set_volume(vol)

    back_btn_hb = pg.draw.rect(screen, GRAY, (5, 5, 60, 60), 1)
    running = True

    achievement_now = None

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pg.MOUSEBUTTONDOWN:
                mouse_pos = pg.mouse.get_pos()
                if back_btn_hb.collidepoint(mouse_pos):
                    button_clicked_sd.play()
                    player_pos = (HALF_WIDTH - 200, HALF_HEIGHT)
                    player_angle = 0
                    player_speed = 2
                    return
        player.movement()
        screen.fill(BLACK)
        pygame.draw.rect(screen, BLUE, (0, 0, WIDTH_B, HALF_HEIGHT))
        pygame.draw.rect(screen, WHITE, (0, HALF_HEIGHT, WIDTH_B, HALF_HEIGHT))
        ray_casting(screen, player.pos, player.angle)
        fps_now = str(clock.get_fps()).split('.')
        myfont = pygame.font.SysFont('Digital-7 Mono', 50)
        if clock.get_fps() > 45:
            textsurface = myfont.render(str(fps_now[0]), False, GREEN)
        elif 25 < clock.get_fps() < 45:
            textsurface = myfont.render(str(fps_now[0]), False, (255, 255, 0))
        else:
            textsurface = myfont.render(str(fps_now[0]), False, RED)
        screen.blit(textsurface, (1150, 0))

        screen.blit(brick_back_btn, brick_back_btn_pos)

        if ach:
            achievement(achievement_now, screen)

        if nomber_of_cursor != 0:
            pg.mouse.set_visible(0)
            if pg.mouse.get_focused():
                cursor(screen, nomber_of_cursor)
        else:
            pg.mouse.set_visible(1)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

# Brick(0, 60, 0)
