import sys
import logging

from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtWebEngineWidgets import *

logger = logging.getLogger("module.app")
backgroundMainColor = '#e8e8e8' #D9D9D9
FORMAT = '%(asctime)s :: %(levelname)s :: %(name)s:%(lineno)s :: %(message)s' # Задаём формат логов

def get_stream_handler():
    sh = logging.StreamHandler()
    sh.setFormatter(logging.Formatter(FORMAT))
    sh.setLevel(logging.DEBUG)
    return sh

def init_button(nameIcon, sizeX, sizeY):
    button = QPushButton()
    button.setIcon(QIcon('icons/%s.png'%nameIcon))
    button.setIconSize(QSize(sizeX, sizeY))
    button.setStyleSheet('border-radius: 50;background-color: %s;'%backgroundMainColor)

    return button

# Запускаем работу приложения
def main():
    logger.info("Start loading app module")
    app = QApplication(sys.argv)
    app.setStyleSheet("MainWindow{background-color: %s;}"%backgroundMainColor) 
    win = MainWindow()
    win.show()
    app.exit(app.exec())

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Настройки главного окна
        self.setWindowTitle('Генератор полётных заданий')
        self.setGeometry(50, 50, 1200, 900)
        self.setMinimumSize(960, 920)

        # Создание и настройка кнопок
        butNew = init_button("butNew", 65, 65)
        butNew.clicked.connect(self.close)
        butSave = init_button("butSave", 65, 65)
        butSave.clicked.connect(self.close)
        butFile = init_button("butFile", 65, 65)
        butFile.clicked.connect(self.close)
        butSett = init_button("butSett", 65, 65)
        butSett.clicked.connect(self.close)
        butPoint = init_button("butPoint", 130, 65)
        butPoint.clicked.connect(self.close)
        butObject = init_button("butObject", 130, 65)
        butObject.clicked.connect(self.close)
        butTrek = init_button("butTrek", 130, 65)
        butTrek.clicked.connect(self.close)

        # Создание виджета выходных данных пользователя
        outlog = QLabel()
        outlog.setStyleSheet("border-radius: 10;background-color: white;")
        outlog.setAlignment(Qt.AlignmentFlag(1))
        outlog.setFont(QFont('Arial', 15))
        curOutput = outlog.text()
        outlog.setText(curOutput + '\n 123')

        # Создание виджета карт Yandex
        yaMap = QWebEngineView()
        yaMap.setHtml(open("yaMap.html").read())

        # Создание структурных слоёв приложения
        layoutMain = QHBoxLayout()
        layoutSTLeft = QVBoxLayout()
        layoutSTRight = QVBoxLayout()

        layoutSTLeftUp = QHBoxLayout()
        layoutSTLeftDown = QHBoxLayout()
        layoutSTRightUp = QHBoxLayout()
        layoutSTRightDown = QHBoxLayout()
        
        # Добавление первого ряда кнопок на слой
        layoutSTLeftUp.addWidget(butNew)
        layoutSTLeftUp.addWidget(butSave)
        layoutSTLeftUp.addWidget(butFile)
        layoutSTLeftUp.addWidget(butSett)
        layoutSTLeftUp.addStretch(1)

        # Добавление второго ряда кнопок на слой
        layoutSTRightUp.addWidget(butPoint)
        layoutSTRightUp.addWidget(butObject)
        layoutSTRightUp.addWidget(butTrek)

        # Добавление карты и выходных логов пользователя
        layoutSTLeftDown.addWidget(yaMap,3)
        layoutSTRightDown.addWidget(outlog,1)

        # Распределение столбцов по опорным слоям
        layoutSTLeft.addLayout(layoutSTLeftUp)
        layoutSTLeft.addLayout(layoutSTLeftDown)
        layoutSTRight.addLayout(layoutSTRightUp)
        layoutSTRight.addLayout(layoutSTRightDown)

        # Настройка отношения размеров слоёв
        layoutMain.addLayout(layoutSTLeft,3)
        layoutMain.addLayout(layoutSTRight,1)
        
        # Настройка главного слоя
        layoutMain.setSpacing(10)
        layoutMain.setContentsMargins(28, 28, 28, 28)

        # Добавление общего виджета и вывод его на экран
        widget = QWidget()
        widget.setLayout(layoutMain)
        self.setCentralWidget(widget)


if __name__ == '__main__':
    main()