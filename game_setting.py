import pygame as pg
import math

# COLOR
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
DARK_RED = (132, 0, 0)
LOADING_RED = (160, 48, 48)
GREEN = (0, 255, 0)
BLUE = (81, 91, 255)
BG_BLUE = (107, 134, 255)
YELLOW = (255, 255, 0)
GRAY = (174, 190, 189)
MILK_COLOR = (245, 245, 220)
VIOLET = (138, 0, 255)
DARK_GRAY = (30, 30, 30)

BTN_GREEN = (0, 255, 47)
BTN_YELLOW = (255, 246, 0)
BTN_RED = (255, 0, 0)
BTN_PERPLE = (255, 0, 255)

# osu_start = False
# game_active = True

# size

mid_latter_size = (120, 180)
wall_size = 50

# GAME SETTING
START_FPS = 60
# FPS = START_FPS
size = WIDTH, HEIGHT = 1000, 700
x, y = WIDTH, 0
ach_size = 260

button_speed = 20
button_speed_exe = 50
thick = 3
game_name = 'BBZ'
balls_speed = 5

# list

# balls_speed_list = [-3, -2, -1, 1, 2, 3]

# position
# cq_pos_x = WIDTH // 2
# cq_pos_y = 0 - mid_latter_size[1]


# logo_pos = (380, 65)

osu_logo_pos = (200, 0)
# start_logo_pos = (no_border_size_on_x + 50, no_border_size_on_y + 50)

# exit_btn_pos = (0, 650)
setting_button_pos = (950, 650)
back_button_pos = (10, 640)
circle_pos_x = 250
# circle_pos_y = HEIGHT - no_border_size_on_y // 2
circle_radius = 20
catch_ball_pos_x = 210
catch_ball_pos_y = 605

# start_stone_btn_pos = (150, -50)
# stone_x, stone_y = 150, -50


# SETTING MENU POSITION | SETTING | IMAGE
# POSITION
setting_logo_pos = (275, 50)
check_bg_pos = (445, 300)
vol_text_pos = (360, 210)
fps_text_pos = (450, 380)
ball_wall_pos = (300, 530)
save_btn_pos = (620, 575)
delete_update_pos = (850, 650)

plus_minus_pos_x = 570
plus_minus_pos_x_2 = 390
plus_minus_pos_y = 302
plus_minus_pos_y_2 = 462
back_btn_pos = (0, 630)

# IMAGE
setting_logo = pg.image.load('./texture/setting/logo.png')
check_bg = pg.image.load('./texture/setting/check_bg.png')
vol_text = pg.image.load('./texture/setting/vol.png')
fps_text = pg.image.load('./texture/setting/fps.png')
ball_wall = pg.image.load('./texture/setting/ball_wall1.png')
ball_wall_hb = pg.image.load('./texture/setting/ball_wall_hb.png')

btn_plus = pg.image.load('./texture/setting/+.png')
btn_minus = pg.image.load('./texture/setting/-.png')
back_btn = pg.image.load('./texture/setting/back.png')
save_btn = pg.image.load('./texture/setting/save_btn.png')
delete_update = pg.image.load('./texture/setting/delete_update.png')

# cursor
cr_no = pg.transform.scale(pg.image.load('./texture/cursors/cr_no.png'), (20, 40))
cr_snow = pg.transform.scale(pg.image.load('./texture/cursors/cr_snow.png'), (20, 40))
cr_tree = pg.transform.scale(pg.image.load('./texture/cursors/cr_tree.png'), (20, 40))
cr_snowman = pg.transform.scale(pg.image.load('./texture/cursors/cr_snowman.png'), (20, 40))
cr_line = pg.transform.scale(pg.image.load('./texture/cursors/cr_line.png'), (20, 40))
cr_vector = pg.transform.scale(pg.image.load('./texture/cursors/cr_vector.png'), (20, 40))
cr_cursor = pg.transform.scale(pg.image.load('./texture/cursors/cr_cursor.png'), (20, 40))

# -

# MENU POSITION | SETTING | IMAGE
# POSITION
r_steam_pos = (420, 180)
bbz_logo_pos = (360, 40)
shovel_pos = (870, 50)

tank_button_pos = (550, 263)
osu_button_pos = (350, 263)
stone_button_pos = (150, 263)
snake_pos = (750, 250)

# SETTING
full_snow_speed = 0.001

# IMAGE
r_steam = pg.image.load('./texture/menu/steam.png')
bbz_logo = pg.image.load('./texture/menu/logo.png')
full_snow = pg.image.load('./texture/menu/full_snow.png')
snowman = pg.image.load('./texture/menu/snowman.png')
shovel = pg.image.load('./texture/menu/shovel.png')

