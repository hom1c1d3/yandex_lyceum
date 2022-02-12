import os
import sys

import pygame
import requests

import requests

user_data = ['Волоколамское ш., 69',
             'Ленинградский просп., 36',
             'ул. Лужники, 24, стр. 1']


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


_, back_map_coord = get_request_result('Москва')
stadiums_coordinates = [get_request_result(i)[1] for i in user_data]
mark_type = 'pm2' + 'org' + 'l'
stadiums_coordinates_map = '~'.join(','.join(i.split()) + f',{mark_type}'
                                    for i in stadiums_coordinates)
map_request = f"http://static-maps.yandex.ru/1.x/" \
              f"?ll={','.join(back_map_coord.split())}&z=10&l=map&pt={stadiums_coordinates_map}"
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
