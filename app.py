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
        self.setWindowTitle('GPZ')
        self.setGeometry(50, 50, 1200, 900)
        self.setMinimumSize(960, 920)

        yaMap = QWebEngineView()
        yaMap.setHtml(open("yaMap.html").read())

        # Это кнопки
        butNew = QPushButton("")
        butNew.setFixedSize(60, 60)
        butNew.setIcon(QIcon('icons/butNew.png'))
        butNew.setIconSize(QSize(60, 60))
        butNew.clicked.connect(self.close)

        butSave = QPushButton("")
        butSave.setFixedSize(60, 60)
        butSave.setIcon(QIcon('icons/butSave.png'))
        butSave.setIconSize(QSize(60, 60))
        butSave.clicked.connect(self.close)

        butFile = QPushButton("")
        butFile.setFixedSize(60, 60)
        butFile.setIcon(QIcon('icons/butFile.png'))
        butFile.setIconSize(QSize(60, 60))
        butFile.clicked.connect(self.close)

        butSett = QPushButton("")
        butSett.setFixedSize(60, 60)
        butSett.setIcon(QIcon('icons/butSett.png'))
        butSett.setIconSize(QSize(60, 60))
        butSett.clicked.connect(self.close)

        butPoin = QPushButton("")
        butPoin.setFixedSize(60, 60)
        butPoin.setIcon(QIcon('icons/butPoin.png'))
        butPoin.setIconSize(QSize(60, 60))
        butPoin.clicked.connect(self.close)

        butObje = QPushButton("")
        butObje.setFixedSize(60, 60)
        butObje.setIcon(QIcon('icons/butObje.png'))
        butObje.setIconSize(QSize(60, 60))
        butObje.clicked.connect(self.close)

        butTrek = QPushButton("")
        butTrek.setFixedSize(60, 60)
        butTrek.setIcon(QIcon('icons/butTrek.png'))
        butTrek.setIconSize(QSize(60, 60))
        butTrek.clicked.connect(self.close)

        vertLayoutMain = QVBoxLayout()
        horLayout1 = QHBoxLayout()
        horLayout2 = QHBoxLayout()

        horLayout1.addWidget(butNew)
        horLayout1.addWidget(butSave)
        horLayout1.addWidget(butFile)
        horLayout1.addWidget(butSett)
        horLayout1.addWidget(butPoin)
        horLayout1.addWidget(butObje)
        horLayout1.addWidget(butTrek)

        horLayout1.addStretch()

        vertLayoutMain.addLayout(horLayout1)

        text = QTextEdit()
        text.setPlaceholderText("Текст текст")

        horLayout2.addWidget(yaMap)
        horLayout2.addWidget(text)

        vertLayoutMain.addLayout(horLayout2)
        vertLayoutMain.setSpacing(10)
        vertLayoutMain.setContentsMargins(28, 28, 28, 28)

        widget = QWidget()
        widget.setLayout(vertLayoutMain)
        self.setCentralWidget(widget)


if __name__ == '__main__':
    main()