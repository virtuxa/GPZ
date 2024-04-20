// Добавление карты
var map = L.map('map',{
    zoom: 12,
    min_zoom: 12,
    max_zoom: 16,
}).setView([59.946991,30.237421]);

// Добавление двух слоёв (vector и satellite)
L.tileLayer('G:/System/YandexIgnore/Личные документы/Проекты/НПП Радар/GPZ/map/vector/{z}/{x}/{y}.png', {
    attribution: 'vector',
    min_zoom: 12,
    max_zoom: 13,
    minNativeZoom: 10,
    maxNativeZoom: 13
}).addTo(map);
L.tileLayer('G:/System/YandexIgnore/Личные документы/Проекты/НПП Радар/GPZ/map/satellite/{z}/{x}/{y}.png', {
    attribution: 'satellite',
    min_zoom: 14,
    max_zoom: 16,
    minNativeZoom: 10,
    maxNativeZoom: 16
}).addTo(map);

/* НАСТРОЙКА КАРТЫ */
L.control.mousePosition().addTo(map); // Отображение координат на карте
L.control.scale().addTo(map); // Отображение высоты на карте
map.attributionControl.setPrefix('<img src="../map/assets/flag.png" height="14px" width="14px">'); // Смена аттрибутов на карте
map.doubleClickZoom.disable(); // Отключение приближения при двойном клике

/* Отображение обьектов на карте */
// Инициализация необходимых переменных
var markers = []; // Переменная для хранения маркеров
var markers_data = []; // Переменная для отправки данных в приложение
var lines = []; // Переменная для хранения линий

// Зададим настройки обьектов
var wayPointIcon = L.icon({ // Настройка иконки маркера
    iconUrl: '../map/assets/wayPoint.png', // URL картинки
    iconSize: [36, 40], // Размеры картинки в пикселях
    iconAnchor: [18, 40], // Точка, которая будет соответствовать точке на земле (относительно величины картинки)
    popupAnchor: [0, -20] // Точка относительно iconAnchor, где будет открываться всплывающее окно (X, Y)
});
var lineOptions = { // Настройка линии
    color: 'purple',
    weight: 3,
};
var arrowheadsOptions = { // Настройка стрелки
    frequency: 2,
    size: '15px',
}
var markerOptions = { // Настройка маркеров
    draggable: true,
    icon: wayPointIcon
}

// Зададим настройки QWebChannel
new QWebChannel(qt.webChannelTransport, function (channel) {
    window.backend = channel.objects.backend;
});

// Функция для добавления маркеров и соединения их линиями
function addMarkerAndConnect(e) {
    var marker = L.marker(e.latlng, markerOptions).addTo(map);
    marker.bindPopup(e.latlng.toString()).openPopup(); // Отображение координат во всплывающем окне маркера
    markers.push(marker);
    
    if (markers.length > 1) {
        var prevMarker = markers[markers.length - 2].getLatLng();
        var currentMarker = marker.getLatLng();
        var line = L.polyline([prevMarker, currentMarker], lineOptions).arrowheads(arrowheadsOptions).addTo(map);
        lines.push(line);
    }

    var index = markers.indexOf(marker);

    markers_data.push([index, e.latlng.lat, e.latlng.lng]) // Собираем все данные в массив
    backend.receiveMarkerCoordinates(markers_data); // Отправляем данные в приложение
        
    marker.on('move', updateLines); // Обновление линий при перемещении маркера
    marker.on('dblclick', deleteLastMarker); // Удаление маркера при двойном клике
    marker.on('dragend', updateMarkerCoordinates); // Обновление данных при перемещении маркера
}
// Функция для обновления позиции линий при перемещении маркера
function updateLines(e) {
    var markerIndex = markers.indexOf(e.target);
    if (markerIndex > -1) {
        if (markerIndex > 0) {
            var prevMarker = markers[markerIndex - 1].getLatLng();
            var currentMarker = e.target.getLatLng();
            lines[markerIndex - 1].setLatLngs([prevMarker, currentMarker]);
        }
        if (markerIndex < markers.length - 1) {
            var nextMarker = markers[markerIndex + 1].getLatLng();
            var currentMarker = e.target.getLatLng();
            lines[markerIndex].setLatLngs([currentMarker, nextMarker]);
        }
    }
}
// Функция для удаления последнего маркера
function deleteLastMarker() {
    try {
        if (markers.length > 0) {
            var lastMarker = markers.pop(); // Удаление последнего маркера из массива
            var lastLine = lines.pop(); // Удаление последней линии из массива
            map.removeLayer(lastMarker); // Удаление маркера с карты
            map.removeLayer(lastLine); // Удаление линии с карты
    
            markers_data.pop();
            backend.receiveMarkerCoordinates(markers_data); // Отправляем данные в приложение
        }
    } catch (err) {
        markers_data = [];
        backend.receiveMarkerCoordinates(markers_data); // Отправляем данные в приложение
    }
}
// Функция обновления координат маркера при перемещении маркера
function updateMarkerCoordinates(event) {
    var marker = event.target;
    var position = marker.getLatLng();
    var lat = position.lat;
    var lng = position.lng;
    var index = markers.indexOf(marker);
    markers_data[index] = ([index, lat, lng]) // Собираем все данные в массив

    backend.receiveMarkerCoordinates(markers_data); // Отправляем данные в приложение
}

// Обработчик события клика по карте
map.on('click', addMarkerAndConnect);