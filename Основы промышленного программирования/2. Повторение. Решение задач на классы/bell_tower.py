class LittleBell:

    @staticmethod
    def sound():
        print('ding')


class BigBell:

    def __init__(self):
        self.bell = True

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
