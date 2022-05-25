from PyQt5.QtWidgets import QWidget, QPushButton
from PyQt5.QtWidgets import QLabel
from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from loading_bar import start

list_of_achievements = [False, False, False, False, False, False, False, False, False, False, False, False, False]


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def get_windows(self, list_of_window5):
        self.list_of_window5 = list_of_window5

    def initUI(self):
        self.xo_rules_is_active = False
        self.osu_rules_is_active = False
        self.city_game_rules_is_active = False
        self.cats_rules_is_active = False
        self.is_active = False

        self.city_game_played = False
        self.osu_game_played = False
        self.xo_game_played = False
        self.cats_game_played = False

        self.xo_rules_count = 0
        self.osu_rules_count = 0
        self.cats_rules_count = 0
        self.city_rules_count = 0
        self.rules_count = 0

        self.timer = 3
        self.time = 4
        self.secret_time = 4
        self.end_time = 4
        self.time_bbz_ach = 4
        self.btn_time = 1

        self.mouse_x = 660
        self.mouse_y = -10
        self.mouse_an_x = 660
        self.mouse_an_y = 10
        self.bonus_mouse_wait = 1

        self.main_window = QWidget()
        self.main_window.resize(1000, 700)
        self.main_window.setGeometry(300, 300, 1000, 700)
        self.main_window.setFixedSize(1000, 700)

        self.background = QLabel(self)
        background1 = QPixmap('./texture/menu_texture/background_menu')
        self.background.setPixmap(background1)
        self.background.move(0, 0)

        # Бонус кнопки
        self.bonus1 = QLabel(self)
        self.bonus1.setPixmap(QPixmap('./texture/menu_texture/bunus.png'))
        self.bonus1.resize(100, 100)
        self.bonus1.move(50, 80)

        self.bonus_btn = QPushButton('', self)
        self.bonus_btn.setIcon(QIcon('./texture/menu_texture/bonus_btn'))
        self.bonus_btn.setIconSize(QSize(100, 100))
        self.bonus_btn.resize(100, 100)
        self.bonus_btn.move(50, 80)

        self.bonus_btn2 = QPushButton('', self)
        self.bonus_btn2.setIcon(QIcon('./texture/menu_texture/bonus_btn2'))
        self.bonus_btn2.setIconSize(QSize(100, 100))
        self.bonus_btn2.resize(100, 100)
        self.bonus_btn2.move(888, 10)

        self.bonus_btn3 = QPushButton('', self)
        self.bonus_btn3.setIcon(QIcon('./texture/menu_texture/bonus_btn3'))
        self.bonus_btn3.setIconSize(QSize(100, 100))
        self.bonus_btn3.resize(100, 100)
        self.bonus_btn3.move(150, 500)

        self.bonus_mouse = QLabel(self)
        self.bonus_mouse.setPixmap(QPixmap('./texture/menu_texture/bonus_btn_mouse.png'))
        self.bonus_mouse.resize(100, 100)
        self.bonus_mouse.move(self.mouse_x, self.mouse_y)

        self.bonus_mouse_btn = QPushButton(self)
        self.bonus_mouse_btn.setIcon(QIcon('./texture/menu_texture/bonus_mouse_btn'))
        self.bonus_mouse_btn.setIconSize(QSize(100, 100))
        self.bonus_mouse_btn.resize(100, 100)
        self.bonus_mouse_btn.move(self.mouse_x, self.mouse_y)

        self.error = QLabel(self)
        self.error.resize(200, 200)
        self.error.move(755, 490)
        self.error.setPixmap(QPixmap('./texture/menu_texture/error_texture.png'))
        self.error.hide()

        self.logo_bbz = QLabel(self)
        self.logo_bbz.move(380, 65)
        self.logo_bbz.setPixmap(QPixmap('./texture/menu_texture/bbz.png'))

        self.one_player_game = QLabel(self)
        self.one_player_game.move(180, 230)
        self.one_player_game.setPixmap(QPixmap('./texture/menu_texture/one_player.png'))

        self.two_player_game = QLabel(self)
        self.two_player_game.move(580, 230)
        self.two_player_game.setPixmap(QPixmap('./texture/menu_texture/two_player.png'))

        self.xo_btn = QPushButton('', self)
        self.xo_btn.resize(100, 100)
        self.xo_btn.move(550, 300)
        self.xo_btn.setIcon(QIcon('./texture/menu_texture/xo_logo.png'))
        self.xo_btn.setIconSize(QSize(100, 100))
        self.xo_btn.clicked.connect(self.xo_game)

        self.xo_rules = QPushButton(self)
        self.xo_rules.resize(100, 50)
        self.xo_rules.move(550, 420)
        self.xo_rules.clicked.connect(self.xo_rule)
        self.xo_rules.setIcon(QIcon('./texture/menu_texture/rules_btn.png'))
        self.xo_rules.setIconSize(QSize(100, 50))

        self.osu_btn = QPushButton('', self)
        self.osu_btn.resize(100, 100)
        self.osu_btn.move(350, 300)
        self.osu_btn.setIcon(QIcon('./texture/menu_texture/osu_logo.png'))
        self.osu_btn.setIconSize(QSize(100, 100))
        self.osu_btn.clicked.connect(self.osu_game)

        self.osu_rules_btn = QPushButton(self)
        self.osu_rules_btn.resize(100, 50)
        self.osu_rules_btn.move(350, 420)
        self.osu_rules_btn.setIcon(QIcon('./texture/menu_texture/rules_btn.png'))
        self.osu_rules_btn.setIconSize(QSize(100, 50))
        self.osu_rules_btn.clicked.connect(self.osu_rules)

        self.city_game_btn = QPushButton('', self)
        self.city_game_btn.resize(100, 100)
        self.city_game_btn.move(150, 300)
        self.city_game_btn.setIcon(QIcon('./texture/menu_texture/city_game_logo.png'))
        self.city_game_btn.setIconSize(QSize(100, 100))
        self.city_game_btn.clicked.connect(self.city_game)

        self.city_game_rules = QPushButton(self)
        self.city_game_rules.resize(100, 50)
        self.city_game_rules.move(150, 420)
        self.city_game_rules.setIcon(QIcon('./texture/menu_texture/rules_btn.png'))
        self.city_game_rules.setIconSize(QSize(100, 50))
        self.city_game_rules.clicked.connect(self.city_game_rule)

        self.cats_btn = QPushButton('', self)
        self.cats_btn.resize(100, 100)
        self.cats_btn.move(750, 300)
        self.cats_btn.setIcon(QIcon('./texture/menu_texture/cats_logo'))
        self.cats_btn.setIconSize(QSize(100, 100))
        self.cats_btn.clicked.connect(self.cats_game)

        self.cats_rules = QPushButton(self)
        self.cats_rules.resize(100, 50)
        self.cats_rules.move(750, 420)
        self.cats_rules.setIcon(QIcon('./texture/menu_texture/rules_btn.png'))
        self.cats_rules.setIconSize(QSize(100, 50))
        self.cats_rules.clicked.connect(self.cat_rules)

        self.exit_btn = QPushButton('', self)
        self.exit_btn.resize(50, 50)
        self.exit_btn.move(0, 650)
        self.exit_btn.setIcon(QIcon('./texture/menu_texture/exit_button_texture.png'))
        self.exit_btn.setIconSize(QSize(100, 50))
        self.exit_btn.clicked.connect(self.exit)

        self.setting_btn = QPushButton('', self)
        self.setting_btn.resize(50, 50)
        self.setting_btn.move(950, 650)
        self.setting_btn.setIcon(QIcon('./texture/menu_texture/crash_button.png'))
        self.setting_btn.setIconSize(QSize(90, 90))

        self.achievements_btn = QPushButton(self)
        self.achievements_btn.resize(50, 50)
        self.achievements_btn.setIcon(QIcon('./texture/menu_texture/achievements_btn_v2.png'))
        self.achievements_btn.setIconSize(QSize(50, 50))

        self.next_bbz = QPushButton(self)
        self.next_bbz.move(950, 325)
        self.next_bbz.resize(50, 50)
        self.next_bbz.setIcon(QIcon('./texture/menu_texture/next.png'))
        self.next_bbz.setIconSize(QSize(50, 50))
        self.next_bbz.clicked.connect(self.next)

    def xo_rule(self):  # при нажатии на кнопку открывает правила, если правила открыты - закрывает их
        if not self.xo_rules_is_active:
            self.hide_ruled()
            self.xo_rules.setIcon(QIcon('./texture/menu_texture/rules_btn_clicced.png'))

            self.xo_rules_is_active = True
        elif self.xo_rules_is_active:
            self.xo_rules.setIcon(QIcon('./texture/menu_texture/rules_btn.png'))
            self.xo_rules_is_active = False

    def osu_rules(self):  # при нажатии на кнопку открывает правила, если правила открыты - закрывает их
        if not self.osu_rules_is_active:
            self.hide_ruled()
            self.osu_rules_btn.setIcon(QIcon('./texture/menu_texture/rules_btn_clicced.png'))
            self.osu_rules_is_active = True

        elif self.osu_rules_is_active:
            self.osu_rules_btn.setIcon(QIcon('./texture/menu_texture/rules_btn.png'))
            self.osu_rules_is_active = False

    def city_game_rule(self):  # при нажатии на кнопку открывает правила, если правила открыты - закрывает их
        if not self.city_game_rules_is_active:
            self.hide_ruled()
            self.city_game_rules.setIcon(QIcon('./texture/menu_texture/rules_btn_clicced.png'))
            self.city_game_rules_is_active = True

        elif self.city_game_rules_is_active:
            self.city_game_rules.setIcon(QIcon('./texture/menu_texture/rules_btn.png'))
            self.city_game_rules_is_active = False

    def cat_rules(self):  # при нажатии на кнопку открывает правила, если правила открыты - закрывает их
        if not self.cats_rules_is_active:
            self.hide_ruled()
            self.cats_rules.setIcon(QIcon('./texture/menu_texture/rules_btn_clicced.png'))
            self.cats_rules_is_active = True
        elif self.cats_rules_is_active:
            self.cats_rules.setIcon(QIcon('./texture/menu_texture/rules_btn.png'))
            self.cats_rules_is_active = False

    def hide_ruled(self):  # закрывает все правила
        self.error.hide()

        self.xo_rules.setIcon(QIcon('./texture/menu_texture/rules_btn.png'))
        self.city_game_rules.setIcon(QIcon('./texture/menu_texture/rules_btn.png'))
        self.osu_rules_btn.setIcon(QIcon('./texture/menu_texture/rules_btn.png'))
        self.cats_rules.setIcon(QIcon('./texture/menu_texture/rules_btn.png'))

        self.xo_rules_is_active = False
        self.osu_rules_is_active = False
        self.city_game_rules_is_active = False
        self.cats_rules_is_active = False

    def osu_game(self):  # переход в игру
        self.osu_btn.setIcon(QIcon('./texture/menu_texture/osu_logo_clicced.png'))
        self.hide_ruled()
        self.btn_osu_timer()

    def cats_game(self):  # переход в игру
        self.cats_btn.setIcon(QIcon('./texture/menu_texture/cats_logo_clicced.png'))
        self.hide_ruled()
        self.btn_cats_timer()

    def xo_game(self):  # переход в игру
        self.xo_btn.setIcon(QIcon('./texture/menu_texture/xo_logo_clicced.png'))
        self.hide_ruled()
        self.btn_xo_timer()

    def city_game(self):  # переход в игру
        self.city_game_btn.setIcon(QIcon('./texture/menu_texture/city_game_logo_clicced.png'))
        self.btn_city_timer()

    def btn_city_timer(self):  # таймер для анимации кнопки игры
        if self.btn_time > 0:
            self.btn_time -= 1
            QTimer().singleShot(300, self.btn_city_timer)
        else:
            self.city_game_btn.setIcon(QIcon('./texture/menu_texture/city_game_logo.png'))
            self.btn_time = 1

    def btn_osu_timer(self):  # таймер для анимации кнопки игры
        if self.btn_time > 0:
            self.btn_time -= 1
            QTimer().singleShot(300, self.btn_osu_timer)
        else:
            self.btn_time = 1
            self.osu_btn.setIcon(QIcon('./texture/menu_texture/osu_logo.png'))

    def btn_xo_timer(self):  # таймер для анимации кнопки игры
        if self.btn_time > 0:
            self.btn_time -= 1
            QTimer().singleShot(300, self.btn_xo_timer)
        else:
            self.btn_time = 1
            self.xo_btn.setIcon(QIcon('./texture/menu_texture/xo_logo.png'))

    def btn_cats_timer(self):  # таймер для анимации кнопки игры
        if self.btn_time > 0:
            self.btn_time -= 1
            QTimer().singleShot(300, self.btn_cats_timer)
        else:
            self.btn_time = 1
            self.cats_btn.setIcon(QIcon('./texture/menu_texture/cats_logo.png'))

    def next(self):
        self.list_of_window5.close()
        start()

    def exit(self):  # выход
        self.ex = Exit()
        self.ex.close()
        self.ex.show()

    def exit_game(self):
        exit()


class Exit(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(400, 90)
        self.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)
        self.setWindowFlags(Qt.WindowMaximizeButtonHint)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setFixedSize(400, 90)
        self.bg = QLabel(self)
        self.bg.setPixmap(QPixmap('./texture/menu_texture/exit_window.png'))
        self.setWindowTitle('Exit')

        self.exit_bnt = QPushButton(self)
        self.exit_bnt.move(85, 45)
        self.exit_bnt.resize(100, 30)
        self.exit_bnt.setText('Да')
        self.exit_bnt.clicked.connect(self.exit)

        self.scip = QPushButton(self)
        self.scip.move(220, 45)
        self.scip.resize(100, 30)
        self.scip.setText('Нет')
        self.scip.clicked.connect(self.no_exit)

    def exit(self):
        exit()

    def no_exit(self):
        self.close()
