d = int(input())
number = int(input())
constant = 12431.25
count = 0
max_energy = 5000

for i in range(number):
    energy = input()
    success = False
    while energy != 'КОНЕЦ ЭКСПЕРИМЕНТА':
        if int(energy) >= max_energy:
            break
        energy = int(energy)
        wavelength = d / (constant / energy)
        if abs(wavelength - round(wavelength)) <= 0.1:
            success = True
            count += 1
        energy = input()
    print(i + 1, int(success))

print('Общее количество успешных экспериментов:', count)