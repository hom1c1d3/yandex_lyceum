from typing import List, Optional, Union, Set, Dict, Callable
from collections import UserList
import datetime
from copy import deepcopy
import itertools

cinema_chain_names_db: Set[str] = set()
FilmName = str
CinemaAddress = str


class CinemaChain:

    def __init__(self, name: str):
        if name in cinema_chain_names_db:
            raise ValueError(f'Cinema chain {name:r} already exists')
        cinema_chain_names_db.add(name)
        self.name = name
        self.cinemas: Dict[str, 'Cinema'] = {}

    def __repr__(self):
        return f'{self.__class__.__name__}({repr(self.name)})'

    def __str__(self):
        return f'Cinema Chain "{self.name.capitalize()}"'

    def get_films(self) -> Set['Film']:
        return {j.sessions_film for i in self.cinemas.values()
                for j in i.film_sessions_dict.values()}


class Cinema:

    def __init__(self, cinema_chain: CinemaChain, address=''):
        self.cinema_chain = cinema_chain
        if address in self.cinema_chain.cinemas:
            raise ValueError(f'Cinema on {address:r} already exists')
        self.cinema_chain.cinemas[address] = self
        self.address = address
        self.cinema_halls: Dict[int, CinemaHall] = {}
        for i in self.cinema_halls:
            i.cinema = self
        self.film_sessions_dict: Dict[FilmName, FilmSessions] = {}

    def __repr__(self):
        return f'{self.__class__.__name__}{self.cinema_chain, self.address, self.cinema_halls}'

    def __str__(self):
        return f'{self.cinema_chain} on "{self.address}" with {len(self.cinema_halls)} halls'


class Seat:

    def __init__(self, number: int):
        self.number = number
        self.cinema_hall: Optional[CinemaHall] = None
        self.price: Optional[int] = None

    def __str__(self):
        return f'[{str(self.number).center(3)}]'

    def __repr__(self):
        return f'{self.__class__.__name__}({self.number})'


class CinemaHall(UserList):

    def __init__(self, cinema: Cinema, number: int, seats: List[List[Seat]]):
        self.number = number
        super().__init__(seats)
        for r in self:
            for s in r:
                s.cinema_hall = self
        self.cinema = cinema
        self.cinema.cinema_halls[number] = self

    def __str__(self):
        return self.printable_seats(self)

    @staticmethod
    def printable_seats(seats):
        max_len_row = max(map(len, seats))
        res = ''
        for i in seats:
            row = ''.join(str(j) for j in i)
            row = row.center(max_len_row * len(str(i[0])))
            res += row
            res += '\n'
        return res

    def __repr__(self):
        return f'{self.__class__.__name__}{self.number, self.data}'


class Film:

    def __init__(self, name: str):
        self.name = name
        self.film_sessions_dict: Dict[CinemaAddress, FilmSessions] = {}

    def __repr__(self):
        return f'{self.__class__.__name__}({self.name})'

    def __str__(self):
        return self.name.title()


class FilmSession:

    def __init__(self, film: Film,
                 session_datetime: datetime.datetime,
                 session_duration: datetime.timedelta,
                 price: Union[List[List[int]], int],
                 cinema_hall: CinemaHall):
        self.film = film
        self.cinema_hall = cinema_hall
        self.duration = session_duration
        self.price = None
        self.set_price(price)
        self.session_time = session_datetime

    def __repr__(self):
        return (f'{self.__class__.__name__}' +
                f'{self.film, self.session_time, self.duration, self.price, self.cinema_hall}')

    # def __str__(self):
    #     return f"on {self.session_time.strftime('%d.%m.%Y at %H:%M')} by {self.price} $"

    def __str__(self):
        return f"at {self.session_time.strftime('%H:%M')} by {self.price} $"

    def set_price(self, price):
        if all(j is not None for i in self.cinema_hall for j in i):
            try:
                for row_ind, i in enumerate(price):
                    for col_ind, j in enumerate(i):
                        self.cinema_hall[row_ind][col_ind].price = j
                price = min(j for i in price for j in i)
            except TypeError:
                for i in self.cinema_hall:
                    for j in i:
                        j.price = j
        if int(price) > 0:
            self.price = int(price)
        else:
            raise ValueError('Price must be more thant zero')


