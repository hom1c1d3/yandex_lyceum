class NaughtyChild:

    def __init__(self, name, volume, cry):
        self.name = name
        self.volume = volume
        self.cry = cry

    def change_cry(self, line):
        change_volume_delta = len(line) - len(self.cry)
        self.volume = self.volume + change_volume_delta if change_volume_delta > 0 else self.volume
        self.volume = 100 if self.volume > 100 else self.volume
        self.cry = line

    def __add__(self, other):
        self.volume += other
        self.volume = 1 if self.volume < 1 else self.volume
        self.volume = 100 if self.volume > 100 else self.volume
        return self

    def __call__(self, arg):
        arg = arg.capitalize()
        return self.volume // 10 * arg

    def __str__(self):
        return f'Naughty Child {self.name} has {self.volume} loudness'

    def __lt__(self, other):
        names = sorted((self, other), key=lambda x: (x.volume, len(self.cry), self.name), reverse=False)
        return [self, other] == names

    def __le__(self, other):
        return self < other and self == other

    def __gt__(self, other):
        names = sorted((self, other), key=lambda x: (x.volume, len(self.cry), self.name), reverse=True)
        return [self, other] == names

    def __eq__(self, other):
        return all(a == b for a, b in zip((self.volume, len(self.cry), self.name),
                                          (other.volume, len(other.cry), other.name)))

    def __repr__(self):
        return str(self)


def main():
    nc = NaughtyChild("Victoria", 50, "I WANT A DO-O-O-OGGY")
    nc = NaughtyChild("Morgan", 19, "give me a car")
    nc1 = NaughtyChild("Sophie", 28, "meow")
    print(nc > nc1)
    nc += 9
    print(nc1 <= nc)
    print(nc, nc1, sep='\n')


if __name__ == '__main__':
    main()
