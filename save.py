def draw_wall(screen):
    x = 0
    y = 50

    for i in range(20):
        screen.blit(pg.image.load('./texture/tank_texture/wall.png').convert_alpha(), (x, 0))
        screen.blit(pg.image.load('./texture/tank_texture/wall.png').convert_alpha(), (x, 650))
        x += 50
    for j in range(12):
        screen.blit(pg.image.load('./texture/tank_texture/wall.png').convert_alpha(), (0, y))
        screen.blit(pg.image.load('./texture/tank_texture/wall.png').convert_alpha(), (950, y))
        y += 50



def mid_wall_draw(screen):
    list_of_wall_x = []
    list_of_wall_y = []
    for n in range(200):
        x_pos = random.randrange(100, 900, 50)
        y_pos = random.randrange(100, 600, 50)
        # print(x_pos, y_pos)
        if x_pos == 850 and y_pos == 100:
            x_pos = random.randrange(100, 900, 50)
            y_pos = random.randrange(100, 600, 50)
            print(123)
        if x_pos == 100 and y_pos == 550:
            print(122)
            x_pos = random.randrange(100, 900, 50)
            y_pos = random.randrange(100, 600, 50)
            # print(1223)
        if x_pos in list_of_wall_x and y_pos in list_of_wall_y:
            x_pos = random.randrange(100, 900, 50)
            y_pos = random.randrange(100, 600, 50)
        list_of_wall_x.append(x_pos)
        list_of_wall_y.append(y_pos)
        screen.blit(pg.image.load('./texture/tank_texture/wall.png').convert_alpha(), (x_pos, y_pos))





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
        self.rect.x, self.rect.y = 150, 600
        # self.direction_red = pg.math.Vector2(3, 0)
        self.angel_red = 0
        self.rotated = 1

        self.speed = 1

        self.mask = pg.mask.from_surface(self.image)

        self.rotated_red = False
        self.shot = True

    def update(self, screen):
        sin_a = math.sin(self.angel_red)
        cos_a = math.cos(self.angel_red)
        keys = pg.key.get_pressed()
        if keys[pg.K_SPACE]:
            self.rotated_red = False
            # print(self.rotated_red)
            if self.shot:
                # Bullet(self.rect.x, self.rect.y, screen, self.direction_red, bullet_group)
                self.shot = False
            if not pg.sprite.spritecollideany(self, wall_group):

                # self.rect.move(self.direction_red)

                # if keys[pg.K_SPACE]:
                self.rect.y += 10 * sin_a
                self.rect.x += 10 * cos_a

                pg.draw.line(screen, GREEN, (self.rect.x, self.rect.y), (sin_a + 10000, cos_a + 10000), 2)

                # print(sin_a, cos_a)
                # print(math.cos(self.angel_red), math.sin(self.angel_red))
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
                    self.rect.y -=1
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
                self.rotated = -self.rotated
                self.rotated_red = True
                self.rect.x -= math.cos(self.angel_red)
                self.rect.y -= math.sin(self.angel_red)

            # else:
            #     self.rect.x -= self.direction_red.x * 0.0000001
            #     self.rect.y -= self.direction_red.y * 0.0000001
            # self.direction_red.rotate_ip(self.angel_red)

        # angle_red = self.direction_red.angle_to((1, 0))
            self.angel_red += self.rotated
            if self.angel_red <= -360 or self.angel_red >= 360:
                self.angel_red = 0
            print(self.angel_red)
            # print(self.angel_red)
        rotated_red_tank = pg.transform.rotate(self.image, self.angel_red)
        screen.blit(rotated_red_tank, rotated_red_tank.get_rect(center=(round(self.rect.x + 22), round(self.rect.y + 22))))