class FilmSessions(UserList[FilmSession]):

    def __init__(self, cinema: Cinema, film_sessions: List[FilmSession]):
        self.check_time_intersection(film_sessions)
        self.cinema = cinema
        super().__init__(film_sessions)
        self.sessions_film, = set(i.film for i in self)
        if self.sessions_film.name not in self.cinema.film_sessions_dict:
            self.cinema.film_sessions_dict[self.sessions_film.name] = self
        else:
            self.cinema.film_sessions_dict[self.sessions_film.name] += self
        for i in self.data:
            if self.cinema.address not in i.film.film_sessions_dict:
                i.film.film_sessions_dict[self.cinema.address] = self
            else:
                i.film.film_sessions_dict[self.cinema.address] += self

    def __repr__(self):
        return f'{self.__class__.__name__}{self.cinema, self.data}'

    def get_film_sessions_by_date(self, film_session_date: datetime.date) -> 'FilmSessions':
        return self.__class__(self.cinema, [i for i in self.data
                                            if i.session_time.date() == film_session_date])

    def __str__(self):
        return f'you can watch {self.sessions_film} {", ".join(str(i) for i in self)}'

    @staticmethod
    def check_time_intersection(film_sessions: List[FilmSession]):
        start_end_sessions = [(i.session_time, i.session_time + i.duration) for i in film_sessions]
        start, end = datetime.datetime.min, datetime.datetime.min
        for s, e in start_end_sessions:
            if end >= s:
                raise ValueError('film sessions contains time intersections')
            start, end = s, e


class TicketSystemInterface:

    def __init__(self, cinema_chain_name):
        self.cinema_chain = CinemaChain(cinema_chain_name)
        self.seats_configs: Dict[int, List[List[Seat]]] = {}

    def add_cinema(self, address=''):
        Cinema(self.cinema_chain, address)  # Привязывется к self.cinema_chain

    def add_seats_config(self, seats_config: List[List[Seat]], seats_config_number: int) -> None:
        if seats_config in self.seats_configs.values():
            raise ValueError(f'Seats configuration already exists')
        self.seats_configs[seats_config_number] = seats_config

    def add_cinema_hall(self, cinema_address: str, number: int, seats_config_number: int):
        cinema = self.cinema_chain.cinemas[cinema_address]
        # Привязывается к cinema
        CinemaHall(cinema, number, deepcopy(self.seats_configs[seats_config_number]))

    def add_film_session(self, cinema_address: str,
                         film_name: str,
                         session_datetime: datetime.datetime,
                         session_duration: datetime.timedelta,
                         price: Union[List[List[int]], int],
                         cinema_hall_number: int):
        film = Film(film_name)  # TODO: сделать отдельный список фильмов
        cinema = self.cinema_chain.cinemas[cinema_address]
        try:
            cinema_hall = cinema.cinema_halls[cinema_hall_number]
        except KeyError:
            raise ValueError
        film_session = FilmSession(film, session_datetime, session_duration, price, cinema_hall)
        FilmSessions(cinema, [film_session])  # Прикрепляется к cinema

    def get_sessions(self, *, cinema_address: Optional[str] = None,
                     film_name: Optional[str] = None,
                     session_date: Optional[datetime.date] = None,
                     is_min_time: bool = False):
        for cinema_adr, cinema in self.cinema_chain.cinemas.items():
            if cinema_adr != (cinema_address if cinema_address is not None else cinema_adr):
                continue
            for flm_name, flm_sessions in cinema.film_sessions_dict.items():
                if flm_name != (film_name if film_name is not None else flm_name):
                    continue
                min_session_time = datetime.time.max
                for flm_session in flm_sessions:
                    if flm_session.session_time.date() != (session_date if session_date is not None
                    else flm_session.session_time.date()):
                        continue
                    if flm_session.session_time.time() < min_session_time:
                        min_session_time = flm_session.session_time.time()
                    else:
                        if is_min_time:
                            continue
                    yield flm_session


class BaseMenuItem:

    def __init__(self, item_text):
        self.text = item_text

    def __str__(self):
        return self.text

    def run(self):
        raise NotImplemented


class FunctionItem(BaseMenuItem):

    def __init__(self, item_text, func: Callable, *func_args, **func_kwargs):
        super().__init__(item_text)
        self.func = func
        self.args = func_args
        self.kwargs = func_kwargs

    def run(self):
        return self.func(*self.args, **self.kwargs)


