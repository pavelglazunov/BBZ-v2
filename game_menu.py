import sys
import os

from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QLabel, QLineEdit
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication, QWidget

from old import Example
from menu import start_menu
from loading_bar import start


class Qt_part(QWidget):

    def get_windows(self, list_of_window3):
        self.list_of_window3 = list_of_window3

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.leter_B1_pos_x = -80
        self.leter_B1_pos_y = 300

        self.leter_B2_pos_x = 480
        self.leter_B2_pos_y = 0

        self.leter_Z_pos_x = 1050
        self.leter_Z_pos_y = 300

        self.loading_btn_size_x = 20
        self.loading_btn_size_y = 15

        self.timer = 2

        self.main_window = QWidget()
        self.main_window.resize(1000, 700)
        self.main_window.setWindowTitle('BBZ_game')
        self.main_window.setFixedSize(1000, 700)
        self.main_window.setWindowOpacity(0.5)

        self.text = QLabel(self)
        politick = open('./txt document/politic.txt', encoding='utf-8').read().split('\n')
        for i in politick:
            self.text.setText(self.text.text() + i + '\n')

        self.scroll_area = QScrollArea()
        self.scroll_area.setWindowTitle("Политика конфидециальности")

        self.scroll_area.setFixedSize(400, 500)
        self.scroll_area.setWidget(self.text)

        self.scroll_area.hide()

        self.background = QLabel(self)
        self.background.resize(1000, 700)
        self.background.setFixedSize(1000, 700)
        self.background.setPixmap(QPixmap('./texture/loading_texture/loading_background.png'))

        self.politic_background = QLabel(self)
        self.politic_background.resize(1000, 700)
        self.politic_background.setFixedSize(1000, 700)
        self.politic_background.setPixmap(QPixmap('./texture/loading_texture/politic_background.png'))
        self.politic_background.hide()

        self.progess_bar = QLabel(self)
        self.progess_bar.move(264, 464)
        self.progess_bar.resize(570, 26)
        self.progess_bar.setPixmap(QPixmap('./texture/loading_texture/loading_progress_bar.png'))

        self.loading_btn = QPushButton(self)
        self.loading_btn.move(270, 470)
        self.loading_btn.resize(self.loading_btn_size_x, self.loading_btn_size_y)
        self.loading_btn.setStyleSheet('background: rgb(255, 255, 255);')
        self.loading_btn.clicked.connect(self.bonus_show)

        self.loading_btn.hide()

        self.later_B1 = QLabel(self)
        self.later_B1.move(380, 300)
        self.later_B1.setPixmap(QPixmap('./texture/loading_texture/later_B1.png'))
        self.later_B1.setPalette(self.palette())
        self.later_B1.setWindowOpacity(1 - 5)

        self.later_B2 = QLabel(self)
        self.later_B2.move(self.leter_B2_pos_x, self.leter_B2_pos_y)
        self.later_B2.setPixmap(QPixmap('./texture/loading_texture/later_B2.png'))
        self.later_B2.show()

        self.later_Z = QLabel(self)
        self.later_Z.move(self.leter_Z_pos_x, self.leter_Z_pos_y)
        self.later_Z.setPixmap(QPixmap('./texture/loading_texture/later_Z.png'))
        self.later_Z.show()

        self.bonus = QLabel(self)
        self.bonus.resize(150, 70)
        self.bonus.move(300, 500)
        self.bonus.setPixmap(QPixmap('./texture/loading_texture/bonus.png'))
        self.bonus.hide()

        self.politic_btn = QPushButton(self)
        self.politic_btn.setIcon(QIcon('./texture/loading_texture/here_texture'))
        self.politic_btn.setIconSize(QSize(100, 50))
        self.politic_btn.resize(70, 50)
        self.politic_btn.move(870, 497)
        self.politic_btn.hide()
        self.politic_btn.clicked.connect(self.privat_policy)

        self.politic_accept_btn = QPushButton(self)
        self.politic_accept_btn.setIconSize(QSize(100, 50))
        self.politic_accept_btn.resize(100, 50)
        self.politic_accept_btn.move(400, 550)
        self.politic_accept_btn.setIcon(QIcon('./texture/loading_texture/accept_btn.png'))
        self.politic_accept_btn.setIconSize(QSize(100, 50))
        self.politic_accept_btn.hide()
        self.politic_accept_btn.clicked.connect(self.start)

        self.politic_not_accept_btn = QPushButton(self)
        self.politic_not_accept_btn.setIconSize(QSize(100, 50))
        self.politic_not_accept_btn.resize(100, 50)
        self.politic_not_accept_btn.move(520, 550)
        self.politic_not_accept_btn.setIcon(QIcon('./texture/loading_texture/not_accept_btn.png'))
        self.politic_not_accept_btn.setIconSize(QSize(100, 50))
        self.politic_not_accept_btn.hide()
        self.politic_not_accept_btn.clicked.connect(self.exit_game)

        self.scip_btn = QPushButton(self)
        self.scip_btn.resize(50, 50)
        self.scip_btn.move(950, 650)
        self.scip_btn.setIcon(QIcon('./texture/loading_texture/scip_btn.png'))
        self.scip_btn.setIconSize(QSize(50, 50))
        self.scip_btn.clicked.connect(self.start)

        self.start_btn = QPushButton(self)
        self.start_btn.resize(200, 50)
        self.start_btn.move(420, 400)
        self.start_btn.setIcon(QIcon('./texture/loading_texture/start_btn.png'))
        self.start_btn.setIconSize(QSize(200, 50))
        self.start_btn.clicked.connect(self.start_game)
        self.start_btn.hide()

        self.loading()
        self.animation()

    def btn_accept_timer(self):
        if self.btn_time > 0:
            self.btn_time -= 1
            QTimer().singleShot(300, self.btn_accept_timer)
        else:
            self.politic_accept_btn.setIcon(QIcon('./texture/menu_texture/accept_btn.png'))
            self.animation_up()

            self.politic_background.hide()
            self.politic_accept_btn.hide()
            self.politic_not_accept_btn.hide()
            self.politic_btn.hide()
            self.scroll_area.close()

            self.timer = 0
            self.animation_up_timer()
            self.btn_time = 1

    def btn_not_accept_timer(self):
        if self.btn_time > 0:
            self.btn_time -= 1
            QTimer().singleShot(300, self.btn_not_accept_timer)
        else:
            self.politic_not_accept_btn.setIcon(QIcon('./texture/menu_texture/not_accept_btn.png'))
            self.btn_time = 1
            exit()

    def bonus_show(self):
        self.bonus.show()
        self.bonus_timer()

    def bonus_timer(self):
        if self.timer > 0:
            self.timer -= 2
            QTimer().singleShot(1000, self.bonus_timer)
        else:
            self.timer = 2
            self.bonus.hide()

    def animation(self):
        animation_curve = QEasingCurve.OutBounce

        self.later_B1.move(380, 300)
        self.later_B2.move(480, 300)
        self.later_Z.move(580, 300)

        animation1 = QPropertyAnimation(self.later_B1, b'pos', self)
        animation1.setEasingCurve(animation_curve)
        animation1.setDuration(4500)
        animation1.setKeyValueAt(0, QPoint(-80, 300))

        animation2 = QPropertyAnimation(self.later_Z, b'pos', self)
        animation2.setEasingCurve(animation_curve)
        animation2.setDuration(4500)
        animation2.setKeyValueAt(0, QPoint(1050, 300))

        animation3 = QPropertyAnimation(self.later_B2, b'pos', self)
        animation3.setEasingCurve(animation_curve)
        animation3.setDuration(3500)
        animation3.setKeyValueAt(0, QPoint(480, -100))

        first_animation_group = QParallelAnimationGroup(self)
        first_animation_group.addAnimation(animation1)
        first_animation_group.addAnimation(animation2)
        first_animation_group.addAnimation(animation3)
        first_animation_group.start()

    def animation_up(self):
        animation_curve1 = QEasingCurve.InQuad

        self.later_B1.move(380, 220)
        self.later_B2.move(480, 220)
        self.later_Z.move(580, 220)

        animation1_1 = QPropertyAnimation(self.later_B1, b'pos', self)
        animation1_1.setEasingCurve(animation_curve1)
        animation1_1.setDuration(1000)
        animation1_1.setKeyValueAt(0, QPoint(380, 300))

        animation2_2 = QPropertyAnimation(self.later_Z, b'pos', self)
        animation2_2.setEasingCurve(animation_curve1)
        animation2_2.setDuration(1200)
        animation2_2.setKeyValueAt(0, QPoint(580, 300))

        animation3_3 = QPropertyAnimation(self.later_B2, b'pos', self)
        animation3_3.setEasingCurve(animation_curve1)
        animation3_3.setDuration(1100)
        animation3_3.setKeyValueAt(0, QPoint(480, 300))

        second_animation_group = QParallelAnimationGroup(self)
        second_animation_group.addAnimation(animation1_1)
        second_animation_group.addAnimation(animation2_2)
        second_animation_group.addAnimation(animation3_3)
        second_animation_group.start()

    def loading(self):
        if self.loading_btn_size_x < 495:
            self.loading_btn.show()
            self.loading_btn_size_x += 1
            self.loading_btn.resize(self.loading_btn_size_x, self.loading_btn_size_y)
            QTimer().singleShot(9.5, self.loading)
        else:
            self.bonus.hide()
            self.progess_bar.hide()
            self.politic_btn.hide()
            self.loading_btn.hide()
            if open('./txt document/updating.txt', encoding='utf-8').read().split('\n')[0] == 'False':
                # f = open('./txt document/updating.txt', 'w')
                # f.write('True')
                # f.close()

                self.politic_background.show()
                self.politic_btn.show()
                # start_menu()
            elif open('./txt document/updating.txt', encoding='utf-8').read().split('\n')[0] == 'True':
                # print('was update')
                self.start()
            else:
                p = os.path.abspath('./txt document/updating.txt')
                print(f'Файл \'updating.txt\' ({p}) - поврежден, '
                      f'программа автоматически перезапишет его, пожалуйста перезапустите игру')
                f = open('./txt document/updating.txt', 'w')
                f.write('False')
                f.close()
                exit()

    def privat_policy(self):
        self.scroll_area.hide()
        self.scroll_area.show()
        self.politic_accept_btn.show()
        self.politic_not_accept_btn.show()

    def start_game(self):
        self.start_btn.setIcon(QIcon('./texture/loading_texture/start_btn_clicced.png'))
        self.start_game_timer()

    def start_game_timer(self):
        if self.btn_time > 0:
            self.btn_time -= 1
            QTimer().singleShot(300, self.start_game_timer)
        else:
            self.btn_time = 1
            # print(5151)
            if open('./txt document/updating.txt', encoding='utf-8').read().split('\n')[0] == 'False':
                f = open('./txt document/updating.txt', 'w')
                f.write('True')
                f.close()
                old_window.get_windows(list_of_windows)
                list_of_windows.setCurrentIndex(1)
            elif open('./txt document/updating.txt', encoding='utf-8').read().split('\n')[0] == 'True':
                # print('was update')
                self.list_of_window3.close()
                # self.start()
                start()
            else:
                p = os.path.abspath('./txt document/updating.txt')
                print(f'Файл \'updating.txt\' ({p}) - поврежден, '
                      f'программа автоматически перезапишет его, пожалуйста перезапустите игру')
                f = open('./txt document/updating.txt', 'w')
                f.write('False')
                f.close()
                exit()
                # f = open("/txt document/updating.txt", 'w')
                # print(f.write('True'))
                # print(f.seek(3))
                # print(f.write('34352'))
                # f.close()
            # start()
            # if open('./txt document/updating.txt', encoding='utf-8').read().split('\n')[0] == 'False':
            #     f = open('./txt document/updating.txt', 'w')
            #     f.write('True')
            #     f.close()
            #     old_window.get_windows(list_of_windows)
            #     list_of_windows.setCurrentIndex(1)
            # elif open('./txt document/updating.txt', encoding='utf-8').read().split('\n')[0] == 'True':
            #     print('was update')
            #     self.list_of_window3.close()
            #     start_menu()
            # else:
            #     p = os.path.abspath('./txt document/updating.txt')
            #     print(f'Файл \'updating.txt\' ({p}) - поврежден, '
            #           f'программа автоматически перезапишет его, пожалуйста перезапустите игру')
            #     f = open('./txt document/updating.txt', 'w')
            #     f.write('False')
            #     f.close()
            #     exit()
            #     f = open("/txt document/updating.txt", 'w')
            #     print(f.write('True'))
            #     print(f.seek(3))
            #     print(f.write('34352'))
            #     f.close()

    def start(self):
        self.btn_time = 1
        self.politic_accept_btn.setIcon(QIcon('./texture/loading_texture/accept_btn_clicced.png'))
        self.btn_accept_timer()

    def animation_up_timer(self):
        if self.timer < 1:
            self.timer += 1
            QTimer().singleShot(1000, self.animation_up_timer)
        else:
            self.start_btn.show()
            self.timer = 0

    def exit_game(self):
        self.btn_time = 1
        self.politic_not_accept_btn.setIcon(QIcon('./texture/loading_texture/not_accept_btn_clicced.png'))
        self.btn_not_accept_timer()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    list_of_windows = QStackedWidget()  # создание списка окон

    # объявление окон
    loading_window = Qt_part()
    old_window = Example()

    # добавление окон в список
    list_of_windows.addWidget(loading_window)  # 0
    list_of_windows.addWidget(old_window)  # 1

    # переход к загрузке
    loading_window.get_windows(list_of_windows)
    list_of_windows.setCurrentIndex(0)

    # задание параметров всех окон
    list_of_windows.setWindowTitle('BBZ_game')
    list_of_windows.setWindowIcon(QIcon('./texture/menu_texture/game_logo'))
    list_of_windows.resize(1000, 700)
    list_of_windows.setFixedSize(1000, 700)
    # list_of_windows.setWindowFlag(Qt.FramelessWindowHint)
    list_of_windows.adjustSize()
    list_of_windows.clearFocus()
    list_of_windows.show()

    sys.exit(app.exec())
