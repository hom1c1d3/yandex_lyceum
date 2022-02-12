import math

import requests


# Определяем функцию, считающую расстояние между двумя точками, заданными координатами
def lonlat_distance(a, b):
    degree_to_meters_factor = 111 * 1000  # 111 километров в метрах
    a_lon, a_lat = a
    b_lon, b_lat = b

    # Берем среднюю по широте точку и считаем коэффициент для нее.
    radians_lattitude = math.radians((a_lat + b_lat) / 2.)
    lat_lon_factor = math.cos(radians_lattitude)

    # Вычисляем смещения в метрах по вертикали и горизонтали.
    dx = abs(a_lon - b_lon) * degree_to_meters_factor * lat_lon_factor
    dy = abs(a_lat - b_lat) * degree_to_meters_factor

    # Вычисляем расстояние между точками.
    distance = math.sqrt(dx * dx + dy * dy)

    return distance


def get_request_result(data):
    geocoder_request = f"https://geocode-maps.yandex.ru/" \
                       f"1.x/" \
                       f"?apikey=40d1649f-0493-4b70-98ba-98533de7710b" \
                       f"&geocode={data}&format=json"
    resp = requests.get(geocoder_request)

    if resp.ok:
        json_resp = resp.json()
        try:
            toponym = json_resp['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']
        except (KeyError, IndexError):
            raise ValueError("Ничего не найдено")
        else:
            toponym_address = toponym["metaDataProperty"]["GeocoderMetaData"]["text"]
            toponym_coordinates = toponym['Point']['pos'].split()
            toponym_coordinates = float(toponym_coordinates[0]), float(toponym_coordinates[1])
            return toponym_address, toponym_coordinates
    else:
        raise ValueError(f"Произошла ошибка\n"
                         f"{geocoder_request}\n"
                         f"Http status {resp.status_code}\n"
                         f"{resp.reason}")


def get_receiver_height(distance, sender_height):
    receiver_height = (distance / 3.6 - math.sqrt(sender_height))
    return receiver_height ** 2 if receiver_height > 0 else 0


def main():
    sender_tower = get_request_result('ул. Академика Королёва, 15, корп. 1')
    sender_height = 525
    user_data = input('Введите адрес: ').strip()
    receiver = get_request_result(user_data)

    distance = lonlat_distance(sender_tower[1], receiver[1])

    receiver_height = get_receiver_height(distance / 1000, sender_height)
    print(f"Вы должны поставить антенну на высоту: {receiver_height}")


if __name__ == '__main__':
    main()