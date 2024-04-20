import sys
import os
import logging

from datetime import datetime
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtWebEngineWidgets import *
from PyQt6.QtWebChannel import QWebChannel

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
    markerCoordinatesChanged = pyqtSignal(float, float)

    # Слот для получения координат маркера из JavaScript
    @pyqtSlot(float, float)
    def receiveMarkerCoordinates(self, lat, lng):
        # Отправляем сигнал с координатами маркера
        self.markerCoordinatesChanged.emit(lat, lng)

class MainWindow(QMainWindow):

    # Слот для обработки полученных координат маркера
    def handleMarkerCoordinatesChanged(self, lat, lng):
        print(f"Received marker coordinates: Lat={lat}, Lng={lng}")
        
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
        self.backend.markerCoordinatesChanged.connect(self.handleMarkerCoordinatesChanged) # Подключаем сигнал от backend к слоту в MainWindow
                
        # map_int = QWebEngineView()
        # map_int.load(QUrl.fromLocalFile(os.path.abspath('map/map.html')))
        # map_int.setHtml(open("templates/map.html").read())
        # map_int.load(QUrl('http://127.0.0.1:5000/'))

        # Настройки главного окна
        self.setWindowTitle('Генератор полётных заданий')
        self.setGeometry(50, 50, 1200, 900)
        self.setMinimumSize(960, 920)
        
        # Создание виджета выходных данных пользователя
        outlog = QLabel()
        outlog.setStyleSheet("border-radius: 10;background-color: white;")
        outlog.setAlignment(Qt.AlignmentFlag(1))
        outlog.setFont(QFont('Arial', 15))
        outlog.setText("\n")

        # Создание и настройка кнопок
        butNew = init_button("butNew", 65, 65)
        butNew.pressed.connect(lambda: log("Has detected event click button butNew", outlog))
        butSave = init_button("butSave", 65, 65)
        butSave.clicked.connect(lambda: log("Has detected event click button butSave", outlog))
        butFile = init_button("butFile", 65, 65)
        butFile.clicked.connect(lambda: log("Has detected event click button butFile", outlog))
        butSett = init_button("butSett", 65, 65)
        butSett.clicked.connect(lambda: log("Has detected event click button butSett", outlog))
        butPoint = init_button("butPoint", 130, 65)
        butPoint.clicked.connect(lambda: log("Has detected event click button butPoint", outlog))
        butObject = init_button("butObject", 130, 65)
        butObject.clicked.connect(lambda: log("Has detected event click button butObject", outlog))
        butTrek = init_button("butTrek", 130, 65)
        butTrek.clicked.connect(lambda: log("Has detected event click button butTrek", outlog))

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

# Логирование + запись в область output
def log(mess, outlog):
    logger.info(mess)
    curOutput = outlog.text()
    date = datetime.now()
    outlog.setText(curOutput+" ["+"%s:"%date.hour+"%s:"%date.minute+"%s "%date.second+"%s."%date.day+"%s."%date.month+"%s"%date.year+"]"+"\n")
    curOutput = outlog.text()
    outlog.setText(curOutput+" " + mess + "\n\n")

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