EXIT = 1


class ExitItem(BaseMenuItem):

    def __init__(self):
        super().__init__('Выйти')

    def run(self):
        return EXIT


class Menu:

    def __init__(self, title, subtitle=None):
        self.items: List[BaseMenuItem] = [ExitItem()]
        self.title = title
        self.subtitle = '' if subtitle is None else subtitle
        self.parent_menu: Optional[Menu] = None

    def append_item(self, item: BaseMenuItem):
        self.items.append(item)

    def display_items(self):
        for ind, item in enumerate(self.items):
            print(ind, item, sep=' — ')

    def display(self):
        print(self.title)
        if self.subtitle:
            print(self.subtitle)
        print()
        self.display_items()
        print()

    def get_option_id(self):
        in_value = input('>>> ')
        try:
            in_value = int(in_value)
            if in_value not in range(len(self.items)):
                raise ValueError
        except ValueError:
            raise
        return in_value

    def run(self):
        res = 0
        while res != EXIT:
            self.display()
            try:
                option_id = self.get_option_id()
                item = self.items[option_id]
                res = item.run()
            except ValueError:
                print('Попробуйте еще раз')


class SubmenuItem(BaseMenuItem):

    def __init__(self, item_text, menu: Menu, parent_menu: Menu):
        super().__init__(item_text)
        self.menu = menu
        self.menu.parent_menu = parent_menu

    def run(self):
        self.menu.run()


