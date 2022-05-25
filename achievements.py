import pygame as pg


def main():
    pg.init()
    FPS = 60

    screen = pg.display.set_mode((1000, 700))
    clock = pg.time.Clock()




    running = True

    while running:
        keys = pg.key.get_pressed()
        for event in pg.event.get():
            if event.type == pg.QUIT or keys[pg.K_ESCAPE]:
                running = False

        screen.fill((0, 0, 0))

        pg.display.flip()
        clock.tick(FPS)

    pg.quit()

# main()
