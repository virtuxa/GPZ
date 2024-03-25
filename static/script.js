// Дождёмся загрузки API и готовности DOM.
ymaps.ready(init);

var map;
var coordsStart;
var coordsEnd;
var condition = 1;

function init () {

    // Создание экземпляра карты и его привязка к контейнеру с тегом map
    map = new ymaps.Map('map', {
        center: [59.850286, 30.237357],
        zoom: 16,
        type: 'yandex#satellite',
        behaviors: [
            'scrollZoom',
            'drag'],
        controls: [
            'zoomControl',
            'searchControl',
        ],
    },{
        searchControlProvider: 'yandex#search'
    }),

    // Получение координат по клику мыши
    map.events.add('click', function(e){
        switch (condition){
            case 0:
                coordsEnd = e.get('coords');
                console.log(coordsEnd);
                addEnd(coordsEnd); // Добавление конечной метки
                postCoords(coordsEnd) // Отправка координат в Python
                console.log(condition);
                condition=2;
                break;
            case 1:
                coordsStart = e.get('coords');
                console.log(coordsStart);
                addStart(coordsStart); // Добавление стартовой метки
                postCoords(coordsStart) // Отправка координат в Python
                console.log(condition);
                condition-=1;
                break;
        }
    })

    // Отправка координат в Python
    function postCoords(coords){
        fetch('/getCoords', {
            // Specify the method
            method: 'POST',

            // JSON
            headers: {
                'Content-Type': 'application/json'
            },

            // A JSON payload
            body: JSON.stringify({
                coords
            })
        }).then(function (response) { // At this point, Flask has printed our JSON
            return response.text();
            }).then(function (text) {

            console.log('POST response: ');

            // Should be 'OK' if everything was successful
            console.log(text);
        });
    }

    // Создание начальной и конечной точки
    var placemarkStart = new ymaps.Placemark([59.850599, 30.237689], null,{
        preset: 'islands#darkOrangeCircleDotIcon'
    });

    var placemarkEnd = new ymaps.Placemark([59.850286, 30.237357], null,{
        preset: 'islands#pinkCircleDotIcon'
    });

    // Функции добавления точек
    function addStart(coordsStart){
        map.geoObjects.add(placemarkStart);
        placemarkStart.geometry.setCoordinates([coordsStart[0], coordsStart[1]])
    }

    function addEnd(coordsEnd){
        map.geoObjects.add(placemarkEnd);
        placemarkEnd.geometry.setCoordinates([coordsEnd[0], coordsEnd[1]])

        // Добавление линии на карту
        map.geoObjects
        .add(startToEndLine);
    }
    
    // Создание обьекта PolyLine
    var startToEndLine = new ymaps.Polyline([
        // Вершины
        placemarkStart.geometry.getCoordinates(),
        placemarkEnd.geometry.getCoordinates(),
    ], {
        // Содержимое балуна.
        balloonContent: "Генеральный маршрут"
    }, {
        balloonCloseButton: true,
        strokeColor: "#f23f42",
        strokeWidth: 4,
        strokeOpacity: 0.8
    });

    // Следим за изменением координат точек и подгоняем линию
    placemarkStart.geometry.events.add('change', function(e) {
        startToEndLine.geometry.set(0, coordsStart);
    });
    placemarkEnd.geometry.events.add('change', function(e) {
        startToEndLine.geometry.set(1, coordsEnd);
    });
}