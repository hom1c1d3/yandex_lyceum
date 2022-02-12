astronaut_list = []
astronaut_input = input()

while astronaut_input != '!':
    astronaut_list.append(astronaut_input)
    astronaut_input = input()

astronaut_filtred = list(
    filter(
        lambda height: 150 < height < 190,
        [int(i) for i in astronaut_list]
    ))

print(len(astronaut_filtred))
print(min(astronaut_filtred), max(astronaut_filtred))
