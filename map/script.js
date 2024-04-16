// Добавление карты
var map = L.map('map',{
    zoom: 12,
    min_zoom: 12,
    max_zoom: 16,
}).setView([59.946991,30.237421]);

// Добавление базового слоя
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

// Печать координат в консоль на ПКМ
map.on("contextmenu", function (event) {
    console.log("Coordinates: " + event.latlng.toString());
    console.log(map.getZoom())
});