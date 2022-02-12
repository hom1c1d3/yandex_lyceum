import os
import sys

import pygame
import requests

coordinates = ['74.267956,45.719903', '-60.373348,-33.041010', '-77.682097,40.689158',
               '144.876359,43.563094']
map_request = "http://static-maps.yandex.ru/1.x/?ll={}&z=11&l=sat"


def get_resp(url):
    resp = requests.get(url)

    if not resp:
        print("Ошибка выполнения запроса:")
        print(map_request)
        print("Http статус:", resp.status_code, "(", resp.reason, ")")
        sys.exit(1)

    return resp


def save_resp(resp, file_name):
    # Запишем полученное изображение в файл.
    map_file = file_name
    with open(map_file, "wb") as file:
        file.write(resp.content)


image_paths = []

for ind, coord in enumerate(coordinates, 1):
    file_path = f'map{ind}.png'
    map_url = map_request.format(coord)
    response = get_resp(map_url)
    save_resp(response, file_path)
    image_paths.append(file_path)

# Инициализируем pygame
pygame.init()
screen = pygame.display.set_mode((600, 450))
image_ind = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            image_ind += 1
            image_ind = image_ind % len(image_paths)
    image_path = image_paths[image_ind]
    screen.blit(pygame.image.load(image_path), (0, 0))
    pygame.display.flip()

pygame.quit()

for file_path in image_paths:
    # Удаляем за собой файл с изображением.
    os.remove(file_path)
