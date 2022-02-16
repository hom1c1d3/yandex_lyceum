import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--barbie', default=50, type=int)
args = parser.parse_args()
barbie = args.barbie
barbie = barbie if 0 <= barbie <= 100 else 50
cars = args.cars
cars = cars if 0 <= cars <= 100 else 50
movie = {'melodrama': 0, 'football': 100, 'other': 50}[args.movie]
boy = (100 - barbie + cars + movie) / 3
boy = int(boy)
girl = 100 - boy

print('boy:', boy)
print('girl:', girl)
