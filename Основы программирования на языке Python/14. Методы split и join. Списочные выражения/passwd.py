info = []
person = input().split(':')

while all(person):
    person = person[0], person[4].split(',')[0], person[1]
    info.append(person)
    person = input().split(':')

passwd = input().split(';')

for i in info:
    if i[-1] in passwd:
        print(f"""To: {i[0]}
{i[1]}, ваш пароль слишком простой, смените его.""")
