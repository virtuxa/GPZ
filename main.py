import sys

from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtWebEngineWidgets import *

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
        self.setWindowTitle('TEST_TEST_TEST')
        self.setGeometry(50, 50, 1200, 900)
        self.setMinimumSize(960, 920)

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

        # Создание 3-ех слоев
        lay_1 = QHBoxLayout()
        leftST = QVBoxLayout()
        rightST = QVBoxLayout()

        lay_4 = QHBoxLayout()
        lay_4.addWidget(Color('orange'))
        lay_5 = QHBoxLayout()
        lay_5.addWidget(Color('yellow'))
        lay_6 = QHBoxLayout()
        lay_6.addWidget(Color('blue'))
        lay_7 = QHBoxLayout()
        lay_7.addWidget(Color('purple'))

        lay_4.addWidget(butSave,1)
        lay_4.addWidget(butFile,1)

        leftST.addLayout(lay_4)
        leftST.addLayout(lay_5)
        rightST.addLayout(lay_6)
        rightST.addLayout(lay_7)

        lay_1.addLayout(leftST,2)
        lay_1.addLayout(rightST,1)

        # Добавление общего виджета и вывод его на экран
        widget = QWidget()
        widget.setLayout(lay_1)
        self.setCentralWidget(widget)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()