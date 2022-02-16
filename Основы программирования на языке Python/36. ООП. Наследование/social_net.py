class User:

    def __init__(self, username):
        self.username = username

    def send_message(self, user, message):
        pass

    def post(self, message):
        pass

    def info(self):
        return ''

    def describe(self):
        print(self.username, self.info())


class Person(User):

    def __init__(self, username, birth):
        super().__init__(username)
        self.birth = birth

    def info(self):
        return f'Дата рождения: {self.birth}'

    def subscribe(self, user: User):
        pass


class Community(User):

    def __init__(self, username, description):
        super().__init__(username)
        self.description = description

    def info(self):
        return f'Описание: {self.description}'
