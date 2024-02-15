import sys
import logging

from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtWebEngineWidgets import *
from PyQt6.QtWidgets import QTextEdit

logger = logging.getLogger("module.app")

# Запускаем работу приложения
def main():
    logger.info("Start loading app module")
    app=QApplication(sys.argv)
    win=MainWindow()
    win.show()
    app.exit(app.exec())

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

        self.setWindowTitle('GPZ')
        self.setGeometry(50,50,1200,900)
        self.setMinimumSize(900,900)

        yaMap = QWebEngineView()
        yaMap.setHtml(open("yaMap.html").read())

        layout1 = QHBoxLayout()
        layout2 = QVBoxLayout()
        layout3 = QHBoxLayout()

        layout1.addWidget(QPushButton("123"))
        layout1.addWidget(QPushButton("123"))
        layout1.addWidget(QPushButton("123"))

        layout2.addLayout( layout1 )

        text = QTextEdit()
        text.setGeometry(1500,1500,1500,1500)
        text.setPlaceholderText("123")

        layout3.addWidget(yaMap)
        layout3.addWidget(text)

        layout2.addLayout( layout3 )
        layout2.setSpacing(10)
        layout2.setContentsMargins(28,28,28,28)

        widget = QWidget()
        widget.setLayout(layout2)
        self.setCentralWidget(widget)


if __name__ == '__main__':
    main()