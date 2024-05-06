import sys
import os
import logging

from datetime import datetime
from PyQt6 import QtCore
from PyQt6.QtWebChannel import QWebChannel
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtWebEngineWidgets import *

logger = logging.getLogger("module.app")
backgroundMainColor = '#e8e8e8'

# Запускаем работу приложения
def main():
    app = QApplication(sys.argv)
    app.setStyleSheet("MainWindow{background-color: %s;}"%backgroundMainColor)
    win = MainWindow()
    win.show()
    app.exit(app.exec())

class Backend(QObject):
    # Сигнал для передачи координат маркера
    markerCoordinatesChanged = pyqtSignal(list)

    # Слот для получения координат маркера из JavaScript
    @pyqtSlot(list)
    def receiveMarkerCoordinates(self, markers):
        # Отправляем сигнал с координатами маркера
        self.markerCoordinatesChanged.emit(markers)
    
    # Слот для обновления координат маркера после перемещения
    @pyqtSlot(list)
    def updateMarkerCoordinates(self, markers):
        # Отправляем сигнал с координатами маркера
        self.markerCoordinatesChanged.emit(markers)

class MainWindow(QMainWindow):

    # Слот для обработки полученных координат маркера
    def handleMarkerCoordinatesChanged(self, markers):
        date = datetime.now()
        curOutput = ""
        if (len(markers)==0):
            self.outlog.setText("")
        
        for i in range(len(markers)):
            self.outlog.setText(curOutput+f"{i+1} ["+"%s:"%date.hour+"%s:"%date.minute+"%s "%date.second+"%s."%date.day+"%s."%date.month+"%s"%date.year+"]"+'<br>'+f'<a href="{markers[i][1]}, {markers[i][2]}">Lat: {round(markers[i][1],5)}, Lng: {round(markers[i][2],5)}</a>'+'<br><br>')
            curOutput = self.outlog.text()

    # Слот для обновления координат при перемещении маркера
    def updateMarkerCoordinatesChanged(self, markers):
        pass

    # Слот для обработки нажатия на ссылку в QLabel
    def handleLabelClick(self, link):
        lat, lng = map(float, link.split(','))
        self.map_int.page().runJavaScript(f"map.setView([{lat}, {lng}], 15)")
        
    def __init__(self):
        super(MainWindow, self).__init__()

        # Инициализируем html, а также создаём связь с js для обмена данными
        self.map_int = QWebEngineView() # Создаем экземпляр QWebEngineView
        # Создаем объекты канала веб-канала
        self.channel = QWebChannel()
        self.backend = Backend()
        self.channel.registerObject('backend', self.backend) # Регистрируем объекты канала веб-канала
        self.map_int.page().setWebChannel(self.channel) # Устанавливаем канал для QWebEngineView
        # Загружаем HTML-файл в QWebEngineView
        file_path = os.path.abspath('map/map.html')
        self.map_int.load(QUrl.fromLocalFile(file_path))
                
        # map_int = QWebEngineView()
        # map_int.load(QUrl.fromLocalFile(os.path.abspath('map/map.html')))
        # map_int.setHtml(open("templates/map.html").read())
        # map_int.load(QUrl('http://127.0.0.1:5000/'))

        # Настройки главного окна
        self.setWindowTitle('Генератор полётных заданий')
        self.setGeometry(50, 50, 1200, 900)
        self.setMinimumSize(500, 500)
        
        # Создание виджета выходных данных пользователя
        self.outlog = QLabel()
        self.outlog.setStyleSheet("border-radius: 10;background-color: white;")
        self.outlog.setAlignment(Qt.AlignmentFlag(1))
        self.outlog.setFont(QFont('Arial', 15))
        self.outlog.setText("\n")
        # Добавим возможность прокрутки при переполнении выходных данных
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(self.outlog)
        
        # Устанавливаем обработчик событий нажатия на QLabel
        self.outlog.linkActivated.connect(self.handleLabelClick)
        # Подключаем обработчик событий для QLabel
        self.backend.markerCoordinatesChanged.connect(self.handleMarkerCoordinatesChanged)

        # Создание и настройка кнопок
        butNew = init_button("butNew", 65, 65)
        butNew.pressed.connect(lambda: log("Has detected event click button butNew", self.outlog))
        butSave = init_button("butSave", 65, 65)
        butSave.clicked.connect(lambda: log("Has detected event click button butSave", self.outlog))
        butFile = init_button("butFile", 65, 65)
        butFile.clicked.connect(lambda: log("Has detected event click button butFile", self.outlog))
        butSett = init_button("butSett", 65, 65)
        butSett.clicked.connect(lambda: log("Has detected event click button butSett", self.outlog))
        butPoint = init_button("butPoint", 130, 65)
        butPoint.clicked.connect(lambda: log("Has detected event click button butPoint", self.outlog))
        butObject = init_button("butObject", 130, 65)
        butObject.clicked.connect(lambda: log("Has detected event click button butObject", self.outlog))
        butTrek = init_button("butTrek", 130, 65)
        butTrek.clicked.connect(lambda: log("Has detected event click button butTrek", self.outlog))

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
        layoutSTLeftDown.addWidget(self.map_int,3)
        layoutSTRightDown.addWidget(scroll_area,1)

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

# Логирование + запись в область output
def log(mess, outlog):
    logger.info(mess)
    curOutput = outlog.text()
    date = datetime.now()
    outlog.setText(curOutput+" ["+"%s:"%date.hour+"%s:"%date.minute+"%s "%date.second+"%s."%date.day+"%s."%date.month+"%s"%date.year+"]"+"\n "+mess+";"+"\n\n")

    return outlog

# Конструктор кнопок 
def init_button(nameIcon, sizeX, sizeY):
    button = QPushButton()
    button.setIcon(QIcon('assets/icons/%s.png'%nameIcon))
    button.setIconSize(QSize(sizeX, sizeY))
    button.setStyleSheet('border-radius: 50;background-color: %s;'%backgroundMainColor)

    return button

if __name__ == '__main__':
    main()