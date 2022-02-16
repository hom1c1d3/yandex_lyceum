import sys
from io import BytesIO
import requests
from PIL import Image


def main1():
    map_request = "http://static-maps.yandex.ru/1.x/?ll=133.795%2C-25.695&spn=20.464,20.780&l=sat"
    response = requests.get(map_request)
    Image.open(BytesIO(response.content)).show()


def main2():
    api_server = "http://static-maps.yandex.ru/1.x"
    lat = 135.795
    lon = -25.695
    delta_x = 20.464
    delta_y = 20.780
    map_type = "sat"
    params = {
        'll': f"{lat},{lon}",
        'spn': f"{delta_x},{delta_y}",
        'l': f"{map_type}"
    }
    response = requests.get(api_server, params=params)
    Image.open(BytesIO(response.content)).show()


def main():
    main2()


if __name__ == '__main__':
    main()