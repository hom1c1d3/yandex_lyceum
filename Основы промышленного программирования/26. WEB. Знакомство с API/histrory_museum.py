import requests

user_data = "Красная площадь, 1, Москва, Россия"


def get_request_result(data):
    geocoder_request = f"https://geocode-maps.yandex.ru/" \
                       f"1.x/" \
                       f"?apikey=40d1649f-0493-4b70-98ba-98533de7710b" \
                       f"&geocode={user_data}&format=json"
    resp = requests.get(geocoder_request)

    if resp.ok:
        json_resp = resp.json()
        try:
            toponym = json_resp['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']
        except (KeyError, IndexError):
            print("Ничего не найдено")
        else:
            toponym_address = toponym["metaDataProperty"]["GeocoderMetaData"]["text"]
            toponym_coordinates = toponym['Point']['pos']
            print(toponym_address, "имеет координаты:", toponym_coordinates)
    else:
        print("Произошла ошибка")
        print(geocoder_request)
        print("Http status", resp.status_code)
        print(resp.reason)


get_request_result(user_data)