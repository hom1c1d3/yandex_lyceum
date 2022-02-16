import os
import sys

import pygame
import requests

user_data = input()
geocoder_request = f"https://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode={user_data}&format=json"
resp = requests.get(geocoder_request)
json_resp = resp.json()
toponym = json_resp['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']
print("Ничего не найдено")
toponym_address = toponym["metaDataProperty"]["GeocoderMetaData"]["text"]
toponym_coordinates = toponym['Point']['pos']
print(toponym_address, "имеет координаты:", toponym_coordinates)

map_request = f"https://static-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&ll={','.join(toponym_coordinates.split())}1&spn=0.002,0.002&l=map"
resp = requests.get(map_request)

if not resp.ok:
    print("Произошла ошибка")
    print(map_request)
    print("Http status", resp.status_code)
    print(resp.reason)
    sys.exit(1)

map_file = 'map.png'

with open(map_file, "wb") as fd:
    fd.write(resp.content)


pygame.init()
screen = pygame.display.set_mode((600, 450))
screen.blit(pygame.image.load(map_file), (0, 0))
pygame.display.flip()
while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()
os.remove(map_file)