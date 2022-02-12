import requests


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


def main():
    user_data = input('Введите адрес: ')
    point = get_ll_from_geocode_response(get_toponym(get_geocode_result(user_data)))
    nearest_metro = get_toponym(get_geocode_result(','.join(point), kind='metro'))
    print("Ближайщее метро:", nearest_metro['name'], "с координатами", nearest_metro['Point']['pos'])


if __name__ == '__main__':
    main()