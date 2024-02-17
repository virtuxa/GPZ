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
    app.setStyleSheet("MainWindow{background-color: #e8e8e8;}") #D9D9D9
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
        yaMap.setStyleSheet('border-radius: 5;background-color: #e8e8e8;')

        # Создание и настройка кнопок функционального меню
        butNew = QPushButton("")
        butNew.setIcon(QIcon('icons/butNew.png'))
        butNew.setIconSize(QSize(65, 65))
        butNew.clicked.connect(self.close)
        butNew.setStyleSheet('border-radius: 50;background-color: #e8e8e8;')

        butSave = QPushButton("")
        butSave.setIcon(QIcon('icons/butSave.png'))
        butSave.setIconSize(QSize(65, 65))
        butSave.clicked.connect(self.close)
        butSave.setStyleSheet('border-radius: 50;background-color: #e8e8e8;')

        butFile = QPushButton("")
        butFile.setIcon(QIcon('icons/butFile.png'))
        butFile.setIconSize(QSize(65, 65))
        butFile.clicked.connect(self.close)
        butFile.setStyleSheet('border-radius: 50;background-color: #e8e8e8;')

        butSett = QPushButton("")
        butSett.setIcon(QIcon('icons/butSett.png'))
        butSett.setIconSize(QSize(65, 65))
        butSett.clicked.connect(self.close)
        butSett.setStyleSheet('border-radius: 50;background-color: #e8e8e8;')

        butPoin = QPushButton("")
        butPoin.setIcon(QIcon('icons/butPoint.png'))
        butPoin.setIconSize(QSize(130, 65))
        butPoin.clicked.connect(self.close)
        butPoin.setStyleSheet('border-radius: 50;background-color: #e8e8e8;')

        butObje = QPushButton("")
        butObje.setIcon(QIcon('icons/butObject.png'))
        butObje.setIconSize(QSize(130, 65))
        butObje.clicked.connect(self.close)
        butObje.setStyleSheet('border-radius: 50;background-color: #e8e8e8;')

        butTrek = QPushButton("")
        butTrek.setIcon(QIcon('icons/butTrek.png'))
        butTrek.setIconSize(QSize(130, 65))
        butTrek.clicked.connect(self.close)
        butTrek.setStyleSheet('border-radius: 50;background-color: #e8e8e8;')

        # Создание выходных данных для пользователя
        outlog = QLabel()
        outlog.setStyleSheet("border-radius: 10;background-color: white;")
        outlog.setAlignment(Qt.AlignmentFlag(1))
        outlog.setFont(QFont('Arial', 15))
        curOutput = outlog.text()
        outlog.setText(curOutput + '\n 123')

        # Создание структурных слоёв приложения
        layoutMain = QHBoxLayout()
        layoutSTLeft = QVBoxLayout()
        layoutSTRight = QVBoxLayout()

        layoutSTLeftUp = QHBoxLayout()
        layoutSTLeftDown = QHBoxLayout()
        layoutSTRightUp = QHBoxLayout()
        layoutSTRightDown = QHBoxLayout()
        
        # Добавление кнопок
        layoutSTLeftUp.addWidget(butNew)
        layoutSTLeftUp.addWidget(butSave)
        layoutSTLeftUp.addWidget(butFile)
        layoutSTLeftUp.addWidget(butSett)
        layoutSTLeftUp.addStretch(1)

        layoutSTRightUp.addWidget(butPoin)
        layoutSTRightUp.addWidget(butObje)
        layoutSTRightUp.addWidget(butTrek)

        layoutSTLeftDown.addWidget(yaMap,3)
        layoutSTRightDown.addWidget(outlog,1)

        layoutSTLeft.addLayout(layoutSTLeftUp)
        layoutSTLeft.addLayout(layoutSTLeftDown)
        layoutSTRight.addLayout(layoutSTRightUp)
        layoutSTRight.addLayout(layoutSTRightDown)

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