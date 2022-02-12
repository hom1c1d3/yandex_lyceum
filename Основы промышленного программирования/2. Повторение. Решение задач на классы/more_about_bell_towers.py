class Bell:

    def __init__(self, *args, **kwargs):
        self.pos_info = args
        self.named_info = kwargs

    def print_info(self):
        pos_info = ', '.join(self.pos_info)
        named_info = sorted(self.named_info.items(), key=lambda x: x[0])
        named_info = ', '.join(f'{k}: {v}' for k, v in named_info)
        if pos_info and named_info:
            info = '; '.join((named_info, pos_info))
        elif pos_info or named_info:
            info = pos_info if pos_info else named_info
        else:
            info = '-'
        print(info)


class LittleBell(Bell):

    @staticmethod
    def sound():
        print('ding')


class BigBell(Bell):

    def __init__(self, *args, **kwargs):
        self.bell = True
        super().__init__(*args, **kwargs)

    def sound(self):
        if self.bell:
            print('ding')
        else:
            print('dong')
        self.bell = not self.bell


class BellTower:

    def __init__(self, *bells):
        self.bells = list(bells)

    def sound(self):
        for bell in self.bells:
            bell.sound()
        print('...')

    def append(self, bell):
        self.bells.append(bell)
