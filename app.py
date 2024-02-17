import sys
import logging

from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtWebEngineWidgets import *

logger = logging.getLogger("module.app")

# Запускаем работу приложения
def main():
    logger.info("Start loading app module")
    app = QApplication(sys.argv)
    app.setStyleSheet("MainWindow{background-color: #D9D9D9;}")
    win = MainWindow()
    win.show()
    app.exit(app.exec())

    # Темная тема
    # logger.info("Start loading app module")
    # sys.argv += ['-platform', 'windows:darkmode=2']
    # app = QApplication(sys.argv)
    # app.setStyle('Fusion')
    # win = MainWindow()
    # win.show()
    # app.exit(app.exec())

class Color(QWidget):

    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Настройки главного окна
        self.setWindowTitle('Генератор полётных заданий')
        self.setGeometry(50, 50, 1200, 900)
        self.setMinimumSize(960, 920)

        yaMap = QWebEngineView()
        yaMap.setHtml(open("yaMap.html").read())

        # Создание и настройка кнопок функционального меню
        butNew = QPushButton("")
        butNew.setIcon(QIcon('icons/butNew.png'))
        butNew.setIconSize(QSize(65, 65))
        butNew.clicked.connect(self.close)
        butNew.setStyleSheet('border-radius: 50;background-color: #D9D9D9;')

        butSave = QPushButton("")
        butSave.setIcon(QIcon('icons/butSave.png'))
        butSave.setIconSize(QSize(65, 65))
        butSave.clicked.connect(self.close)
        butSave.setStyleSheet('border-radius: 50;background-color: #D9D9D9;')

        butFile = QPushButton("")
        butFile.setIcon(QIcon('icons/butFile.png'))
        butFile.setIconSize(QSize(65, 65))
        butFile.clicked.connect(self.close)
        butFile.setStyleSheet('border-radius: 50;background-color: #D9D9D9;')

        butSett = QPushButton("")
        butSett.setIcon(QIcon('icons/butSett.png'))
        butSett.setIconSize(QSize(65, 65))
        butSett.clicked.connect(self.close)
        butSett.setStyleSheet('border-radius: 50;background-color: #D9D9D9;')

        butPoin = QPushButton("")
        butPoin.setIcon(QIcon('icons/butPoint.png'))
        butPoin.setIconSize(QSize(130, 65))
        butPoin.clicked.connect(self.close)
        butPoin.setStyleSheet('border-radius: 50;background-color: #D9D9D9;')

        butObje = QPushButton("")
        butObje.setIcon(QIcon('icons/butObject.png'))
        butObje.setIconSize(QSize(130, 65))
        butObje.clicked.connect(self.close)
        butObje.setStyleSheet('border-radius: 50;background-color: #D9D9D9;')

        butTrek = QPushButton("")
        butTrek.setIcon(QIcon('icons/butTrek.png'))
        butTrek.setIconSize(QSize(130, 65))
        butTrek.clicked.connect(self.close)
        butTrek.setStyleSheet('border-radius: 50;background-color: #D9D9D9;')

        # Создание 3-ех слоев
        vertLayoutMain = QVBoxLayout()
        horLayout1 = QHBoxLayout()
        horLayout2 = QHBoxLayout()

        # Добавление кнопок на слой
        horLayout1.addWidget(butNew)
        horLayout1.addWidget(butSave)
        horLayout1.addWidget(butFile)
        horLayout1.addWidget(butSett)

        # Привязка кнопок к левой стороне
        horLayout1.addStretch(2)

        horLayout1.addWidget(butPoin)
        horLayout1.addWidget(butObje)
        horLayout1.addWidget(butTrek)

        vertLayoutMain.addLayout(horLayout1)

        outlog = QLabel('Click me', self)
        outlog.setStyleSheet("background-color: white;")
        outlog.setAlignment(Qt.AlignmentFlag(1))

        horLayout2.addWidget(yaMap,3)
        horLayout2.addWidget(outlog,1)

        vertLayoutMain.addLayout(horLayout2)
        vertLayoutMain.setSpacing(10)
        vertLayoutMain.setContentsMargins(28, 28, 28, 28)

        # Добавление общего виджета и вывод его на экран
        widget = QWidget()
        widget.setLayout(vertLayoutMain)
        self.setCentralWidget(widget)


if __name__ == '__main__':
    main()

# curOutput = outlog.text()
# outlog.setText(curOutput + '\n 123')