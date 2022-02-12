class Weapon:

    def __init__(self, name, damage, weapon_range):
        self.name = name
        self.damage = damage
        self.range = weapon_range

    def hit(self, actor, target):
        if not target.is_alive():
            print('Враг уже повержен')
            return
        distance = (sum((p - q) ** 2.0
                        for p, q in zip(actor.get_coords(), target.get_coords()))) ** 0.5
        if distance > self.range:
            print(f'Враг слишком далеко для оружия {self.name}')
            return
        print(f'Врагу нанесен урон оружием {self.name} в размере {self.damage}')
        target.get_damage(self.damage)

    def __str__(self):
        return self.name


class BaseCharacter:

    def __init__(self, pos_x, pos_y, hp):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.hp = hp

    def move(self, delta_x, delta_y):
        self.pos_x, self.pos_y = self.pos_x + delta_x, self.pos_y + delta_y

    def is_alive(self):
        return bool(self.hp)

    def get_damage(self, amount):
        self.hp -= amount
        self.hp = 0 if self.hp < 0 else self.hp

    def get_coords(self):
        return self.pos_x, self.pos_y


class BaseEnemy(BaseCharacter):

    def __init__(self, pos_x, pos_y, weapon, hp):
        super().__init__(pos_x, pos_y, hp)
        self.weapon = weapon

    def hit(self, target):
        if isinstance(target, MainHero):
            self.weapon.hit(self, target)
        else:
            print('Могу ударить только Главного героя')

    def __str__(self):
        return f"Враг на позиции ({self.pos_x}, {self.pos_y}) с оружием {self.weapon}"


class MainHero(BaseCharacter):

    def __init__(self, pos_x, pos_y, name, hp):
        super().__init__(pos_x, pos_y, hp)
        self.name = name
        self._inventory = []
        self._current_weapon = None
        self._max_hp = 200

    def hit(self, target):
        if not self._inventory:
            print('Я безоружен')
        elif not isinstance(target, BaseEnemy):
            print('Могу ударить только Врага')
        else:
            self._current_weapon.hit(self, target)

    def add_weapon(self, weapon):
        if not isinstance(weapon, Weapon):
            print('Это не оружие')
            return
        if not self._inventory:
            self._current_weapon = weapon
        self._inventory.append(weapon)
        print(f'Подобрал {weapon}')

    def next_weapon(self):
        if not self._inventory:
            print('Я безоружен')
        elif len(self._inventory) == 1:
            print('У меня только одно оружие')
        else:
            self._current_weapon = self._inventory.pop()
            self._inventory.insert(0, self._current_weapon)
            print(f'Сменил оружие на {self._current_weapon}')

    def heal(self, amount):
        self.hp += amount
        self.hp = self._max_hp if self.hp > self._max_hp else self.hp
        print(f'Полечился, теперь здоровья {self.hp}')
