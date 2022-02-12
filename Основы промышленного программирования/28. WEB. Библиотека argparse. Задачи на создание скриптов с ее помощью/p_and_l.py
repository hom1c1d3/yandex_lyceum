import argparse


def time_period_to_day(period_kind, period):
    translation = {
        'day': 1,
        'week': 7,
        'month': 30,
        'year': 360,
    }
    days = period * translation[period_kind]
    return days


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('--per-day', type=int, default=0)
    parser.add_argument('--per-week', type=int, default=0)
    parser.add_argument('--per-month', type=int, default=0)
    parser.add_argument('--per-year', type=int, default=0)

    parser.add_argument('--get-by', choices=['day', 'month', 'year'], default='day')

    args = parser.parse_args()

    proceeds = 0

    proceeds += args.per_day
    proceeds += args.per_week / 7
    proceeds += args.per_month / 30
    proceeds += args.per_year / 360

    if args.get_by == 'month':
        proceeds *= 30
    elif args.get_by == 'year':
        proceeds *= 360

    proceeds = int(proceeds)

    print(proceeds)


if __name__ == '__main__':
    main()