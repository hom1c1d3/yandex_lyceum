question1 = "Вы любите программировать на Python? "
answer1 = input(question1)
question2 = "Вы знаете анлийский язык? "
answer2 = input(question2)

if (answer1 != "да" and answer1 != "нет") or (answer2 != "да" and answer2 != "нет"):
    print("ОТВЕЧАЙТЕ ТОЛЬКО 'ДА' ИЛИ 'НЕТ'")
    exit()

if answer1 == "да":
    if answer2 == "да":
        print("Вы приняты в Янедкс!")
    else:
        print("Как вы смогли выжить!?")
elif answer1 == "нет":
    if answer2 == "нет":
        print("Мы вам перезвоним")
    else:
        print("Вы достаточно консервативны")