class TicketSystemUserInterface:

    def __init__(self):
        self.main_menu = Menu('Билетная система')
        self.add_creation_cinema_chain()
        self.tsi: Optional[TicketSystemInterface] = None

    def add_creation_cinema_chain(self):
        cinema_chain_submenu = Menu('Создание сети кинотеатров')
        get_cinema_chain_name_item = FunctionItem('Дать имя сети кинотеатров',
                                                  self.create_ticket_system_interface,
                                                  'Введите имя сети кинотеатров: ')
        cinema_chain_submenu.append_item(get_cinema_chain_name_item)
        cinema_chain_submenu_item = SubmenuItem('Создать сеть кинотеатров',
                                                cinema_chain_submenu,
                                                self.main_menu)
        self.main_menu.append_item(cinema_chain_submenu_item)

    def create_ticket_system_interface(self, prompt):
        name = input(prompt)
        self.tsi = TicketSystemInterface(name)
        self.add_ticket_system_interface_item()
        self.main_menu.items.pop(-2)

    def add_ticket_system_interface_item(self):
        tsi_submenu = Menu(self.main_menu.title, self.tsi.cinema_chain.name)
        self.main_menu.append_item(SubmenuItem(self.tsi.cinema_chain.name,
                                               tsi_submenu,
                                               self.main_menu))
        self.add_cinema_creation_item(tsi_submenu)

    def add_cinema_creation_item(self, tsi_menu: Menu):
        cinema_creation_menu = Menu('Создание кинотеатров')
        cinema_creation_item = FunctionItem('Задать адрес кинотеатра', self.create_cinema,
                                            'Введите адрес кинотеатра: ', tsi_menu)
        cinema_creation_menu.append_item(cinema_creation_item)
        cinema_creation_menu_item = SubmenuItem('Создать кинотеатр', cinema_creation_menu, tsi_menu)
        tsi_menu.append_item(cinema_creation_menu_item)

    def create_cinema(self, prompt, menu: Menu):
        cinema_address = input(prompt)
        self.tsi.add_cinema(cinema_address)
        self.add_cinema_item(cinema_address, menu)

    def add_cinema_item(self, cinema_address, menu: Menu):
        cinema = self.tsi.cinema_chain.cinemas[cinema_address]
        cinema_menu = Menu(menu.subtitle, cinema.address)
        menu.append_item(SubmenuItem(cinema.address, cinema_menu, menu))
        self.add_seats_config_creation_item(cinema_menu)

    def add_seats_config_creation_item(self, menu: Menu):
        seats_config_creation_menu = Menu(menu.subtitle, 'Создание кофигурации кресел')
        seats_config_creation_item = FunctionItem('Задать конфигурацию кресел',
                                                  self.create_seats_configuration,
                                                  'Введите количество строк, колонок'
                                                  ' и номер конфигурации кресел (8 11 1): ',
                                                  menu)
        seats_config_creation_menu.append_item(seats_config_creation_item)
        seats_config_creation_menu_item = SubmenuItem('Создать конфигурацию кресел',
                                                      seats_config_creation_menu, menu)
        menu.append_item(seats_config_creation_menu_item)

    def create_seats_configuration(self, prompt, menu: Menu):
        row, col, seats_config_number = input(prompt).split()
        row, col, seats_config_number = int(row), int(col), int(seats_config_number)
        seats_config = [[Seat(j) for j in range(col)] for _ in range(row)]
        self.tsi.add_seats_config(seats_config, seats_config_number)
        self.add_display_seats_configuration_item(menu)
        self.add_cinema_hall_creation_item(menu)

    def add_display_seats_configuration_item(self, menu: Menu):
        display_seats_configuration_item = FunctionItem('Показать все конфигурации кресел',
                                                        lambda: print(
                                                            self.get_printable_seats_configurations(
                                                                self.tsi.seats_configs)))
        if display_seats_configuration_item.text not in list(map(str, menu.items)):
            menu.append_item(display_seats_configuration_item)

    def add_cinema_hall_creation_item(self, menu: Menu):
        cinema_hall_creation_menu = Menu(menu.subtitle, 'Создание зала')
        cinema_hall_creation_item = FunctionItem('Создать конфигурацию кресел зала',
                                                 self.create_cinema_hall,
                                                 'Введите номер зала и номер конфигурации кресел'
                                                 ' (1 1): ',
                                                 menu)  # menu.subtitle - адрес
        cinema_hall_creation_menu.append_item(cinema_hall_creation_item)
        cinema_hall_creation_menu_item = SubmenuItem('Создать зал', cinema_hall_creation_menu, menu)
        if cinema_hall_creation_menu_item.text not in list(map(str, menu.items)):
            menu.append_item(cinema_hall_creation_menu_item)

    @staticmethod
    def get_printable_seats_configurations(seats_configurations: Dict[int, List[List[Seat]]]):
        string_rows_seats_configs = []
        for num, i in seats_configurations.items():
            string_rows = CinemaHall.printable_seats(i).splitlines()
            string_num = str(num).center(len(string_rows[0]))
            rows = [string_num] + string_rows
            string_rows_seats_configs.append(rows)
        max_rows = max(len(i) for i in string_rows_seats_configs)
        for i in string_rows_seats_configs:
            len_row = len(i[0])
            for j in range(max_rows - len(i)):
                i.append(' ' * len_row)
        string_seats_configs = zip(*string_rows_seats_configs)
        string_seats_configs = '\n'.join('\t\t'.join(j for j in i) for i in string_seats_configs)
        return string_seats_configs

    def add_display_cinema_halls_item(self, menu: Menu):
        def display_cinema_halls():
            cinema_halls = self.tsi.cinema_chain.cinemas[menu.subtitle].cinema_halls
            cinema_halls_configs = {a: b.data for a, b in cinema_halls.items()}
            print(self.get_printable_seats_configurations(cinema_halls_configs))
        display_cinema_halls_item = FunctionItem('Показать все залы', display_cinema_halls)
        if display_cinema_halls_item.text not in list(map(str, menu.items)):
            menu.append_item(display_cinema_halls_item)

    def create_cinema_hall(self, prompt, menu: Menu):
        string_seats_configs = self.get_printable_seats_configurations(self.tsi.seats_configs)
        print(string_seats_configs)
        hall_number, seats_config_number = input(prompt).split()
        hall_number, seats_config_number = int(hall_number), int(seats_config_number)
        self.tsi.add_cinema_hall(menu.subtitle, hall_number, seats_config_number)
        self.add_display_cinema_halls_item(menu)
        self.add_film_session_creation_item(menu)

    def add_film_session_creation_item(self, menu: Menu):
        film_session_creation_menu = Menu(menu.subtitle, 'Создание показа фильма')
        film_session_creation_item = FunctionItem('Задать показ фильма',
                                                  self.create_film_session,
                                                  menu)  # menu.subtitle - адрес
        film_session_creation_menu.append_item(film_session_creation_item)
        film_session_creation_menu_item = SubmenuItem('Создать показ фильма',
                                                      film_session_creation_menu, menu)
        if film_session_creation_menu_item.text not in list(map(str, menu.items)):
            menu.append_item(film_session_creation_menu_item)

    def create_film_session(self, menu: Menu):
        film_name = input('Введите название фильма: ')
        date_and_time = datetime.datetime.fromisoformat(
            input('Введите дату и время показа (год-месяц-числоTчас:минута): '))
        duration = (datetime.datetime.strptime(input('Введите длительность показа (час:минута): '),
                                               '%H:%M')
                    - datetime.datetime.min.replace(year=1900))
        price = int(input('Введите цену: '))
        cinema_hall_number = int(input('Введите номер зала: '))
        cinema_address = menu.subtitle
        self.tsi.add_film_session(cinema_address, film_name, date_and_time, duration, price,
                                  cinema_hall_number)
        self.add_display_film_session_item(menu)

    def add_display_film_session_item(self, menu: Menu):
        display_film_sessions_menu = Menu(menu.subtitle, 'Показы фильмов')
        display_all_film_sessions_item = FunctionItem('Отобразите все показы',
                                                      self.display_all_film_sessions_in_cinema,
                                                      display_film_sessions_menu)
        display_film_sessions_menu.append_item(display_all_film_sessions_item)
        display_film_sessions_menu_item = SubmenuItem('Отобразить показы фильмов',
                                                      display_film_sessions_menu, menu)
        if display_film_sessions_menu_item.text not in list(map(str, menu.items)):
            menu.append_item(display_film_sessions_menu_item)

    def display_all_film_sessions_in_cinema(self, menu: Menu):
        sessions = self.tsi.get_sessions(cinema_address=menu.title)
        self.display_film_sessions(sessions)

    @staticmethod
    def display_film_sessions(film_sessions):
        sessions = sorted(film_sessions, key=lambda x: x.session_time.date())
        for dt, i in itertools.groupby(sessions, lambda x: x.session_time.date()):
            print(dt)
            sessions_by_film = sorted(i, key=lambda x: x.film.name)
            for flm, j in itertools.groupby(sessions_by_film, key=lambda x: x.film.name):
                print('\t', flm, sep='')
                for session in sorted(j, key=lambda x: x.session_time.time()):
                    print('\t\t', session, sep='')

    def run(self):
        self.main_menu.run()


