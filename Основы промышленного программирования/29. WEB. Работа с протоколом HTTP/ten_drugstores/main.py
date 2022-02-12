import sys
from io import BytesIO
from typing import List

from PIL import Image

from utils import *


def get_organization_pointers(organizations: List):
    pointers = []
    for org in organizations:
        try:
            hours = org['properties']['CompanyMetaData']['Hours']
        except KeyError:
            color = 'gr'
        else:
            available = hours['Availabilities']
            if available:
                is_all_day = available[0].get('TwentyFourHours', False)
                is_everyday = available[0].get('Everyday', False)
                if is_all_day and is_everyday:
                    color = 'gn'
                else:
                    color = 'bl'
            else:
                color = 'gr'
        coord = get_organization_coord(org)
        coord = ','.join(coord)
        pt_style = 'pm2'
        pt_size = 'l'
        pt = f"{coord},{pt_style}{color}{pt_size}"
        pointers.append(pt)
    return pointers


def main():
    toponym_to_find = " ".join(sys.argv[1:])
    geocode_res = get_geocode_result(toponym_to_find)
    try:
        toponym = get_toponym(geocode_res)
    except ValueError:
        print('Объект не найден')
        return 1
    lat, lon = get_ll_from_geocode_response(toponym)
    # span = 0.01
    # nearest_drugstores = []
    # while span < 100 and len(nearest_drugstores) < 10:
    #     span *= 2.0
    #
    #     nearest_drugstores = get_organizations_to_point('аптека', ll=",".join([lat, lon]),
    #                                                     spn=f'{span},{span}')
    nearest_drugstores = get_organizations_to_point('аптека', ll=",".join([lat, lon]),
                                                    spn=f'0.001,0.001')
    pointer_style = 'pm2'
    pointer_color = 'rd'
    pointer_size = 'l'
    pointer = f'{lat},{lon},{pointer_style}{pointer_color}{pointer_size}'
    drugstore_pointers = get_organization_pointers(nearest_drugstores['features'])
    pointers = '~'.join([pointer, ] + drugstore_pointers)
    image_raw = get_static_map(pt=pointers)
    Image.open(BytesIO(
        image_raw)).show()


if __name__ == '__main__':
    main()
