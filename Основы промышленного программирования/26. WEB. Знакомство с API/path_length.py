import os
import sys

import pygame
import requests


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
            toponym_coordinates = toponym['Point']['pos']
            return toponym_address, toponym_coordinates
    else:
        raise ValueError(f"Произошла ошибка\n"
                         f"{geocoder_request}\n"
                         f"Http status {resp.status_code}\n"
                         f"{resp.reason}")


path = [(29.914783, 59.891574), (30.105881, 59.944074), (30.237944, 59.916487),
        (30.266268, 59.919073), (30.275489, 59.930952), (30.310165, 59.941203)]


def get_distance_between_points(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** .5


def get_mean_of_two_points(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    mean = (x1 + x2) / 2, (y1 + y2) / 2
    return mean


def get_polyline_center(coordinates):
    segments_center_lengths = []
    for seg in zip(coordinates, coordinates[1:]):
        length = get_distance_between_points(*seg)
        center = get_mean_of_two_points(*seg)
        segments_center_lengths.append((center, length))
    weights_sum = sum(lng for _, lng in segments_center_lengths)
    barycenter_x = sum(x * lng for ((x, _), lng) in segments_center_lengths) / weights_sum
    barycenter_y = sum(y * lng for ((_, y), lng) in segments_center_lengths) / weights_sum
    return barycenter_x, barycenter_y


back_map_coord = get_polyline_center(path)
path_center = path[int(len(path) // 2)]
str_path_center = f"{path_center[0]},{path_center[1]}"
path_length = sum(get_distance_between_points(*i) for i in zip(path, path[1:]))
str_back_map_coord = f"{back_map_coord[0]},{back_map_coord[1]}"

print(f"Длина пути: {path_length}")

str_path = [f"{a},{b}" for a, b in path]
line_type = 'pm2' + 'org' + 'l'
route_coordinates_map = ','.join(str_path)
map_request = f"http://static-maps.yandex.ru/1.x/" \
              f"?ll={str_back_map_coord}" \
              f"&z=9&l=map&pl={route_coordinates_map}&pt={str_path_center},pm2orgl"
response = requests.get(map_request)

if not response:
    print("Ошибка выполнения запроса:")
    print(map_request)
    print("Http статус:", response.status_code, "(", response.reason, ")")
    sys.exit(1)

# Запишем полученное изображение в файл.
map_file = "map.png"
with open(map_file, "wb") as file:
    file.write(response.content)

# Инициализируем pygame
pygame.init()
screen = pygame.display.set_mode((600, 450))
# Рисуем картинку, загружаемую из только что созданного файла.
back_map = pygame.image.load(map_file)
screen.blit(back_map, (0, 0))
# Переключаем экран и ждем закрытия окна.
pygame.display.flip()
while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()

# Удаляем за собой файл с изображением.
os.remove(map_file)
