import requests

user_data = input()
geocoder_request = f"https://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode={user_data}&format=json"
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
        # print(toponym_address + ',', toponym["metaDataProperty"]["GeocoderMetaData"]['AddressDetails']['Country']['AdministrativeArea']['AdministrativeAreaName'], "имеет координаты:", toponym_coordinates)
        print(user_data, '-', toponym["metaDataProperty"]["GeocoderMetaData"]['AddressDetails']['Country']['AdministrativeArea']['AdministrativeAreaName'])
        # print(user_data, '-', toponym["metaDataProperty"]["GeocoderMetaData"]['Address']['Components'][1]['name'])

else:
    print("Произошла ошибка")
    print(geocoder_request)
    print("Http status", resp.status_code)
    print(resp.reason)