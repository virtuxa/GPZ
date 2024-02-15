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
    app=QApplication(sys.argv)
    win=MainWindow()
    win.show()
    app.exit(app.exec())

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle('GPZ')
        self.setGeometry(50,50,1116,851)
        self.setMinimumSize(900,900)

        view = QWebEngineView()
        view.setHtml(open("yaMap.html").read())

        self.setCentralWidget(view)


if __name__ == '__main__':
    main()