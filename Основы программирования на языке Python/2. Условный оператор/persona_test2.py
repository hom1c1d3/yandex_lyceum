question1 = "Что вы предпочетаете на второе? "
answer_guess1 = ("ролтон", "доширак", "пельмени")
answer1 = input(question1 + " | ".join(answer_guess1) + "\n").lower()
if answer1 not in answer_guess1:
    exit("Стоп, я этого не ожидал")
question2 = "Сколько звезд в обозримой вселенной? "
answer_guess2 = ("много", "не знаю", "100 миллиардов")
answer2 = input(question2 + " | ".join(answer_guess2) + "\n").lower()
if answer2 not in answer_guess2:
    exit("Стоп, я этого не ожидал")
question3 = "Любимая буква алфавита? "
answer_guess3 = ("а", "я", "м")
answer3 = input(question3 + " | ".join(answer_guess3) + "\n").lower()
if answer3 not in answer_guess3:
    exit("Стоп, я этого не ожидал")

if answer1 == answer_guess1[0] or answer1 == answer_guess1[1]:
    if answer2 == answer_guess2[0]:
        if answer3 == answer_guess3[1]:
            print("Вы интеллектуал.")
        else:
            print("Вы не любите терять свое время.")
    else:
        print("У вас очень решительный характер.")
if answer1 == answer_guess1[2]:
    if answer2 == answer_guess2[2]:
        if answer3 == answer_guess3[2]:
            print("Вы способны на большее!")
        else:
            print("Вы всесторонне развитый человек.")
    else:
        print("Вы сомодостаточный человек.")
