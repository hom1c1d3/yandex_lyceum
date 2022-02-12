import re

mail_names = [input() for _ in range(int(input()))]
# разделяет на имя, номер и остальную часть
mail_names = re.findall(r'([a-zA-Z]+_[a-zA-Z]+)(\d*)(@untitled\.py)', '\n'.join(mail_names))
for _ in range(int(input())):
    new_name = input()
    same_names = list(filter(lambda x: x[0] == new_name, mail_names))
    if not same_names:
        new_mail_name = (new_name, '', '@untitled.py')
        mail_names.append(new_mail_name)
        print(*new_mail_name, sep='')
        continue
    max_same_name = list(max(same_names, key=lambda x: x[1]))
    max_same_name[1] = str(int(max_same_name[1]) + 1) if max_same_name[1] else str(1)
    mail_names.append(max_same_name)
    new_mail_name = ''.join(max_same_name)
    print(new_mail_name)
