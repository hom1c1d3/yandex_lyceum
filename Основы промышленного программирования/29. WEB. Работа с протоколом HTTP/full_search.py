import sys
from io import BytesIO
# Этот класс поможет нам сделать картинку из потока байт

import requests
from PIL import Image


# Пусть наше приложение предполагает запуск:
# python search.py Москва, ул. Ак. Королева, 12
# Тогда запрос к геокодеру формируется следующим образом:


def get_geocode_result(geocode_data):
    geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"

    geocoder_params = {
        "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
        "geocode": geocode_data,
        "format": "json"}

    response = requests.get(geocoder_api_server, params=geocoder_params)

    if not response:
        # обработка ошибочной ситуации
        pass

    # Преобразуем ответ в json-объект
    json_response = response.json()

    return json_response


def get_ll_from_geocode_response(geocode_result):
    # Получаем первый топоним из ответа геокодера.
    toponym = geocode_result["response"]["GeoObjectCollection"][
        "featureMember"][0]["GeoObject"]
    # Координаты центра топонима:
    toponym_coodrinates = toponym["Point"]["pos"]
    # Долгота и широта:
    toponym_longitude, toponym_lattitude = toponym_coodrinates.split(" ")
    return toponym_longitude, toponym_lattitude


def get_address_span(geocode_result):
    toponym = geocode_result["response"]["GeoObjectCollection"][
        "featureMember"][0]["GeoObject"]
    envelope = toponym['boundedBy']['Envelope']
    left, bottom = envelope["lowerCorner"].split(" ")
    right, top = envelope["upperCorner"].split(" ")
    dx = abs(float(left) - float(right)) / 2.0
    dy = abs(float(top) - float(bottom)) / 2.0
    return round(dx, 5), round(dy, 5)


def get_static_map(lat, lon, span):
    # Собираем параметры для запроса к StaticMapsAPI:
    span = ','.join(map(str, span))
    map_params = {
        "ll": ",".join([lat, lon]),
        "spn": span,
        "l": "map"
    }
    map_api_server = "http://static-maps.yandex.ru/1.x/"
    # ... и выполняем запрос
    response = requests.get(map_api_server, params=map_params)
    return response.content


def main():
    toponym_to_find = " ".join(sys.argv[1:])
    geocode_res = get_geocode_result(toponym_to_find)
    lat, lon = get_ll_from_geocode_response(geocode_res)
    span = get_address_span(geocode_res)
    image_raw = get_static_map(lat, lon, span)
    Image.open(BytesIO(
        image_raw)).show()


if __name__ == '__main__':
    main()