# #n - переход на новую строку внутри ячейки
# #c - запятая внутри ячейки

rules = {'#n': r'\n', '#c': ','}
text = [input() for i in range(int(input()))]
text = [[j.replace('#n', r'\n').replace('#c', ',') for j in i.split(',')] for i in text]
for i in range(int(input())):
    row, col = map(int, input().split(','))
    print(text[row][col])