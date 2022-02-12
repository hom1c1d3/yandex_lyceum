patience = int(input())
true_seq = ['раз', 'два', 'три', 'четыре']
count = 0

while patience:
    for i in range(4):
        indication = input()
        if indication in true_seq and true_seq.index(indication) == i:
            count += 1
        else:
            print(f'Правильных отсчётов было {count}, но теперь вы ошиблись.')
            count = 0
            patience -= 1
            break

print('На сегодня хватит.')