stone = pg.image.load('./texture/menu/stone_btn_snow.png')
osu = pg.image.load('./texture/menu/osu_btn_snow.png')
tank = pg.image.load('./texture/menu/tank_btn_snow.png')
snake = pg.image.load('./texture/menu/snake_btn_snow.png')
exit_button = pg.image.load('./texture/menu/exit_btn.png')
setting = pg.image.load('./texture/menu/setting_btn.png')

# -

# OSU POSITION | SETTING | IMAGE
# POSITION
no_border_size_on_x = 200
no_border_size_on_y = 150
osu_field_length = WIDTH - no_border_size_on_x * 2
osu_field_height = HEIGHT - no_border_size_on_y * 2
first_timer_number = 895, 260
dif_logo_pos = (270, 170)
time_txt_pos = (800, 200)
logo_pos = (200, 10)
time_out_pos = (200, 200)
win_logo_pos = (200, 200)
no_time_pos = (820, 260)

start_btn_pos = (445, 450)
ez_btn_pos = (280, 350)
normal_btn_pos = (410, 350)
hard_btn_pos = (540, 350)
impossible_btn_pos = (670, 350)
exit_btn_pos = (0, 630)
restart_btn_pos = (430, 400)

# SETTING
ball_radius = 20
ball_speed = 0

# IMAGE
logo = pg.image.load('./texture/osu/3d_text/logo.png')
dif_logo = pg.image.load('./texture/osu/3d_text/dif_logo.png')
time_txt = pg.image.load('./texture/osu/3d_text/time.png')
colon = pg.image.load('./texture/osu/3d_text/colon.png')
breake = pg.image.load('./texture/osu/ball_breake.png')
time_out = pg.image.load('./texture/osu/3d_text/time_out.png')
win_logo = pg.image.load('./texture/osu/3d_text/win.png')
no_time = pg.image.load('./texture/osu/3d_text/no_time.png')

start_btn = pg.image.load('./texture/osu/button/start_btn.png')
start_btn_green = pg.image.load('./texture/osu/button/start_btn_green.png')
start_btn_yellow = pg.image.load('./texture/osu/button/start_btn_yellow.png')
start_btn_red = pg.image.load('./texture/osu/button/start_btn_red.png')
start_btn_perple = pg.image.load('./texture/osu/button/start_btn_perple.png')

ez_btn = pg.image.load('./texture/osu/button/ez_btn.png')
normal_btn = pg.image.load('./texture/osu/button/normal_btn.png')
hard_btn = pg.image.load('./texture/osu/button/hard_btn.png')
impossible_btn = pg.image.load('./texture/osu/button/imposible_btn.png')
exit_btn = pg.image.load('./texture/osu/button/exit_btn.png')
restart_btn = pg.image.load('./texture/osu/button/restart_btn.png')

# -

# TANK POSITION | SETTING | IMAGE
# POSITION
WIDTH = 1000
HEIGHT = 700
HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2

red_tank_pos = (40, HEIGHT - 100)
blue_tank_pos = (WIDTH - 60, 100)
tank_speed = 2

allowed_x = 150
back_allowed_x = WIDTH - allowed_x

allowed_y = 100
back_allowed_y = HEIGHT - allowed_y

wall_size = 50

# IMAGE
bullet_snowball = pg.image.load('./texture/tank_texture/bullet_snowball.png')
bullet_bar_blue = pg.image.load('./texture/tank_texture/bullet_bar_blue.png')
bullet_bar_red = pg.image.load('./texture/tank_texture/bullet_bar.png')
# ezz = 100
# norm = 250
# hard = 600
# impos = 750
# PS больше 750 улетает за карту <3
list_of_cursor = [cr_no, cr_snow, cr_tree, cr_snowman, cr_line, cr_vector]

# BRICK POSITION | SETTING | IMAGE

# SETTING
WIDTH_B = 1200
HEIGHT_B = 800
HALF_WIDTH = WIDTH_B // 2
HALF_HEIGHT = HEIGHT_B // 2
# FPS = 60
SIDE = 100

FOV = math.pi / 3
HALF_FOV = FOV / 2
NUM_RAYS = 240
MAX_DEPTH = 1000
DELTA_ANGLE = FOV / NUM_RAYS
DIST = NUM_RAYS / (2 * math.tan(HALF_FOV))
PROJ_COEFF = 3 * DIST * SIDE
SCALE = WIDTH_B // NUM_RAYS

# POSITION
player_pos = (400, 348)
player_angle = 0
player_speed = 2
brick_back_btn_pos = (0, 0)

# IMAGE

brick_back_btn = pg.image.load('./texture/brick/back_btn.png')

# PING-PONG POSITION | SETTING | IMAGE

# POSITION
left = -50
right = 1050
up = 150
down = 550
mid_x = 500
mid_y = 350
ping_pong_logo_pos = (300, 50)
# IMAGE
ping_pong_logo = pg.image.load('./texture/pingpong/logo.png')

list_of_achievements = [False, False, False, False, False, False, False, False, False, False]

