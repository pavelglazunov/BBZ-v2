import pygame as pg

from game_setting import *
from menu import start_menu


def start():
    vx = 0.125
    vy = 0.03125
    v2 = 0.0625

    vx1 = 0.1875
    vy1 = 0.0625

    # updating position
    x, y = 246, 453
    x1, y1 = 246, 479

    xb, yb = 544, 487
    xb1, yb1 = 544, 500

    xp, yp = 517, 514
    xp1, yp1 = 517, 543

    xu, yu = 532, 518
    xu1, yu1 = 532, 535

    xn, yn = 592, 456
    xn1, yn1 = 592, 477

    xbb, ybb = 606, 463
    xbb1, ybb1 = 606, 491

    xuu, yuu = 527, 544
    xuu1, yuu1 = 527, 573

    xi, yi = 582, 559
    xi1, yi1 = 582, 586

    xii, yii = 619, 522
    xii1, yii1 = 619, 549

    xt, yt = 678, 537
    xt1, yt1 = 678, 550

    xe, ye = 668, 550
    xe1, ye1 = 668, 578

    thick = 4
    game_name = 'BBZ'
    color = GREEN

    pg.init()
    pg.display.set_caption(game_name)

    screen = pg.display.set_mode(size)

    running = True
    now_draw = True

    clock = pg.time.Clock()
    FPS = 60

    screen.fill(BG_BLUE)

    im = pg.image.load('./texture/updating_texture/logo_bbz.png').convert_alpha()
    screen.blit(im, (350, 130))

    tic_snake = 0
    tic = 0
    queue = 0
    list_of_updating_text = [pg.image.load('./texture/updating_texture/loading0.png'),
                             pg.image.load('./texture/updating_texture/loading1.png'),
                             pg.image.load('./texture/updating_texture/loading2.png'),
                             pg.image.load('./texture/updating_texture/loading3.png')]
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.MOUSEBUTTONDOWN:
                now_draw = False
            if event.type == pg.MOUSEBUTTONUP:
                now_draw = True

        if now_draw:
            if x < 480 and x1 < 480:
                pg.draw.polygon(screen, color, [(246, 453), (247, 479), (x, y), (x1, y1)], 0)
                x += vx
                y += vy
                x1 += vx
                y1 += vy
            else:
                if x < 513 and x1 < 513:
                    pg.draw.polygon(screen, color, [(482, 508), (482, 537), (x + 2, y - 1), (x1 + 2, y1 - 2)], 0)
                    x += v2
                    y -= v2
                    x1 += v2
                    y1 -= v2
                else:
                    if x < 540:
                        pg.draw.polygon(screen, color, [(517, 472), (517, 503), (x + 5, y - 2), (x1 + 5, y1 - 2)], 0)
                        if x1 > 520:
                            x1 = 520
                            y1 = 500
                        x += vx
                        y += vy
                        x1 += vx
                        y1 += vy
                    else:
                        if xb > 517:
                            pg.draw.polygon(screen, color, [(544, 487), (544, 500), (xb, yb), (xb1, yb1)], 0)
                            if xb <= 517:
                                xb = 517
                                yb1 = 512
                            if xb1 <= 530:
                                xb1 = 530
                                yb1 = 512
                            xb -= v2
                            yb += v2
                            xb1 -= v2
                            yb1 += v2
                        else:
                            if xp1 < 530:
                                pg.draw.polygon(screen, color, [(517, 514), (517, 543), (xp, yp), (xp1, yp1)], 0)
                                xp += vx1
                                yp += vy1
                                xp1 += vx1
                                yp1 += vy1
                            else:
                                if xu < 590:
                                    pg.draw.polygon(screen, color, [(532, 518), (532, 535), (xu, yu), (xu1, yu1)], 0)
                                    xu += v2
                                    yu -= v2
                                    xu1 += v2
                                    yu1 -= v2
                                else:
                                    if xn < 606:
                                        pg.draw.polygon(screen, color, [(592, 456), (592, 477), (xn, yn), (xn1, yn1)],
                                                        0)
                                        xn += v2
                                        yn += v2
                                        xn1 += v2
                                        yn1 -= v2
                                    else:
                                        if xbb > 525:
                                            pg.draw.polygon(screen, color,
                                                            [(606, 463), (606, 491), (xbb, ybb), (xbb1, ybb1)], 0)
                                            if xbb1 < 550:
                                                xbb1 = 550
                                                ybb1 = 550
                                            xbb -= v2
                                            ybb += v2
                                            xbb1 -= v2
                                            ybb1 += v2
                                        else:
                                            if xuu < 580:
                                                pg.draw.polygon(screen, color,
                                                                [(527, 544), (527, 573), (xuu, yuu), (xuu1, yuu1)], 0)
                                                xuu += vx
                                                yuu += vy
                                                xuu1 += vx
                                                yuu1 += vy
                                            else:
                                                if xi < 617:
                                                    pg.draw.polygon(screen, color,
                                                                    [(582, 559), (582, 586), (xi, yi), (xi1, yi1)], 0)
                                                    xi += v2
                                                    yi -= v2
                                                    xi1 += v2
                                                    yi1 -= v2
                                                else:
                                                    if xii < 680:
                                                        pg.draw.polygon(screen, color,
                                                                        [(619, 522), (619, 549), (xii, yii),
                                                                         (xii1, yii1)], 0)
                                                        if xii1 > 665:
                                                            xii1 = 665
                                                            yii1 = 548
                                                        xii += vx
                                                        yii += vy
                                                        xii1 += vx
                                                        yii1 += vy
                                                    else:
                                                        if xt > 666:
                                                            pg.draw.polygon(screen, color,
                                                                            [(678, 537), (678, 550), (xt, yt),
                                                                             (xt1, yt1)], 0)
                                                            xt -= v2
                                                            yt += v2
                                                            xt1 -= v2
                                                            yt1 -= v2
                                                        else:
                                                            if xe < 712:
                                                                pg.draw.polygon(screen, color,
                                                                                [(668, 550), (668, 578), (xe, ye),
                                                                                 (xe1, ye1)], 0)
                                                                xe += vx
                                                                ye += vy
                                                                xe1 += vx
                                                                ye1 += vy
                                                            else:
                                                                pg.draw.polygon(screen, RED, [(712, 565),
                                                                                                        (712, 585),
                                                                                                        (735, 575)], 0)
                                                                tic_snake += 1

                                                                if tic_snake > FPS * 2:
                                                                    now_draw = False
                                                                    start_menu()

            outline_color = BLACK

            pg.draw.polygon(screen, outline_color, [(245, 450),
                                                    (480, 508),
                                                    (480, 539),
                                                    (245, 480)], thick)

            pg.draw.polygon(screen, outline_color, [(480, 508),
                                                    (480, 539),
                                                    (515, 503),
                                                    (515, 473)], thick)

            pg.draw.polygon(screen, outline_color, [(515, 473),
                                                    (515, 503),
                                                    (522, 505),
                                                    (545, 482)], thick)

            pg.draw.polygon(screen, outline_color, [(545, 482),
                                                    (545, 501),
                                                    (530, 516),
                                                    (515, 512)], thick)

            pg.draw.polygon(screen, outline_color, [(515, 512),
                                                    (515, 545),
                                                    (525, 548),
                                                    (525, 542),
                                                    (530, 537),
                                                    (530, 516)], thick)

            pg.draw.polygon(screen, outline_color, [(530, 516),
                                                    (530, 537),
                                                    (590, 477),
                                                    (590, 456)], thick)

            pg.draw.polygon(screen, outline_color, [(590, 456),
                                                    (590, 477),
                                                    (606, 462)], thick)

            pg.draw.polygon(screen, outline_color, [(606, 462),
                                                    (606, 493),
                                                    (550, 549),
                                                    (525, 542)], thick)

            pg.draw.polygon(screen, outline_color, [(525, 542),
                                                    (525, 575),
                                                    (580, 588),
                                                    (580, 557)], thick)

            pg.draw.polygon(screen, outline_color, [(580, 557),
                                                    (580, 588),
                                                    (617, 551),
                                                    (617, 520)], thick)

            pg.draw.polygon(screen, outline_color, [(617, 551),
                                                    (617, 520),
                                                    (680, 535),
                                                    (666, 548),
                                                    (665, 562)], thick)

            pg.draw.polygon(screen, outline_color, [(680, 535),
                                                    (666, 548),
                                                    (680, 552)], thick)

            pg.draw.polygon(screen, outline_color, [(666, 548),
                                                    (666, 580),
                                                    (712, 590),
                                                    (712, 560)], thick)

            pg.draw.polygon(screen, outline_color, [(712, 565),
                                                    (712, 585),
                                                    (735, 575)], 3)

            pg.draw.circle(screen, BLACK, (680, 560), 2)
            pg.draw.circle(screen, BLACK, (680, 575), 2)

        clock.tick(FPS * 10)
        pg.display.flip()

    pg.quit()


# start()
