class Server:

    def __init__(self):
        self.users = {}

    def __setitem__(self, key, value):
        self.users[key] = value

    def __getitem__(self, item):
        return self.users[item]

    def __delitem__(self, item):
        del self.users[item]

    def __contains__(self, item):
        return item in self.users


class Client:

    def __init__(self, server: Server, user):
        server[user] = []
        self.user = user
        self.server = server

    def receive_mail(self):
        messages = self.server[self.user]
        return messages.pop() if messages else None

    def send_mail(self, server, user, message):
        if user in server:
            server[user].append(message)
        else:
            server[user] = [message]

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.user}')"


def main():
    server1 = Server()
    username1 = input("Имя первого пользователя: ")
    user1 = Client(server1, username1)
    print(user1)
    username2 = input('Имя второго пользователя: ')
    user2 = Client(server1, username2)
    print(user2)
    user1.send_mail(server1, username2, input("Сообщение для второго пользователя: "))
    user1.send_mail(server1, username2, input("Сообщение для второго пользователя: "))
    print("Получим все сообщения второго: ", *[user2.receive_mail() for _ in range(2)][::-1],
          sep='\t')
    user2.send_mail(server1, username1, input("Сообщение для первого пользователя: "))
    print("Получим все сообщения второго: ", *[user2.receive_mail() for _ in range(1)][::-1],
          sep='\t')


if __name__ == '__main__':
    main()
