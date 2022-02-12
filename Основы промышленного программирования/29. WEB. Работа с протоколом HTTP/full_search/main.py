import sys
from io import BytesIO
# Этот класс поможет нам сделать картинку из потока байт

import requests
from PIL import Image

from utils import get_address_span


# Пусть наше приложение предполагает запуск:
# python search.py Москва, ул. Ак. Королева, 12
# Тогда запрос к геокодеру формируется следующим образом:


def get_geocode_result(geocode_data, **params):
    geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"

    geocoder_params = {
        "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
        "geocode": geocode_data,
        "format": "json",
        **params
    }

    response = requests.get(geocoder_api_server, params=geocoder_params)

    if not response:
        # обработка ошибочной ситуации
        pass

    # Преобразуем ответ в json-объект
    json_response = response.json()

    return json_response


def get_toponym(geocode_result):
    # Получаем первый топоним из ответа геокодера.
    try:
        toponym = geocode_result["response"]["GeoObjectCollection"][
            "featureMember"][0]["GeoObject"]
    except (KeyError, IndexError):
        raise ValueError
    return toponym


def get_ll_from_geocode_response(toponym):
    # Координаты центра топонима:
    toponym_coodrinates = toponym["Point"]["pos"]
    # Долгота и широта:
    toponym_longitude, toponym_lattitude = toponym_coodrinates.split(" ")
    return toponym_longitude, toponym_lattitude


def get_static_map(lat, lon, **params):
    # Собираем параметры для запроса к StaticMapsAPI:
    map_type = params.get('l', 'map')
    map_params = {
        "ll": ",".join([lat, lon]),
        "l": map_type,
        **params,
    }
    map_api_server = "http://static-maps.yandex.ru/1.x/"
    # ... и выполняем запрос
    response = requests.get(map_api_server, params=map_params)
    return response.content


def main():
    toponym_to_find = " ".join(sys.argv[1:])
    geocode_res = get_geocode_result(toponym_to_find)
    try:
        toponym = get_toponym(geocode_res)
    except ValueError:
        print('Объект не найден')
        return 1
    lat, lon = get_ll_from_geocode_response(toponym)
    span = get_address_span(toponym)
    span = ','.join(map(str, span))
    pointer_style = 'pm2'
    pointer_color = 'org'
    pointer_size = 'l'
    pointer = f'{lat},{lon},{pointer_style}{pointer_color}{pointer_size}'
    image_raw = get_static_map(lat, lon, spn=span, pt=pointer)
    Image.open(BytesIO(
        image_raw)).show()


if __name__ == '__main__':
    main()