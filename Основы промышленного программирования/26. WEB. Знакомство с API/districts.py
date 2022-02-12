import requests

user_data = ['Хабаровск', 'Уфа', 'Нижний Новгород', 'Калининград']


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
            print("Ничего не найдено")
        else:
            print(data, '-', toponym["metaDataProperty"]
                                    ["GeocoderMetaData"]
                                    ['Address']
                                    ['Components']
                                    [1]
                                    ['name'])

    else:
        print("Произошла ошибка")
        print(geocoder_request)
        print("Http status", resp.status_code)
        print(resp.reason)


for i in user_data:
    get_request_result(i)