def test():
    cinema_chain = CinemaChain('')
    seats = [[Seat(j) for j in range(9)]] + [[Seat(j) for j in range(11)] for _ in range(8)]
    cinema = Cinema(cinema_chain)
    film = Film('requiem')
    sessions = [FilmSession(film,
                            datetime.datetime.now() + datetime.timedelta(hours=i),
                            datetime.timedelta(minutes=50),
                            1, CinemaHall(cinema, i, seats)) for i in range(30)]
    film_sessions = FilmSessions(cinema, sessions)
    print(film_sessions)
    print('In', cinema, film_sessions.get_film_sessions_by_date(
        datetime.date.today().replace(day=datetime.date.today().day + 1)))


def test1():
    tsi = TicketSystemInterface('Kino')
    tsi.add_cinema('Pupkina street')
    seats_config = [[Seat(j) for j in range(9)]] + [[Seat(j) for j in range(11)] for _ in range(8)]
    tsi.add_seats_config(seats_config, 1)
    tsi.add_cinema_hall('Pupkina street', 1, 1)
    for i in range(30):
        tsi.add_film_session('Pupkina street', 'Requiem',
                             datetime.datetime.now() + datetime.timedelta(hours=i),
                             datetime.timedelta(minutes=50), 150, 1)
    print(next(iter(tsi.cinema_chain.get_films())).film_sessions_dict['Pupkina street'])
    print(list(tsi.get_sessions(session_date=datetime.date.today(), is_min_time=True)))


def test2():
    menu = Menu('Билетная система')
    cinema_chain_submenu = Menu('Сеть кинотеатров')
    get_cinema_chain_name_item = FunctionItem('Дать имя сети кинотеатров', input,
                                              'Введите имя сети кинотеатров: ')
    cinema_chain_submenu.append_item(get_cinema_chain_name_item)
    cinema_chain_submenu_item = SubmenuItem('Создать сеть кинотеатров', cinema_chain_submenu, menu)
    menu.append_item(cinema_chain_submenu_item)
    menu.run()


def main():
    tsui = TicketSystemUserInterface()
    tsui.run()
    print()


if __name__ == '__main__':
    main()
