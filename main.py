import sys
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtWebEngineWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle('Пример загрузки локальной веб-страницы')
        self.setGeometry(5,30,1355,730)
        self.browser=QWebEngineView()
        
        # # Загрузить внешний веб-интерфейс
        # url=r'index.html'
        # self.browser.load(QUrl(url))

        self.browser.setHtml('''<!DOCTYPE html>
                                <html>
                                    <head>

                                        <script src="https://api-maps.yandex.ru/2.1/?lang=ru-RU" type="text/javascript"></script>

                                    </head>
                                    <body>
                                        
                                        <div id="myMap" style="width: 700px; height: 700px;"></div>

                                        <script>
                                            ymaps.ready(init);
                                            function init(){
                                                var myMap = new ymaps.Map ('myMap', {
                                                    center: [59.850286, 30.237357],
                                                    zoom: 16,
                                                    type: 'yandex#satellite'
                                                });
                                            }

                                        </script>

                                    </body>
                                </html>''')
        self.setCentralWidget(self.browser)

if __name__ == '__main__':
    app=QApplication(sys.argv)
    win=MainWindow()
    win.show()
    app.exit(app.exec())